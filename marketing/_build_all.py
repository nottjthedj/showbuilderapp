#!/usr/bin/env python3
"""One command, whole pipeline, in dependency order.

    brands/gtad.show.json
      -> marketing/shot-sheet.json      the film as <=15s prompts, dialogue included
      -> marketing/shot-list.json       the same clips regrouped by subject
      -> marketing/voice-script.json    every spoken line regrouped by voice
      -> documents/*.md                 the readable script files

Each step reads the step before it, so the script, the prompts and the recording
script cannot disagree with each other. Run it after any change to the show file
or to a builder.
"""
import pathlib, runpy, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STEPS = [
    ("The master prompt sheet", ROOT / 'marketing/_build_shotsheet.py'),
    ("Regrouped by subject", ROOT / 'marketing/_build_shotlists.py'),
    ("Regrouped by voice", ROOT / 'marketing/_build_vo.py'),
    ("The script documents", ROOT / 'documents/_build_documents.py'),
]

for i, (label, path) in enumerate(STEPS, 1):
    print(f"\n[{i}/{len(STEPS)}] {label}  ({path.relative_to(ROOT)})")
    if not path.exists():
        sys.exit(f"missing builder: {path}")
    runpy.run_path(str(path), run_name='__main__')
print("\nDone. Pages are built separately — _build_sheet_page.py, _build_shotlist_pages.py, "
      "_build_vo_page.py.")
