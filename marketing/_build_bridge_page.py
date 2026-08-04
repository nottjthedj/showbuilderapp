#!/usr/bin/env python3
"""The bridges page — free fixes, the element library, textures, and the join list."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / 'marketing'
SRC = json.load(open(HERE / 'bridge-shots.json'))
OUT = HERE / 'bridges.html'
OUT.write_text((HERE / '_bridge_template.html').read_text()
               .replace('/*__DATA__*/null', json.dumps(SRC, ensure_ascii=False)))
print(f"{OUT.name} | {SRC['meta']['elements']} elements + {SRC['meta']['textures']} textures | "
      f"{round(OUT.stat().st_size/1024)} KB")
