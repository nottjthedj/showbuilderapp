#!/usr/bin/env python3
import json, pathlib
HERE = pathlib.Path(__file__).parent
SRC = json.load(open('/home/user/showbuilderapp/marketing/voice-script.json'))
TPL = (HERE/'_vo_template.html').read_text()
out = HERE/'recording-script.html'
out.write_text(TPL.replace('/*__DATA__*/null', json.dumps(SRC, ensure_ascii=False)))
print(f'{out.name} | {SRC["meta"]["lines"]} lines | {round(out.stat().st_size/1024)} KB')
