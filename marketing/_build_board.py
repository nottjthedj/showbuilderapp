#!/usr/bin/env python3
"""Build the transmission board — the 30 daily posts as a working content calendar."""
import json, pathlib

SRC = json.load(open('/home/user/showbuilderapp/marketing/daily-transmissions.json'))
OUT = pathlib.Path('/tmp/claude-0/-home-user-showbuilderapp/'
                   '5c527e80-cd5a-5785-b004-d3c65c699ec9/scratchpad/transmission-board.html')

DATA = json.dumps({
    'posts': SRC['posts'],
    'format': SRC['format'],
    'share': SRC['shareEngine'],
    'formats': SRC['formats'],
    'tour': SRC['tourCadence'],
}, ensure_ascii=False)

HTML = pathlib.Path(__file__).with_name('board_template.html').read_text()
OUT.write_text(HTML.replace('/*__DATA__*/null', DATA))

rt = [p['runtimeSec'] for p in SRC['posts']]
print(f'wrote {OUT}')
print(f"posts {len(SRC['posts'])} | runtime {min(rt)}–{max(rt)}s | triggers {len(SRC['shareEngine']['mechanisms'])}")
