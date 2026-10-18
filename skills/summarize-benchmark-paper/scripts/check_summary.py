#!/usr/bin/env python3
"""Check paired HTML freshness and measure the actual visible overview."""
import argparse
from html.parser import HTMLParser
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import tempfile


class ReadingText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.in_footer = False
        self.hidden_details = []
        self.visible = []
        self.full = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "main":
            self.in_main = True
            self.in_footer = False
        if tag == "details":
            self.hidden_details.append("open" not in attrs)
        if tag == "div" and attrs.get("class") == "footer":
            self.in_footer = True

    def handle_endtag(self, tag):
        if tag == "details":
            self.hidden_details.pop()
        if tag == "main":
            self.in_main = False

    def handle_data(self, data):
        if self.in_main and not self.in_footer:
            self.full.append(data)
            if not any(self.hidden_details):
                self.visible.append(data)


def word_count(parts):
    return len(re.findall(r"\b[\w’−]+\b", " ".join(parts)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--words-per-minute", type=int, default=200)
    parser.add_argument("--max-words", type=int, default=900)
    parser.add_argument("--max-minutes", type=float, default=5)
    args = parser.parse_args()
    if min(args.words_per_minute, args.max_words, args.max_minutes) <= 0:
        parser.error("Reading rate and limits must be positive.")
    source = args.markdown_file.read_text(encoding="utf-8")
    actual = args.html.read_bytes()
    renderer = Path(__file__).with_name("render_html.py")
    with tempfile.TemporaryDirectory(prefix="paper_summary_check_") as folder:
        fresh = Path(folder) / "summary.html"
        subprocess.run([sys.executable, str(renderer), str(args.markdown_file),
                        "--output", str(fresh), "--collapse-source-excerpts"],
                       check=True, stdout=subprocess.PIPE)
        matches = actual == fresh.read_bytes()
    reader = ReadingText()
    reader.feed(actual.decode("utf-8"))
    overview_words = word_count(reader.visible)
    full_words = word_count(reader.full)
    minutes = overview_words / args.words_per_minute
    expected_label = max(1, math.ceil(minutes))
    label_match = re.search(r"~(\d+)-minute (?:overview|read)", source)
    issues = []
    if not matches:
        issues.append("HTML differs from a fresh rendering of the Markdown.")
    if overview_words > args.max_words or minutes > args.max_minutes:
        issues.append("Visible overview exceeds the requested reading limit.")
    if label_match and int(label_match.group(1)) != expected_label:
        issues.append("Reading label should be approximately {} minutes at {} words/minute."
                      .format(expected_label, args.words_per_minute))
    print(json.dumps({"html_matches_markdown": matches,
                      "overview_words": overview_words,
                      "full_words": full_words,
                      "assumed_words_per_minute": args.words_per_minute,
                      "overview_minutes": round(minutes, 2),
                      "suggested_label_minutes": expected_label,
                      "issues": issues}, indent=2))
    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
