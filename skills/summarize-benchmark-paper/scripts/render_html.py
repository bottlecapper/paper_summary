#!/usr/bin/env python3
"""Render a Markdown document as a standalone, offline HTML reading page."""
import argparse
import html
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit
from xml.etree import ElementTree

import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.util import AtomicString


class VerbatimProcessor(InlineProcessor):
    def handleMatch(self, match, data):
        element = ElementTree.Element("span", {"class": "verbatim"})
        # Keep copied text literal, including any Markdown syntax or HTML in it.
        element.text = AtomicString(html.unescape(match.group(1)))
        return element, match.start(0), match.end(0)


class VerbatimExtension(Extension):
    def extendMarkdown(self, md):
        pattern = r'&lt;span class="verbatim"&gt;(.*?)&lt;/span&gt;'
        # Process after code spans but before Markdown escapes/emphasis/links.
        md.inlinePatterns.register(VerbatimProcessor(pattern, md), "verbatim", 185)


def protect_verbatim_blocks(source):
    """Keep original code tabs/spaces intact while Markdown parses surrounding lists."""
    lines = source.splitlines(keepends=True)
    output, blocks = [], []
    index = 0
    while index < len(lines):
        marker = re.fullmatch(r"( {4,})verbatim\s*", lines[index].rstrip("\r\n"))
        if marker is None:
            output.append(lines[index])
            index += 1
            continue
        indent = marker.group(1)
        index += 1
        original = []
        while index < len(lines):
            line = lines[index]
            if line.strip() and not line.startswith(indent):
                break
            original.append(line[len(indent):] if line.startswith(indent) else line)
            index += 1
        code = "".join(original).rstrip("\r\n") + "\n"
        output.append(indent + "CODEX_VERBATIM_BLOCK_{}\n\n".format(len(blocks)))
        blocks.append(code)
    return "".join(output), blocks


def rebase_local_links(body, source_path, output_path):
    """Keep relative document links valid when HTML lives in another folder."""
    root = ElementTree.fromstring("<div>" + body + "</div>")
    changed = False
    for anchor in root.iter("a"):
        href = anchor.get("href", "")
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
            continue
        target = source_path.resolve().parent / unquote(parts.path)
        relative = os.path.relpath(str(target), str(output_path.resolve().parent))
        rewritten = urlunsplit(("", "", quote(relative, safe="/"), parts.query, parts.fragment))
        if rewritten != href:
            anchor.set("href", rewritten)
            changed = True
    if not changed:
        return body
    return "".join(ElementTree.tostring(child, encoding="unicode", method="html") for child in root)


def collapse_source_lists(body):
    """Keep nested source bullets available beneath a short, readable overview."""
    root = ElementTree.fromstring("<div>" + body + "</div>")
    keep_section_visible = False
    collapsed_items = set()
    for block in root:
        if block.tag == "h2":
            keep_section_visible = "".join(block.itertext()).strip() in ("Summary", "Important Sections")
        if keep_section_visible:
            continue
        for item in list(block.iter("li")):
            # Preserve the logical bullet hierarchy inside a source excerpt.
            if item in collapsed_items:
                continue
            # Category children are overview content, rather than source excerpts.
            lead = item.find("p")
            label = (lead if lead is not None else item).find("strong")
            if label is not None:
                label_text = "".join(label.itertext()).rstrip(":")
                if label_text in ("Review Approach", "Quality Dimensions"):
                    continue
                # A heading-only category introduces visible design elements.
                # A complete design sentence may instead have source excerpts.
                if label_text == "Task Design":
                    lead_text = item.text or ""
                    for part in item:
                        if part.tag in ("ul", "ol", "details"):
                            break
                        lead_text += "".join(part.itertext()) + (part.tail or "")
                    if lead_text.strip().rstrip(":") == label_text:
                        continue
            for child in list(item):
                if child.tag not in ("ul", "ol"):
                    continue
                position = list(item).index(child)
                item.remove(child)
                details = ElementTree.Element("details", {"class": "source-excerpts"})
                details.tail, child.tail = child.tail, None
                ElementTree.SubElement(details, "summary").text = "Source Excerpts"
                details.append(child)
                item.insert(position, details)
                collapsed_items.update(child.iter("li"))
    return "".join(ElementTree.tostring(child, encoding="unicode", method="html") for child in root)


STYLE = """
:root {color-scheme:light; --paper:#fff; --bg:#f3f5f2; --ink:#21312c; --muted:#5b6e65; --line:#dce4de; --accent:#24634b}
* {box-sizing:border-box} body {margin:0;background:var(--bg);color:var(--ink);font:17px/1.7 system-ui,-apple-system,sans-serif}
.layout {max-width:1280px;margin:auto;display:grid;grid-template-columns:235px minmax(0,1fr);gap:32px;padding:36px 24px}
aside {align-self:start;position:sticky;top:24px;max-height:90vh;overflow:auto;font-size:13px}
.brand {font-weight:750;letter-spacing:.08em;text-transform:uppercase;margin-bottom:24px;color:var(--accent)}
.toc ul {padding-left:17px}.toc li {margin:8px 0}.toc a {color:var(--muted);text-decoration:none}
main {background:var(--paper);border:1px solid var(--line);border-radius:18px;padding:40px 48px;min-width:0}
h1 {font-size:clamp(26px,3.5vw,40px);line-height:1.2;letter-spacing:-.035em;margin-top:0}
h2 {font-size:25px;line-height:1.25;margin:28px 0 2px;padding:0} h3 {font-size:19px;line-height:1.3;margin:16px 0 2px;padding:0}
h4 {font-size:17px;line-height:1.3;margin:10px 0 2px;padding:0}
main > p, main > ul, main > ol {margin-top:0;margin-bottom:0}
main li > p {margin-top:0;margin-bottom:0}
main ul {list-style-type:disc;padding-left:1.5em}
main ul ul {list-style-type:circle;margin-top:0;margin-bottom:0}
p,li {max-width:78ch} a {color:var(--accent);text-underline-offset:3px} strong {font-weight:700}
.verbatim {color:#175cd3}
.task-instruction {font-size:0.88em;text-align:justify}
.source-excerpts {margin:0}.source-excerpts > summary {font-size:13px;color:var(--muted);cursor:pointer}
.source-excerpts ul, .source-excerpts ol {margin-top:0;margin-bottom:0}
blockquote {margin:24px 0;border-left:4px solid #8eb79b;padding:12px 20px;background:#f0f6f0}
table {width:100%;border-collapse:collapse;font-size:14px;display:block;overflow-x:auto} th,td {text-align:left;vertical-align:top;padding:12px 14px;border-bottom:1px solid var(--line)} th {background:#edf3ee}
code {background:#eef2ed;border-radius:4px;padding:2px 5px;font-size:.9em} pre {overflow:auto;padding:16px;background:#eef2ed;border-radius:8px} pre code {padding:0}
button {font:inherit;font-size:13px;border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:7px;padding:8px 12px;cursor:pointer}
.color-swatch {display:inline-block;width:14px;height:14px;vertical-align:-2px;border:1px solid #9ba99f;border-radius:3px;margin-right:5px}
.tools {display:flex;gap:8px;flex-wrap:wrap;margin-top:24px}.footer {margin-top:40px;font-size:12px;color:var(--muted)}
@media(max-width:850px) {.layout {display:block;padding:16px} aside {position:static;max-height:none;margin-bottom:20px}.toc {display:none}main {padding:26px 22px}.tools {margin:8px 0}}
@media print {body {background:white;font-size:11pt}.layout {display:block;padding:0}aside {display:none}main {border:0;padding:0}h2 {break-after:avoid}a {color:inherit}table {display:table;font-size:10pt}}
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--collapse-source-excerpts", action="store_true",
                        help="Place nested source bullets in expandable details below each lead bullet")
    args = parser.parse_args()
    source = args.markdown_file.read_text(encoding="utf-8")
    # YAML skill frontmatter is metadata, not visible prose.
    if source.startswith("---\n") and "\n---\n" in source[4:]:
        source = source.split("\n---\n", 1)[1]
    title = next((line[2:].strip() for line in source.splitlines() if line.startswith("# ")), args.markdown_file.stem)
    converter = markdown.Markdown(extensions=[VerbatimExtension(), "tables", "fenced_code", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-3"}})
    # Escape raw HTML so document content cannot execute scripts.
    prepared, original_code = protect_verbatim_blocks(source)
    body = converter.convert(html.escape(prepared, quote=False))
    # Markdown escapes code text again; restore one layer while keeping it inert.
    body = re.sub(r'(<code(?: [^>]*)?>)(.*?)(</code>)',
                  lambda m: m.group(1) + html.escape(html.unescape(html.unescape(m.group(2))), quote=False) + m.group(3),
                  body, flags=re.S)
    body = re.sub(r'<pre><code>CODEX_VERBATIM_BLOCK_(\d+)\s*</code></pre>',
                  lambda m: '<pre><code class="verbatim">' +
                  html.escape(original_code[int(m.group(1))], quote=False) + '</code></pre>', body)
    body = re.sub(r"<code>(#[0-9A-Fa-f]{6})</code>", lambda m: '<span class="color-swatch" aria-hidden="true" style="background:{}"></span>{}'.format(m.group(1), m.group(0)), body)
    body = rebase_local_links(body, args.markdown_file, args.output)
    body = body.replace('<p>The task instruction is: <em>',
                        '<p class="task-instruction">The task instruction is: <em>')
    if args.collapse_source_excerpts:
        body = collapse_source_lists(body)
    source_control = '<button id="sources">Show Source Excerpts</button>' if args.collapse_source_excerpts else ""
    document = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{style}</style></head><body>
<div class="layout"><aside><div class="brand">Paper summary</div><nav aria-label="Contents">{toc}</nav>
<div class="tools"><button onclick="window.print()">Print / save PDF</button><button id="expand">Show contents</button>{source_control}</div>
</aside><main>{body}<div class="footer">Source Markdown: {filename} · Standalone HTML · Works offline</div></main></div>
<script>document.getElementById('expand').addEventListener('click',function(){{const t=document.querySelector('.toc');if(t){{t.style.display=t.style.display==='block'?'':'block';}}}});
const sourceButton=document.getElementById('sources');if(sourceButton){{sourceButton.addEventListener('click',function(){{const excerpts=Array.from(document.querySelectorAll('details.source-excerpts'));const show=excerpts.some(d=>!d.open);excerpts.forEach(d=>d.open=show);sourceButton.textContent=show?'Hide Source Excerpts':'Show Source Excerpts';}});}}</script>
</body></html>""".format(title=html.escape(title), style=STYLE, toc=converter.toc, body=body, filename=html.escape(args.markdown_file.name), source_control=source_control)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(document, encoding="utf-8")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
