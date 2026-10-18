#!/usr/bin/env python3
"""Resolve shared reader defaults and only the requested paper's overrides."""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import re


def merge(base, overrides):
    result = deepcopy(base)
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


def resolve(paper_slug, project=None):
    if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", paper_slug):
        raise ValueError("Use a snake_case paper slug.")
    defaults = Path(__file__).resolve().parents[1] / "assets/default_preferences.json"
    settings = json.loads(defaults.read_text(encoding="utf-8"))
    project = project or {}
    shared = {key: value for key, value in project.items() if key != "paper_overrides"}
    settings = merge(settings, shared)
    selected = project.get("paper_overrides", {}).get(paper_slug, {})
    settings = merge(settings, selected)
    settings.pop("paper_overrides", None)
    settings["resolved_paper_slug"] = paper_slug
    return settings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-slug", required=True)
    parser.add_argument("--preferences", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    project = (json.loads(args.preferences.read_text(encoding="utf-8"))
               if args.preferences else {})
    settings = resolve(args.paper_slug, project)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(settings, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
