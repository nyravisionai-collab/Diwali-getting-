#!/usr/bin/env python3
"""Personalise the Diwali 2026 greetings for one recipient — or for a whole list.

    python3 tools/personalize.py --name "રમેશ પટેલ"
    python3 tools/personalize.py --csv names.csv          # one name per line
    python3 tools/personalize.py --name "Ramesh Patel" --skip-cards

Output (never overwrites the generic, write-the-name-yourself files):
    documents/personal/ElectricalSkart-Diwali-{Letter,Email}-{lang}-<name>.{docx,pdf,txt}
    cards/personal/ElectricalSkart-Diwali-Card-{GU,EN,BI}[-Banner]-<name>.jpg
"""
import argparse
import csv
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)


def run(cmd):
    subprocess.run(cmd, check=True)


def read_names(args):
    names = []
    if args.name:
        names.append(args.name.strip())
    if args.csv:
        with open(args.csv, encoding="utf-8-sig") as f:
            for row in csv.reader(f):
                if row and row[0].strip():
                    names.append(row[0].strip())
    # de-duplicate, keep order
    seen, out = set(), []
    for n in names:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def main():
    ap = argparse.ArgumentParser(
        description="Build name-filled letters, e-mails and cards.")
    ap.add_argument("--name", help='one recipient, e.g. --name "રમેશ પટેલ"')
    ap.add_argument("--csv", help="file with one name per line (or first column)")
    ap.add_argument("--skip-cards", action="store_true", help="documents only")
    ap.add_argument("--skip-docs", action="store_true", help="cards only")
    args = ap.parse_args()

    names = read_names(args)
    if not names:
        ap.error("give --name \"…\" or --csv names.csv")

    for i, nm in enumerate(names, 1):
        print(f"\n── [{i}/{len(names)}] {nm} " + "─" * 24)
        if not args.skip_docs:
            run([sys.executable, os.path.join(HERE, "build_documents.py"), "all", "--name", nm])
        if not args.skip_cards:
            run([sys.executable, os.path.join(HERE, "build_cards.py"), "all", "--name", nm])

    print(f"\nપૂર્ણ થયું · Done — {len(names)} recipient(s):")
    if not args.skip_docs:
        print("  documents/personal/")
    if not args.skip_cards:
        print("  cards/personal/")


if __name__ == "__main__":
    main()
