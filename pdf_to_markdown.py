#!/usr/bin/env python3
"""Convert a PDF file to Markdown using pymupdf4llm."""

import argparse
import pathlib

import pymupdf4llm


def convert(pdf_path: pathlib.Path, output_path: pathlib.Path) -> None:
    md_text = pymupdf4llm.to_markdown(str(pdf_path), use_ocr=False, show_progress=True)
    output_path.write_text(md_text, encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=pathlib.Path, help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output", type=pathlib.Path, default=None,
        help="Path to the output Markdown file (default: same name as PDF with .md extension)",
    )
    args = parser.parse_args()

    output = args.output or args.pdf.with_suffix(".md")
    convert(args.pdf, output)
