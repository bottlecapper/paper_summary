# Topic Map and Coverage Audit

Use a JSON list of topic groups. Each included highlight has exactly one primary assignment; merging repeated meanings across colors is expected. The helper recalculates group priority from actual annotations. Reader topic priority or logical presentation order can override color order in the summary; the audit inventory remains ordered by highlight priority and then paper order.

Each group requires `key`, `section`, `label`, `lead`, `highlight_ids`, and `context`. `lead` and each context string contain the exact summary Markdown, including any blue markers. Use a unique stable topic key and current-extraction highlight IDs. Optional fields include `subsection` (Human Review/Auto Judge), `review_category` (Review Approach/Quality Dimensions), and `presentation_order`.

```json
[
  {
    "key": "expert-review",
    "section": "Quality Control",
    "subsection": "Human Review",
    "review_category": "Review Approach",
    "label": "Review Approach",
    "lead": "Short source-supported description of this paper's review method.",
    "highlight_ids": [1, 2],
    "context": ["Distinct supporting detail with original wording when useful."]
  }
]
```

Before final audit, add an `evidence` list to each group. Each entry binds one or more of that group's highlight IDs to a literal, contiguous excerpt in the final Markdown and explains the shared meaning. Use the shortest excerpt that actually represents the selected content; a heading alone cannot stand in for a highlighted factual claim. Several entries can share a summary excerpt when selections repeat the same meaning. Use an empty assignment nowhere, and cover each primary ID once. This makes omissions inspectable instead of declaring coverage from topic names.

```json
"evidence": [
  {
    "highlight_ids": [1, 2],
    "summary_excerpt": "Exact excerpt copied from the final summary Markdown.",
    "meaning": "How this excerpt preserves every distinct selected point.",
    "transformation_reason": "Only when needed: why the complete selection is not quoted in blue, and how its details survive."
  }
]
```

Run `audit_highlights.py` with `--summary /output/summary/paper_slug.md`. It verifies evidence IDs and presence within the group's declared section/subsection. It also checks whether each full selection appears in a blue span, allowing PDF line wraps and hyphen repairs. If not, the evidence entry must give a `transformation_reason`: for example, author framing removed, repeated meaning merged, extracted formula reconstructed, combined table statistics, or heading capitalization changed. Explain the transformation for that selection and identify where its details survive; do not reuse a generic coverage assertion for unrelated selections. Brevity alone is not a reason to lose selected information; use collapsed source excerpts. Check each action, constraint, number, and qualification against the evidence, reviewing multi-part selections and rectangles point by point. When evidence spans several bullets, bind the smallest contiguous passage covering those points. A vague topic-level paraphrase or an entire group's presence cannot establish that its details are covered. The script cannot judge whether the meaning explanation or transformation is correct. Review that manually against the original selection and surrounding paper.

`context` may be empty for a concise original lead. A dimensions group may use its category title as `lead` and keep dimensions visible as context. Store additional web context or unhighlighted examples as supplementary fields on a relevant group, not as fabricated highlight IDs. Do not create an empty-highlight group: the audit orders groups by their actual selections.

For evidence intentionally reused under Special Design, add `secondary_presentations` to its primary group. Each presentation can have `section`, `label`, `lead`, `context`, `presentation_order`, and `related_group_keys`; it has no new primary highlight assignment. The agent checks that both presentations appear and preserve meaning. Retain internal source pages, figure/table identifiers, and permitted original example files.

```bash
python scripts/audit_highlights.py /output/.artifacts/paper_slug/extracted.json /output/.artifacts/paper_slug/topic_map.json --preferences /output/.artifacts/paper_slug/preferences.json --summary /output/summary/paper_slug.md --inventory /output/summary/paper_slug_highlights.md --report /output/.artifacts/paper_slug/coverage.json
```

For an audit of an existing summary, optionally pass `--prior-status prior_status.json`. That file maps highlight ID strings to `covered`, `partial`, `title_only`, or `missing`. These statuses require semantic review, not substring checks. Without it, the helper uses Not Assessed. The inventory's before/after language is bookkeeping, not independent proof of semantic coverage.

Run the helper when annotations, groups, or assignments change; a formatting-only change can retain the current map after checking its text still matches. Pass resolved preferences, not another paper's overrides. Check that all included selections are assigned, yellow questions remain excluded, and unknown colors/non-highlight annotations remain unclassified. Render the resulting inventory to its paired HTML without collapsing it.
