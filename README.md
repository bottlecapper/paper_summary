# Paper Summaries

## Existing Paper Summaries

| Paper | Summary | HTML | Highlight Audit |
| --- | --- | --- | --- |
| DeepSWE | [Read summary](summary/312_deepswe.md) | [HTML](html/312_deepswe.html) | [Audit](summary/312_deepswe_highlights.md) |
| AutomationBench | [Read summary](summary/313_automationbench.md) | [HTML](html/313_automationbench.html) | [Audit](summary/313_automationbench_highlights.md) |
| Terminal-Bench 2.0 | [Read summary](summary/314_terminal_bench.md) | [HTML](html/314_terminal_bench.html) | [Audit](summary/314_terminal_bench_highlights.md) |
| GDPval | [Read summary](summary/315_gdpval.md) | [HTML](html/315_gdpval.html) | [Audit](summary/315_gdpval_highlights.md) |
| OSWorld 2.0 | [Read summary](summary/316_osworld_2_0.md) | [HTML](html/316_osworld_2_0.html) | [Audit](summary/316_osworld_2_0_highlights.md) |

Additional GDPval materials: [regenerated summary](summary/315_gdpval_regenerated.md), [regenerated HTML](html/315_gdpval_regenerated.html), [highlight audit](summary/315_gdpval_regenerated_highlights.md), and [skill reproduction review](summary/315_gdpval_reproduction_review.md).

Read the Markdown summaries directly on GitHub. To view the formatted HTML, download or clone the repository and open an HTML file in a browser.

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
