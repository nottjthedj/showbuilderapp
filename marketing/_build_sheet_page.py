#!/usr/bin/env python3
import json, pathlib
SRC = json.load(open('/home/user/showbuilderapp/marketing/shot-sheet.json'))
HERE = pathlib.Path(__file__).parent
DATA = json.dumps({
    'meta': SRC['meta'], 'theFix': SRC['theFix'], 'rules': SRC['rules'],
    'blocks': SRC['blocks'], 'clips': SRC['clips'],
    'strip': (HERE/'snap.b64').read_text().strip(),
}, ensure_ascii=False)
out = HERE/'shot-sheet.html'
out.write_text((HERE/'_sheet_template.html').read_text().replace('/*__DATA__*/null', DATA))
print('wrote', out, '|', len(SRC['clips']), 'clips |', round(out.stat().st_size/1024), 'KB')
