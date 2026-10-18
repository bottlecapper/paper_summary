#!/usr/bin/env python3
"""Validate a topic-to-highlight map and render a priority-ordered audit inventory.

The agent supplies semantic groups and prior coverage judgments. This helper
checks annotation accounting, not whether a paraphrase preserves every nuance.
"""
import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path


def normalized(text):
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def section_text(markdown, section, subsection=None):
    """Find a declared destination without matching another section's evidence."""
    heading = re.search(r"^## " + re.escape(section) + r"\s*$", markdown, re.M)
    if not heading:
        return ""
    remaining = markdown[heading.end():]
    end = re.search(r"^## ", remaining, re.M)
    remaining = remaining[:end.start()] if end else remaining
    if subsection:
        heading = re.search(r"^### " + re.escape(subsection) + r"\s*$", remaining, re.M)
        if not heading:
            return ""
        remaining = remaining[heading.end():]
        end = re.search(r"^### ", remaining, re.M)
        remaining = remaining[:end.start()] if end else remaining
    return remaining


def selection_variants(text):
    return {normalized(text),
            normalized(re.sub(r"(?<=\w)-\n(?=\w)", "", text)),
            normalized(re.sub(r"(?<=\w)-\n(?=\w)", "-", text))}


def validate_evidence(groups, markdown, annotations=None):
    """Validate actual evidence anchors, leaving semantic judgment to the reader."""
    bindings = {}
    blue = [normalized(part) for part in re.findall(r'<span class="verbatim">(.*?)</span>', markdown, re.S)]
    for group in groups:
        evidence = group.get("evidence", [])
        assigned = []
        destination = normalized(section_text(markdown, group["section"], group.get("subsection")))
        for item in evidence:
            ids = item.get("highlight_ids", [])
            excerpt = item.get("summary_excerpt", "")
            if not ids or not excerpt.strip() or not item.get("meaning", "").strip():
                raise SystemExit("Evidence needs highlight_ids, summary_excerpt, and meaning: " + group["key"])
            if normalized(excerpt) not in destination:
                raise SystemExit("Evidence excerpt absent from declared summary destination: " + group["key"])
            assigned.extend(ids)
            for i in ids:
                bindings[i] = {"summary_excerpt": excerpt, "meaning": item["meaning"]}
                if annotations is not None:
                    quoted = any(variant in fragment for variant in selection_variants(annotations[i]["text"]) for fragment in blue)
                    reason = item.get("transformation_reason", "").strip()
                    if not quoted and not reason:
                        raise SystemExit("H{:03d} is not retained as a complete blue selection; record a transformation_reason and review every distinct detail.".format(i))
                    bindings[i].update({"full_selection_quoted": quoted,
                                        "transformation_reason": reason if not quoted else None})
        if Counter(assigned) != Counter(group["highlight_ids"]):
            raise SystemExit("Evidence must represent each primary highlight exactly once: " + group["key"])
    return bindings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("extracted", type=Path)
    parser.add_argument("groups", type=Path)
    parser.add_argument("--preferences", type=Path, required=True)
    parser.add_argument("--prior-status", type=Path)
    parser.add_argument("--summary", type=Path, help="Require evidence bindings to the delivered Markdown")
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--title", default="Highlight Audit")
    args = parser.parse_args()
    extracted = json.loads(args.extracted.read_text(encoding="utf-8"))
    preferences = json.loads(args.preferences.read_text(encoding="utf-8"))
    groups = json.loads(args.groups.read_text(encoding="utf-8"))
    prior = json.loads(args.prior_status.read_text(encoding="utf-8")) if args.prior_status else {}
    colors = preferences["colors"]
    eligible, excluded, unclassified = {}, [], []
    for annotation in extracted["annotations"]:
        color = colors.get(annotation["hex"])
        if color is None or annotation["type"] not in color.get("annotation_types", ["Highlight"]):
            unclassified.append(annotation)
        elif color.get("include_in_summary"):
            eligible[annotation["id"]] = annotation
        else:
            excluded.append(annotation)
    assignments = [i for group in groups for i in group["highlight_ids"]]
    repeated = [i for i, n in Counter(assignments).items() if n > 1]
    missing = sorted(set(eligible) - set(assignments))
    extra = sorted(set(assignments) - set(eligible))
    if repeated or missing or extra:
        raise SystemExit("Invalid coverage map: " + json.dumps({"missing": missing, "duplicate": repeated, "ineligible": extra}))
    if len({group["key"] for group in groups}) != len(groups):
        raise SystemExit("Topic keys must be unique.")
    for group in groups:
        if not group.get("lead") or not isinstance(group.get("context"), list):
            raise SystemExit("Each topic requires a lead and a context list (which may be empty for a direct original sentence): " + group["key"])
    bindings = validate_evidence(groups, args.summary.read_text(encoding="utf-8"), eligible) if args.summary else {}
    def order(i):
        a = eligible[i]
        return colors[a["hex"]]["priority"], a["page"], a["id"]
    ordered = sorted(groups, key=lambda g: min(order(i) for i in g["highlight_ids"]))
    rows = []
    lines = ["# " + args.title, "",
             "All {} included highlights are mapped to the revised summary. Topics are ordered by their highest highlight priority; selections within each topic are ordered by priority, then paper order.".format(len(eligible)), "",
             "Prior-coverage judgments are a manual semantic review. Annotation accounting is checked programmatically. Raw selections retain PDF extraction artifacts; mathematical selections are explained in context in the summary.", "",
             "Previous statuses: **Covered**, **Partial**, **Title only**, or **Missing**. New coverage means the highlighted information is represented by a topic lead, source excerpt, definition, or merged equivalent passage—not that every duplicate fragment is repeated verbatim.", ""]
    labels = {"covered": "Covered", "partial": "Partial", "title_only": "Title only", "missing": "Missing", "not_assessed": "Not assessed"}
    for group in ordered:
        group_priority = min(order(i)[0] for i in group["highlight_ids"])
        path = []
        for part in [group["section"], group.get("subsection"), group.get("review_category"), group["label"]]:
            if part and (not path or path[-1] != part):
                path.append(part)
        destination = " → ".join(path)
        section_path = " · ".join(part for part in [group["section"], group.get("subsection"), group.get("review_category")] if part)
        lines += ["## " + group["label"], "", "**Priority {} · {}**".format(group_priority, section_path), "", group["lead"], ""]
        for i in sorted(group["highlight_ids"], key=order):
            a = eligible[i]
            color = colors[a["hex"]]
            status = prior.get(str(i), "not_assessed")
            if status not in labels:
                raise SystemExit("Unknown prior status: " + status)
            selection = a["text"].replace("\n", " ")
            # A delimiter longer than any source backtick run keeps raw text literal.
            fence = "`" * (max([len(run) for run in re.findall(r'`+', selection)] or [0]) + 1)
            lines += ["- **H{:03d} · {} · Before: {}**".format(i, color["name"], labels[status]),
                      "    - Selected text: " + fence + selection + fence,
                      "    - Now represented under **{}**.".format(destination), ""]
            if i in bindings:
                lines += ["    - Summary evidence: " + bindings[i]["summary_excerpt"],
                          "    - Meaning: " + bindings[i]["meaning"], ""]
                if bindings[i].get("transformation_reason"):
                    lines += ["    - Transformation reason: " + bindings[i]["transformation_reason"], ""]
            rows.append({"highlight_id": i, "color": a["hex"], "priority": color["priority"],
                         "source_page": a["page"], "original_selection": a["text"],
                         "prior_status": status, "current_group": group["key"],
                         "current_section": group["section"], "current_subsection": group.get("subsection"),
                         "current_review_category": group.get("review_category"),
                         "current_representation": "topic lead and supporting context" if group["context"] else "direct topic text"})
            if i in bindings:
                rows[-1].update(bindings[i])
    lines += ["## Excluded and Unclassified", ""]
    for annotation in excluded:
        lines.append("- H{:03d}: {} highlight, excluded by your color preferences.".format(annotation["id"], colors[annotation["hex"]]["name"]))
    for annotation in unclassified:
        lines.append("- H{:03d}: {} annotation ({}); meaning unclassified, not included in the highlight count.".format(annotation["id"], annotation["type"], annotation["hex"]))
    lines.append("")
    report = {"eligible_highlights": len(eligible), "mapped_highlights": len(rows), "topic_groups": len(groups),
              "unmapped": missing, "duplicates": repeated, "ineligible_assignments": extra,
              "prior_status_counts": dict(Counter(r["prior_status"] for r in rows)),
              "excluded_ids": [a["id"] for a in excluded], "unclassified_ids": [a["id"] for a in unclassified], "highlights": rows}
    report["evidence_anchors_verified"] = len(bindings)
    report["full_selections_quoted"] = sum(bool(item.get("full_selection_quoted")) for item in bindings.values())
    report["transformed_highlight_ids"] = sorted(i for i, item in bindings.items() if not item.get("full_selection_quoted"))
    report["semantic_review"] = "Agent review required; anchor presence does not establish semantic equivalence."
    args.inventory.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.inventory.write_text("\n".join(lines), encoding="utf-8")
    args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["eligible_highlights", "mapped_highlights", "topic_groups", "unmapped", "duplicates", "prior_status_counts"]}, indent=2))


if __name__ == "__main__":
    main()
