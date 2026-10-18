#!/usr/bin/env python3
"""Build a standalone GitHub Pages site from the README index and summary HTML."""

import argparse
from html import escape
from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]


def link_target(cell):
    match = re.search(r"\[[^\]]+\]\(([^)]+)\)", cell)
    if match is None:
        raise ValueError(f"Expected a Markdown link in {cell!r}")
    return match.group(1)


def anchor(url, label):
    return f'<a href="{escape(url, quote=True)}">{escape(label)}</a>'


def build(output):
    readme = (ROOT / "README.md").read_text()
    table = readme.split("## Existing Paper Summaries\n\n", 1)[1].split("\n\n", 1)[0]
    rows = []
    files = set()
    for line in table.splitlines()[2:]:
        benchmark, author, published, paper, summary = (
            cell.strip() for cell in line.strip().strip("|").split("|")
        )
        markdown_path = Path(link_target(summary))
        if markdown_path.parent != Path("summary") or markdown_path.suffix != ".md":
            raise ValueError(f"Expected a Markdown summary path: {markdown_path}")
        summary_path = Path("html") / markdown_path.with_suffix(".html").name
        files.add(summary_path)
        audit_path = summary_path.with_stem(summary_path.stem + "_highlights")
        audit = ""
        if (ROOT / audit_path).is_file():
            files.add(audit_path)
            audit = anchor(audit_path.as_posix(), "Audit")
        institutions = "<br>".join(escape(part.strip()) for part in re.split(r"<br\s*/?>", author, flags=re.IGNORECASE))
        cells = [escape(benchmark), institutions, escape(published),
                 anchor(link_target(paper), re.search(r"\[([^\]]+)\]", paper).group(1)),
                 anchor(summary_path.as_posix(), "Read summary"), audit]
        rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in cells) + "</tr>")

    extras = [
        ("315_gdpval_regenerated.html", "Regenerated summary"),
        ("315_gdpval_regenerated_highlights.html", "Highlight audit"),
    ]
    extra_links = []
    for filename, label in extras:
        path = Path("html") / filename
        if (ROOT / path).is_file():
            files.add(path)
            extra_links.append(anchor(path.as_posix(), label))

    for path in files:
        if not (ROOT / path).is_file():
            raise FileNotFoundError(ROOT / path)
        destination = output / path
        if destination.resolve() == (ROOT / path).resolve():
            raise ValueError("Output directory must be separate from the source repository")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, destination)

    page = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Paper Summaries</title>
  <meta name="description" content="Summaries and highlight audits of AI benchmark papers.">
  <style>
    :root { color-scheme: light dark; font-family: system-ui, sans-serif; }
    body { max-width: 1120px; margin: 0 auto; padding: 48px 24px; line-height: 1.6; }
    h1 { line-height: 1.2; margin-bottom: 12px; }
    a { color: light-dark(#175cd3, #93baff); text-underline-offset: 3px; }
    a:hover { text-decoration-thickness: 2px; }
    .table-scroll { overflow-x: auto; margin: 28px 0; }
    table { width: 100%; border-collapse: collapse; text-align: left; }
    th, td { padding: 14px 16px; border-bottom: 1px solid light-dark(#dde2ea, #444); }
    th { background: light-dark(#f3f5f9, #24272d); }
    td:first-child { font-weight: 600; }
    td:nth-child(n+3) { white-space: nowrap; }
    .note { color: light-dark(#596579, #b4bfce); font-size: .9rem; }
    h2 { margin-top: 36px; font-size: 1.3rem; }
  </style>
</head>
<body>
  <main>
    <h1>Paper Summaries</h1>
    <p>Concise summaries of AI benchmark papers, with source excerpts and highlight audits.</p>
    <div class="table-scroll">
      <table>
        <thead><tr><th>Benchmark</th><th>Author Lab</th><th>Published</th><th>Paper</th><th>Summary</th><th>Highlights</th></tr></thead>
        <tbody>__ROWS__</tbody>
      </table>
    </div>
    <p class="note">Published month refers to the paper's first arXiv submission. Links retain the versions used by the summaries where specified.</p>
    <h2>Additional GDPval Materials</h2>
    <p>__EXTRAS__</p>
    <p class="note">In the summaries, blue text marks verified original wording. Expand Source Excerpts to read supporting details.</p>
  </main>
</body>
</html>
"""
    page = page.replace("__ROWS__", "\n".join(rows)).replace("__EXTRAS__", " · ".join(extra_links))
    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(page)
    (output / ".nojekyll").write_text("")
    print(f"Built {len(rows)} benchmark entries and {len(files)} HTML documents at {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "docs")
    args = parser.parse_args()
    build(args.output.resolve())
