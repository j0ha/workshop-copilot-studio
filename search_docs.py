#!/usr/bin/env python3
"""
Gezielte Stichpunktsuche in der grossen Copilot-Studio-Dokumentations-Markdown-Datei,
ohne die komplette Datei in den Kontext laden zu muessen.

Verwendung:
  # 1) Ueberblick verschaffen: welche Ueberschriften passen zu einem Stichwort?
  python3 search_docs.py headings "Instructions"

  # 2) Freitextsuche mit Kontextzeilen (grep-artig)
  python3 search_docs.py grep "sensitivity label" --context 3

  # 3) Einen ganzen Abschnitt ab einer bestimmten Ueberschrift extrahieren
  #    (von der Zeile bis zur naechsten Ueberschrift gleicher/hoeherer Ebene)
  python3 search_docs.py section 4523

Alle Treffer werden mit Zeilennummern ausgegeben, damit man gezielt mit
`section <zeile>` nachladen kann, statt die ganze Datei zu lesen.
"""

import argparse
import re
import sys
from pathlib import Path

DEFAULT_FILE = Path(__file__).parent / "microsoft-copilot-studio.md"

HEADING_RE = re.compile(r"^(#{1,6})\s*(.*)$")


def load_lines(path: Path) -> list[str]:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()


def cmd_headings(args, lines: list[str]) -> None:
    pattern = re.compile(args.keyword, re.IGNORECASE)
    hits = 0
    for i, line in enumerate(lines, start=1):
        m = HEADING_RE.match(line)
        if not m:
            continue
        text = m.group(2)
        if pattern.search(text):
            hits += 1
            print(f"{i}:\t{line.rstrip()}")
            if args.limit and hits >= args.limit:
                print(f"... (Limit von {args.limit} erreicht, --limit erhoehen fuer mehr)")
                break
    if hits == 0:
        print("Keine Ueberschriften gefunden. Versuche es mit 'grep' fuer Freitextsuche.")


def cmd_grep(args, lines: list[str]) -> None:
    pattern = re.compile(args.keyword, re.IGNORECASE)
    hits = 0
    n = len(lines)
    i = 0
    while i < n:
        if pattern.search(lines[i]):
            hits += 1
            start = max(0, i - args.context)
            end = min(n, i + args.context + 1)
            print(f"--- Treffer bei Zeile {i + 1} ---")
            for j in range(start, end):
                marker = ">>" if j == i else "  "
                print(f"{marker} {j + 1}:\t{lines[j].rstrip()}")
            print()
            if args.limit and hits >= args.limit:
                print(f"... (Limit von {args.limit} Treffern erreicht, --limit erhoehen fuer mehr)")
                break
        i += 1
    if hits == 0:
        print("Keine Treffer gefunden.")


def cmd_section(args, lines: list[str]) -> None:
    start_idx = args.line - 1
    if start_idx < 0 or start_idx >= len(lines):
        print(f"Zeile {args.line} liegt ausserhalb der Datei (1..{len(lines)}).")
        return

    start_match = HEADING_RE.match(lines[start_idx])
    if not start_match:
        print(
            f"Zeile {args.line} ist keine Ueberschrift. "
            f"Inhalt: {lines[start_idx].rstrip()!r}\n"
            f"Nutze zuerst 'headings' oder 'grep', um eine Ueberschriftenzeile zu finden."
        )
        return

    start_level = len(start_match.group(1))
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        m = HEADING_RE.match(lines[j])
        if m and len(m.group(1)) <= start_level:
            end_idx = j
            break

    # Sicherheitsbegrenzung, falls ein Abschnitt ungewoehnlich lang ist
    max_lines = args.max_lines
    if end_idx - start_idx > max_lines:
        end_idx = start_idx + max_lines
        truncated = True
    else:
        truncated = False

    print(f"### Abschnitt Zeilen {start_idx + 1}-{end_idx} ###\n")
    print("".join(lines[start_idx:end_idx]))
    if truncated:
        print(f"\n[... Abschnitt gekuerzt bei {max_lines} Zeilen. --max-lines erhoehen fuer mehr ...]")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE, help="Pfad zur Markdown-Datei")
    sub = parser.add_subparsers(dest="command", required=True)

    p_headings = sub.add_parser("headings", help="Ueberschriften nach Stichwort durchsuchen")
    p_headings.add_argument("keyword", help="Regex/Stichwort (case-insensitive)")
    p_headings.add_argument("--limit", type=int, default=50, help="Max. Anzahl Treffer (0 = unbegrenzt)")
    p_headings.set_defaults(func=cmd_headings)

    p_grep = sub.add_parser("grep", help="Freitextsuche mit Kontextzeilen")
    p_grep.add_argument("keyword", help="Regex/Stichwort (case-insensitive)")
    p_grep.add_argument("--context", type=int, default=3, help="Kontextzeilen vor/nach dem Treffer")
    p_grep.add_argument("--limit", type=int, default=20, help="Max. Anzahl Treffer (0 = unbegrenzt)")
    p_grep.set_defaults(func=cmd_grep)

    p_section = sub.add_parser("section", help="Abschnitt ab Ueberschriftenzeile extrahieren")
    p_section.add_argument("line", type=int, help="Zeilennummer der Ueberschrift (1-indiziert)")
    p_section.add_argument("--max-lines", type=int, default=400, help="Maximale Abschnittslaenge in Zeilen")
    p_section.set_defaults(func=cmd_section)

    args = parser.parse_args()
    if not args.file.exists():
        print(f"Datei nicht gefunden: {args.file}", file=sys.stderr)
        sys.exit(1)

    lines = load_lines(args.file)
    args.func(args, lines)


if __name__ == "__main__":
    main()
