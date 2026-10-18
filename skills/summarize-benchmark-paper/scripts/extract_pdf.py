#!/usr/bin/env python3
"""Extract page text and geometric annotation selections without modifying a PDF."""
import argparse
import colorsys
import json
from collections import Counter
from pathlib import Path

import fitz


def color_name(rgb):
    if not rgb:
        return "Unspecified"
    h, s, v = colorsys.rgb_to_hsv(*rgb)
    if s < 0.12:
        return "White" if v > 0.9 else "Gray" if v > 0.2 else "Black"
    hue = h * 360
    name = next((name for limit, name in [(15, "Red"), (45, "Orange"), (80, "Yellow"),
                                         (165, "Green"), (195, "Cyan"), (255, "Blue"),
                                         (285, "Purple"), (345, "Pink"), (361, "Red")] if hue < limit), "Red")
    return ("Light " + name.lower()) if min(rgb) > 0.35 else name


def inside_quad(point, vertices):
    # PDF quad ordering is upper-left, upper-right, lower-left, lower-right.
    polygon = [vertices[i] for i in (0, 1, 3, 2)]
    signs = []
    x, y = point
    for i, (ax, ay) in enumerate(polygon):
        bx, by = polygon[(i + 1) % 4]
        cross = (bx - ax) * (y - ay) - (by - ay) * (x - ax)
        if abs(cross) > 0.01:
            signs.append(cross > 0)
    return not signs or all(signs) or not any(signs)


def selected_text(annotation, words):
    vertices = annotation.vertices or []
    quads = [vertices[i:i + 4] for i in range(0, len(vertices), 4) if len(vertices[i:i + 4]) == 4]
    selected = set()
    lines = []
    for quad in quads:
        matches = []
        for i, word in enumerate(words):
            center = ((word[0] + word[2]) / 2, (word[1] + word[3]) / 2)
            if i not in selected and inside_quad(center, quad):
                selected.add(i)
                matches.append(word[4])
        if matches:
            lines.append(" ".join(matches))
    if not quads:
        matches = []
        rect = annotation.rect
        for word in words:
            center = fitz.Point((word[0] + word[2]) / 2, (word[1] + word[3]) / 2)
            if rect.contains(center):
                matches.append(word[4])
        lines = [" ".join(matches)] if matches else []
    # Keep line endings: hyphenation and disconnected selections require human interpretation.
    return "\n".join(lines), "quad_word_centers" if quads else "rect_word_centers"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pages, annotations = [], []
    colors, types = {}, Counter()
    with fitz.open(str(args.pdf)) as doc:
        if doc.needs_pass:
            raise SystemExit("PDF is encrypted and requires a password.")
        metadata = doc.metadata
        for page in doc:
            words = page.get_text("words", sort=True)
            pages.append({"page": page.number + 1, "label": page.get_label(), "text": page.get_text("text", sort=True)})
            for annotation in page.annots() or []:
                kind = annotation.type[1]
                types[kind] += 1
                rgb = annotation.colors.get("stroke") or annotation.colors.get("fill")
                if rgb and len(rgb) == 3:
                    hex_color = "#" + "".join("{:02X}".format(round(max(0, min(1, c)) * 255)) for c in rgb)
                    rgb = list(rgb)
                else:
                    hex_color = "unspecified"
                text, method = selected_text(annotation, words)
                record = {"id": len(annotations) + 1, "page": page.number + 1,
                          "page_label": page.get_label(), "type": kind, "hex": hex_color,
                          "rgb": rgb, "text": text, "comment": annotation.info.get("content", ""),
                          "selection_method": method, "rect": list(annotation.rect)}
                annotations.append(record)
                if kind == "Highlight":
                    group = colors.setdefault(hex_color, {"hex": hex_color, "name": color_name(rgb),
                                                          "rgb": rgb, "count": 0, "pages": [], "sample": record})
                    group["count"] += 1
                    if record["page"] not in group["pages"]:
                        group["pages"].append(record["page"])
    result = {"source_name": args.pdf.name, "metadata": metadata, "page_count": len(pages),
              "annotation_types": dict(types), "highlight_colors": sorted(colors.values(), key=lambda g: -g["count"]),
              "annotations": annotations, "pages": pages,
              "pages_without_text": [p["page"] for p in pages if not p["text"].strip()],
              "empty_markup_ids": [a["id"] for a in annotations if a["type"] in ("Highlight", "Underline", "Squiggly", "StrikeOut") and not a["text"].strip()]}
    json_path = args.output_dir / "extracted.json"
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    (args.output_dir / "paper_text.txt").write_text("\n\n".join("=== PDF page {} ===\n{}".format(p["page"], p["text"]) for p in pages), encoding="utf-8")
    print(json.dumps({"extracted": str(json_path.resolve()), "pages": len(pages), "annotation_types": dict(types),
                      "colors": [{"name": g["name"], "hex": g["hex"], "count": g["count"], "pages": g["pages"]} for g in result["highlight_colors"]],
                      "pages_without_text": result["pages_without_text"], "empty_markup_ids": result["empty_markup_ids"]}, indent=2))


if __name__ == "__main__":
    main()
