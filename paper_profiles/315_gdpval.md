# GDPval Profile

Apply only to the annotated GDPval paper, never as a template of facts for another benchmark. Project overrides for slug `315_gdpval` are in `highlight_preferences.json` → `paper_overrides.315_gdpval`. Resolved settings preserve the reader's previously agreed layout and priorities.

- Retain Expert Sourcing and Task Design as reader-chosen labels. Dataset Creation order is Expert Sourcing → Validating the Digital Tasks Measure → Task Design → Example Tasks.
- Quality Control and Model Evaluation each use Human Review, then Auto Judge. Dataset Auto Judge is Model-in-the-Loop Task Review; automated model-output grading belongs in Model Evaluation.
- Quality dimensions are Representativeness, Difficulty, Overall Quality, and Prompt Specificity. Difficulty includes the paper's difficulty scores and completion-time means/medians as workload context. Keep the specificity-assessment sentence visible and its percentage in Source Excerpts.
- Human evaluation topics are Human Expert Grading, Headline Results, Model Strengths and Weaknesses, and Task Duration. Automated Grading contains agreement, limitations, and scoring details.
- Key Findings priority: Speed and Cost Comparison; Increasing Reasoning Effort and Scaffolding; Under-Contextualized GDPval; Time to Complete. Findings specific to individual models are less important.
- Special Design priority: Expert Recruitment and Iterative Review Process; Files and Attachments; Representative Breadth. Reuse concise expert-experience, screening, review-count, and revision evidence under the first topic.
- Header paper link: https://arxiv.org/abs/2510.04374v1. Metadata is OpenAI, Oct 2025; calculate the reading estimate from the current text rather than copying a previous value.
- Headline Results links to https://artificialanalysis.ai/evaluations/gdpval-aa. Keep original paper results dated; Headline Results contains the dated paper comparison and leaderboard link only, with no additional source list, bar-legend explanation, independent-evaluation attribution, or ties note. Keep score definitions in internal provenance. Verify the leaderboard before changing it.
- The selected original example is public task `a328feea-47db-4856-b4be-2bdc63dd88fb`, an Administrative Services Manager absence/lateness policy. Put Example Tasks directly under Dataset Creation, alongside Task Design. Keep only the complete original instruction and the official dataset source with task ID and row/search details. Put the dataset source and lookup details directly after **Example Task:**, before the instruction. Do not embed the expert Word-document text or other example details.
- Source facts, counts, and section titles must still be checked against the PDF/topic map. No GDPval-specific number or topic is a default for future papers.

- Numbered filenames are `summary/315_gdpval.md`, `html/315_gdpval.html`, `summary/315_gdpval_highlights.md`, and `html/315_gdpval_highlights.html`; internal provenance uses `.artifacts/315_gdpval/`.

- Opening Summary keeps separate Purpose, Scope, Task Design, Time and Cost, and Evaluation Method bullets, when source information is available. Impact keeps separate Economic Relevance and Limitations bullets. These labels preserve this paper's edited organization; other papers derive appropriate content from their own sources.
