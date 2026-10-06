#!/usr/bin/env python3
import json, pathlib, sys, urllib.request
try:
    import yaml
except ImportError:
    sys.exit("PyYAML fehlt. Installiere: python3 -m pip install -r scripts/requirements.txt")
root=pathlib.Path(__file__).resolve().parents[1]
config=json.loads((root/'config/openapi-sources.json').read_text(encoding='utf-8'))
for source in config['sources']:
    print(f"Lade {source['name']} ...")
    req=urllib.request.Request(source['url'],headers={'User-Agent':'rl-digital-api-docs/1.0'})
    with urllib.request.urlopen(req,timeout=30) as response:
        data=json.load(response)
    target=root/source['target']; target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8')
    print(f"Geschrieben: {target.relative_to(root)}")
