# Paper Summaries

## Existing Paper Summaries

<table>
<thead>
<tr><th rowspan="2">Benchmark</th><th colspan="2">Size</th><th rowspan="2">Author Lab</th><th rowspan="2">Published</th><th rowspan="2">Paper</th><th colspan="2" rowspan="2">Summary</th></tr>
<tr><th>Public</th><th>Private</th></tr>
</thead>
<tbody>
<tr><td>DeepSWE</td><td>113</td><td>—</td><td>Datacurve</td><td>Jul 2026</td><td><a href="https://arxiv.org/abs/2607.07946v1">312</a></td><td><a href="summary/312_deepswe.md">MD</a></td><td><a href="https://bottlecapper.github.io/paper_summary/html/312_deepswe.html">HTML</a></td></tr>
<tr><td>AutomationBench</td><td>600</td><td>600+</td><td>Zapier</td><td>Apr 2026</td><td><a href="https://arxiv.org/abs/2604.18934">313</a></td><td><a href="summary/313_automationbench.md">MD</a></td><td><a href="https://bottlecapper.github.io/paper_summary/html/313_automationbench.html">HTML</a></td></tr>
<tr><td>Terminal-Bench 2.0</td><td>89</td><td>—</td><td>Stanford, Laude Institute</td><td>Jan 2026</td><td><a href="https://arxiv.org/abs/2601.11868">314</a></td><td><a href="summary/314_terminal_bench.md">MD</a></td><td><a href="https://bottlecapper.github.io/paper_summary/html/314_terminal_bench.html">HTML</a></td></tr>
<tr><td>GDPval</td><td>220</td><td>1,100</td><td>OpenAI</td><td>Oct 2025</td><td><a href="https://arxiv.org/abs/2510.04374v1">315</a></td><td><a href="summary/315_gdpval.md">MD</a></td><td><a href="https://bottlecapper.github.io/paper_summary/html/315_gdpval.html">HTML</a></td></tr>
<tr><td>OSWorld 2.0</td><td>108</td><td>—</td><td>XLANG Lab</td><td>Jun 2026</td><td><a href="https://arxiv.org/abs/2606.29537v2">316</a></td><td><a href="summary/316_osworld_2_0.md">MD</a></td><td><a href="https://bottlecapper.github.io/paper_summary/html/316_osworld_2_0.html">HTML</a></td></tr>
<tr><td>FrontierSWE v2</td><td>34</td><td>—</td><td>Proximal</td><td>Sep 2026</td><td><a href="https://www.frontierswe.com/blog/v2">317</a></td><td><a href="summary/317_frontierswe.md">MD</a></td><td><a href="https://bottlecapper.github.io/paper_summary/html/317_frontierswe.html">HTML</a></td></tr>
</tbody>
</table>

Published month refers to the first arXiv submission or, for blog reports, the linked report's release. Paper links point to the versions used by the summaries, where specified.

Size counts tasks in the linked release. Public includes released task sets, including OSWorld 2.0's [gated task files](https://huggingface.co/datasets/xlangai/osworld_v2_tasks); — means no separate private split is reported. [AutomationBench](https://arxiv.org/html/2604.18934v1#S2) reports 600 public and 600+ private evaluation tasks. GDPval's private count is derived: [1,320 total](https://arxiv.org/html/2510.04374v1#S1) − [220 public gold tasks](https://arxiv.org/html/2510.04374v1#S4) = 1,100.

Additional GDPval materials: [regenerated summary](summary/315_gdpval_regenerated.md), [regenerated HTML](https://bottlecapper.github.io/paper_summary/html/315_gdpval_regenerated.html), [highlight audit](summary/315_gdpval_regenerated_highlights.md), and [skill reproduction review](summary/315_gdpval_reproduction_review.md).

Read the Markdown summaries directly on GitHub, or visit the [summary website](https://bottlecapper.github.io/paper_summary/) for formatted HTML. The HTML links above open rendered web pages. Standalone files in [html/](html/) can also be opened locally after downloading or cloning the repository.

## Use This Repository with Codex in VS Code

### 1. Open the Project

Install the official Codex extension in VS Code and sign in, following the [OpenAI IDE setup guide](https://learn.chatgpt.com/docs/codex/ide). Clone this repository:

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

Start a chat in Codex with the repository open and paste this prompt, replacing the PDF path:

```text
Summarize .artifacts/input/317_new_benchmark.pdf following
skills/summarize-benchmark-paper/SKILL.md and this repo's preferences.
Update the README and website.
```

### 4. Review and Refine

Preview the Markdown in VS Code and open the generated HTML in a browser. Check the overview, expandable source excerpts, and highlight audit. Continue in the same Codex chat with specific revisions, for example:

```text
Revise summary/317_new_benchmark.md to make the dataset quality checks
clearer. Follow the benchmark skill, verify the edits against the source
PDF, update the highlight audit, and regenerate the matching HTML.
Run python3 scripts/build_pages.py to refresh docs/ too.
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
| [docs/](docs/) | Generated summary website published through GitHub Pages. |
| [scripts/build_pages.py](scripts/build_pages.py) | Rebuilds the website from the README index and summary HTML. |
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

## Publishing the Website

GitHub Pages serves [the summary website](https://bottlecapper.github.io/paper_summary/) from `docs/` on the `main` branch. After updating summaries or the README table, rebuild the site from the repository root:

```bash
python3 scripts/build_pages.py
```

Review and commit the updated source files together with `docs/`, then push to `main`. GitHub Pages automatically publishes the committed `docs/` contents. Edit the originals in `html/` or the README table rather than editing generated files in `docs/`.
