#!/usr/bin/env python3
import json, pathlib
HERE = pathlib.Path(__file__).parent
SRC = json.load(open('/home/user/showbuilderapp/marketing/shot-list.json'))
TPL = (HERE/'_shotlist_template.html').read_text()

def build(mode, title, eyebrow, h1, keys, out):
    data = {k: SRC[k] for k in ('meta','blocks') + keys}
    # every page needs the seed text so character-mode can swap it out for a token
    data['seedIndex'] = [{'key': c['key'], 'name': c['name'], 'seed': c['seed']}
                         for c in SRC['characters'] if c.get('seed')]
    html = (TPL.replace('__TITLE__', title).replace('__EYEBROW__', eyebrow)
               .replace('__H1__', h1).replace('__MODE__', mode)
               .replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False)))
    (HERE/out).write_text(html)
    print(f'{out}: {round((HERE/out).stat().st_size/1024)} KB')

build('characters', 'The Score — shot list by character', 'batch one person at a time',
      '<span class="a">Shot List</span><br><span class="b">By Character</span>',
      ('howToBatch','characters'), 'shot-list-characters.html')
build('ensemble', 'The Score — two-hander shot list', 'two subjects, one frame',
      '<span class="a">Ensemble</span><br><span class="b">Shot List</span>',
      ('ensembleRules','ensemble'), 'shot-list-ensemble.html')
