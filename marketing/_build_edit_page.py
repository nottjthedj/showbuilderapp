#!/usr/bin/env python3
"""The assembly page — the cut order, the running clock, the music cues."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / 'marketing'
SRC = json.load(open(HERE / 'edit-list.json'))
OUT = HERE / 'assembly.html'
OUT.write_text((HERE / '_edit_template.html').read_text()
               .replace('/*__DATA__*/null', json.dumps(SRC, ensure_ascii=False)))
print(f'{OUT.name} | {SRC["meta"]["clips"]} cuts | {SRC["meta"]["runtimeText"]} | '
      f'{round(OUT.stat().st_size/1024)} KB')
