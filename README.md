# Paper Summaries

## Existing Paper Summaries

| Benchmark Name | Author Company / Institution | Published Month | Paper Link | Summary Link | HTML Link |
| --- | --- | --- | --- | --- | --- |
| DeepSWE | Datacurve | Jul 2026 | [Paper](https://arxiv.org/abs/2607.07946v1) | [Markdown](summary/312_deepswe.md) | [HTML](html/312_deepswe.html) |
| AutomationBench | Zapier | Apr 2026 | [Paper](https://arxiv.org/abs/2604.18934) | [Markdown](summary/313_automationbench.md) | [HTML](html/313_automationbench.html) |
| Terminal-Bench 2.0 | Stanford University, Laude Institute | Jan 2026 | [Paper](https://arxiv.org/abs/2601.11868) | [Markdown](summary/314_terminal_bench.md) | [HTML](html/314_terminal_bench.html) |
| GDPval | OpenAI | Oct 2025 | [Paper](https://arxiv.org/abs/2510.04374v1) | [Markdown](summary/315_gdpval.md) | [HTML](html/315_gdpval.html) |
| OSWorld 2.0 | XLANG Lab | Jun 2026 | [Paper](https://arxiv.org/abs/2606.29537v2) | [Markdown](summary/316_osworld_2_0.md) | [HTML](html/316_osworld_2_0.html) |

Published month refers to the paper's first arXiv submission. Paper links point to the versions used by the summaries, where specified.

Additional GDPval materials: [regenerated summary](summary/315_gdpval_regenerated.md), [regenerated HTML](html/315_gdpval_regenerated.html), [highlight audit](summary/315_gdpval_regenerated_highlights.md), and [skill reproduction review](summary/315_gdpval_reproduction_review.md).

Read the Markdown summaries directly on GitHub. To view the formatted HTML, download or clone the repository and open an HTML file in a browser.

## Use This Repository with Codex in VS Code

### 1. Open the Project

Install the official Codex extension in VS Code and sign in, following the [OpenAI IDE setup guide](https://learn.chatgpt.com/docs/codex/ide). Clone this private repository using a GitHub account with access:

```bash
git clone https://github.com/bottlecapper/paper_summary.git
cd paper_summary
code .
```

If the `code` command is unavailable, use **File → Open Folder** in VS Code and select `paper_summary`. Open Codex from its sidebar icon or run **Codex: Open Codex Sidebar** in the Command Palette.

### 2. Prepare an Annotated Paper

Save your highlighted benchmark-paper PDF locally, for example at `.artifacts/input/317_new_benchmark.pdf`. Create the folders if needed. Source PDFs and working artifacts are excluded from Git and are not included when cloning this repository.

Review [highlight_preferences.json](highlight_preferences.json) for highlight-color priorities, formatting, and paper-specific overrides. The defaults prioritize cyan, bright green, and light green; yellow marks questions and is excluded from the summary.

### 3. Ask Codex to Create a Summary

Start a chat in Codex with the repository open and paste the following prompt, replacing the PDF path and paper slug:

```text
Read and follow skills/summarize-benchmark-paper/SKILL.md.
Use highlight_preferences.json and only the overrides for this paper.
Summarize the annotated benchmark paper at
.artifacts/input/317_new_benchmark.pdf using slug 317_new_benchmark.
If needed, create a Python environment under .dependencies/ and install
skills/summarize-benchmark-paper/scripts/requirements.txt there.
Preserve the source PDF. Save the summary in summary/317_new_benchmark.md,
its matching HTML in html/317_new_benchmark.html, and companion highlight
audits in summary/ and html/. Keep internal provenance in
.artifacts/317_new_benchmark/. Check highlight coverage and Markdown/HTML
consistency, then add this paper to the README table.
```

The prompt explicitly loads the skill from its current location. For automatic skill discovery, Codex uses `.agents/skills/`; see the [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

### 4. Review and Refine

Preview the Markdown in VS Code and open the generated HTML in a browser. Check the overview, expandable source excerpts, and highlight audit. Continue in the same Codex chat with specific revisions, for example:

```text
Revise summary/317_new_benchmark.md to make the dataset quality checks
clearer. Follow the benchmark skill, verify the edits against the source
PDF, update the highlight audit, and regenerate the matching HTML.
```

Review the Git diff in VS Code's Source Control view before committing and pushing the summary, HTML, audits, and README update.

## About This Repository

This repository collects concise summaries of AI benchmark papers and a reusable workflow for turning annotated PDFs into searchable Markdown and standalone HTML. The summaries focus on how benchmarks are built, how their quality is checked, how models are evaluated, and what the findings mean.

The workflow follows the reader's highlight priorities and keeps source evidence alongside the overview. HTML summaries distinguish verified original wording in blue and provide expandable source excerpts. Companion highlight audits document how included annotations are covered by the summary.

## Repository Contents

| Path | Purpose |
| --- | --- |
| [summary/](summary/) | Paper summaries, highlight audits, and the GDPval reproduction review. |
| [html/](html/) | Standalone HTML versions of summaries, audits, and reference documents. |
| [skills/summarize-benchmark-paper/](skills/summarize-benchmark-paper/) | Reusable summarization instructions, default preferences, topic guidance, and Python scripts. |
| [highlight_preferences.json](highlight_preferences.json) | Project preferences for highlight colors, summary structure, formatting, and paper-specific overrides. |
| [paper_profiles/](paper_profiles/) | Paper-specific editorial choices, including the GDPval profile. |
| [examples/](examples/) | Selected benchmark task requests and supporting artifacts, such as reference solutions, environment setup, and an expert deliverable. |

## Summarization Workflow

The [benchmark summarization skill](skills/summarize-benchmark-paper/SKILL.md) documents the full process:

1. Resolve the project preferences and any paper-specific overrides.
2. Extract the annotated PDF and account for the included highlights.
3. Write a concise summary with source support, then audit highlight coverage.
4. Render the Markdown to HTML and check that the two versions match.

The Python dependencies are listed in [requirements.txt](skills/summarize-benchmark-paper/scripts/requirements.txt). For example, from the repository root, render and check an existing summary with:

```bash
python3 skills/summarize-benchmark-paper/scripts/render_html.py \
  summary/312_deepswe.md \
  --output html/312_deepswe.html \
  --collapse-source-excerpts

python3 skills/summarize-benchmark-paper/scripts/check_summary.py \
  summary/312_deepswe.md \
  --html html/312_deepswe.html
```

Markdown is the source of truth for its paired HTML. Cached PDFs, internal working artifacts, local dependencies, and Python caches are excluded from version control.
