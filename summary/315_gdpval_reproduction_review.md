# Benchmark Skill Reproduction Review

The benchmark skill is finalized after seven independent generations across four revisions. The latest two runs used the exact final skill, the original highlighted PDF, project preferences, and the raw official task example. Neither had access to the approved summary or the other run’s output. The approved Markdown and HTML remain unchanged.

## Major Gaps Fixed

- **Coverage:** Topic assignment alone could claim coverage without representing the highlighted detail. Every included highlight now needs evidence in the actual summary and its declared section. A selection not retained completely in blue needs a specific transformation reason and semantic review.
- **Classification:** Judge dataset validity under Quality Control and model deliverables under Model Evaluation. Keep sourcing qualifications separate from task-quality dimensions; distinguish review methods from assessed dimensions.
- **Source Fidelity:** Preserve coherent original excerpts containing distinct highlighted details. Prefer concise original leads, verify blue wording, and keep rewrites and reconstructed formulas in default color.
- **Readable Output:** Measure the visible overview, retain requested key statistics, and put supporting detail in expandable Source Excerpts. Render HTML from Markdown and check consistency.
- **Original Example:** Embed the complete original request and actual expert deliverable. Preserve Word’s procedure numbering without creating extra collapsed lists.
- **Portability:** The reusable skill contains no GDPval references or facts. GDPval’s editorial choices and example selection are in the project’s paper profile, applied only to its exact identifier. A different benchmark resolves without that profile.

## Final Verification

| Check | Run 6 | Run 7 (Saved Candidate) |
|---|---:|---:|
| Included highlights assigned once with actual-summary evidence | 117/117 | 117/117 |
| Verified blue excerpts in summary | 95/95 | 93/93 |
| Complete original request and expert deliverable | Pass | Pass |
| Required section and topic structure versus approved summary | Match | Match |
| Visible overview words | 642 | 734 |
| Overview at 200 words/minute | 3.21 min | 3.67 min |
| Reading label | ~4 minutes | ~4 minutes |
| Fresh matching Markdown/HTML | Pass | Pass |

All checked key numeric values are present. The candidate is not word-for-word identical: phrasing, excerpt length, and some within-topic ordering vary. No major content gap was found in the final review. Expanded excerpts are longer than the approved version; the four-minute estimate applies to the visible overview.

## Useful Differences

- **Repeated Attempts:** The candidate adds Table 2’s repeated-attempt limit: GPT-5 speed/cost ratios of 1.39×/1.63×, alongside the one-attempt 1.12×/1.18× scenario. These remain conditional modeled results in Source Excerpts.
- **Task Values:** It identifies the table means separately: $398.46 for gold and $391.44 for the full set, rather than only “around $400.”
- **Original Deliverable:** It preserves all seven original procedure numbers.

One precision improvement found during comparison is worth retaining in future edits: Table 7’s 89.07% well-specified figure refers to the gold subset; the full set is 89.34%. The candidate retains the original quotation without adding this explicit population label.

## Files and Limits

- [Final reusable skill](../skills/summarize-benchmark-paper/SKILL.md)
- [GDPval project profile](../paper_profiles/315_gdpval.md)
- [Regenerated Markdown](315_gdpval_regenerated.md)
- [Regenerated HTML](../html/315_gdpval_regenerated.html)
- [Regenerated highlight audit](../html/315_gdpval_regenerated_highlights.html)
- [Approved HTML](../html/315_gdpval.html)

Yellow H112 is excluded. H044 is an unclassified blue `#4B99FF` squiggly; no meaning was invented. Semantic coverage still requires agent judgment; scripts verify accounting, evidence anchors, and declared transformations rather than proving equivalence. HTML received structural checks, without a graphical browser review. Full forward-testing used this paper; portability checks do not establish performance on every other benchmark.
