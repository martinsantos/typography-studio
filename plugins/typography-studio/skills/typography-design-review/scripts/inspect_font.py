#!/usr/bin/env python3
"""Report metadata and coverage without altering a supplied font."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from font_evidence import inspect, read_corpus, write_new, TTLibError


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("font", type=Path)
    parser.add_argument("--corpus", type=Path, default=Path(__file__).resolve().parents[1] / "assets/corpus.json")
    parser.add_argument("--output", type=Path, help="New JSON file; otherwise writes to stdout.")
    args = parser.parse_args()
    try:
        result = json.dumps(inspect(args.font, read_corpus(args.corpus)), ensure_ascii=False, indent=2) + "\n"
        if args.output:
            write_new(args.output, result)
            print(f"Metadata written to {args.output}. No visual approval was performed.")
        else:
            print(result, end="")
    except (OSError, ValueError, TTLibError, ImportError) as exc:
        parser.exit(1, f"Inspection failed: {exc}\n")


if __name__ == "__main__":
    main()
