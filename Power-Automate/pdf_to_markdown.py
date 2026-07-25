#!/usr/bin/env python3
"""Convert a PDF file to Markdown using pymupdf4llm.

Converts page-by-page in worker-process batches with a timeout. Some PDFs
contain pathological pages (e.g. deeply nested Form XObjects) that make
pymupdf4llm's text/layout extraction balloon in size and take effectively
forever on a single page. Converting the whole document in one call means a
single such page hangs the entire script forever with no partial output and
no indication of which page is the problem. Here, a batch that times out is
retried page-by-page, any page that still times out is skipped with a note
in the output, and already-converted pages are flushed to disk immediately.
"""

import argparse
import multiprocessing
import pathlib
import time

import pymupdf4llm


def _convert_batch(pdf_path, pages, queue):
    try:
        md = pymupdf4llm.to_markdown(
            str(pdf_path), pages=pages, use_ocr=False, show_progress=False
        )
        queue.put(("ok", md))
    except Exception as exc:  # noqa: BLE001 - report any failure back to parent
        queue.put(("error", str(exc)))


def convert_pages(pdf_path: pathlib.Path, pages: list[int], timeout: float) -> str | None:
    """Convert `pages` (0-based indices) in a subprocess, enforcing `timeout`.

    Returns the markdown text, or None if the subprocess timed out or failed.
    """
    queue: multiprocessing.Queue = multiprocessing.Queue()
    proc = multiprocessing.Process(target=_convert_batch, args=(pdf_path, pages, queue))
    proc.start()
    proc.join(timeout)
    if proc.is_alive():
        proc.terminate()
        proc.join()
        return None
    if not queue.empty():
        status, payload = queue.get()
        if status == "ok":
            return payload
    return None


def convert(
    pdf_path: pathlib.Path,
    output_path: pathlib.Path,
    batch_size: int = 25,
    batch_timeout: float = 90,
    page_timeout: float = 60,
) -> None:
    import pymupdf

    doc = pymupdf.open(str(pdf_path))
    total_pages = doc.page_count
    doc.close()

    skipped = []
    t_start = time.time()

    with output_path.open("w", encoding="utf-8") as out:
        page = 0
        while page < total_pages:
            batch = list(range(page, min(page + batch_size, total_pages)))
            md = convert_pages(pdf_path, batch, batch_timeout)
            if md is not None:
                out.write(md)
                out.flush()
            else:
                print(
                    f"  batch {batch[0] + 1}-{batch[-1] + 1} timed out after "
                    f"{batch_timeout}s, retrying page by page...",
                    flush=True,
                )
                for p in batch:
                    single = convert_pages(pdf_path, [p], page_timeout)
                    if single is not None:
                        out.write(single)
                        out.flush()
                    else:
                        skipped.append(p)
                        out.write(
                            f"\n\n<!-- page {p + 1} skipped: conversion "
                            f"timed out after {page_timeout}s -->\n\n"
                        )
                        out.flush()
                        print(
                            f"  page {p + 1} skipped (timed out after {page_timeout}s)",
                            flush=True,
                        )

            page += batch_size
            done = min(page, total_pages)
            elapsed = time.time() - t_start
            pct = done / total_pages * 100
            print(f"[{pct:5.1f}%] {done}/{total_pages} pages ({elapsed:.0f}s elapsed)", flush=True)

    print(f"Wrote {output_path}")
    if skipped:
        print(f"Skipped {len(skipped)} page(s) that timed out: {[p + 1 for p in skipped]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=pathlib.Path, help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output", type=pathlib.Path, default=None,
        help="Path to the output Markdown file (default: same name as PDF with .md extension)",
    )
    parser.add_argument(
        "--batch-size", type=int, default=25,
        help="Pages to convert per worker batch (default: 25)",
    )
    parser.add_argument(
        "--batch-timeout", type=float, default=90,
        help="Seconds allowed per batch before falling back to page-by-page (default: 90)",
    )
    parser.add_argument(
        "--page-timeout", type=float, default=60,
        help="Seconds allowed per single page before it is skipped (default: 60)",
    )
    args = parser.parse_args()

    output = args.output or args.pdf.with_suffix(".md")
    convert(
        args.pdf, output,
        batch_size=args.batch_size,
        batch_timeout=args.batch_timeout,
        page_timeout=args.page_timeout,
    )
