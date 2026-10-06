#!/usr/bin/env python3
import pathlib, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML fehlt. Installiere: python3 -m pip install -r scripts/requirements.txt")
root=pathlib.Path(__file__).resolve().parents[1]
errors=[]
for path in sorted((root/'static/openapi').glob('*.yaml')):
    try:
        data=yaml.safe_load(path.read_text(encoding='utf-8'))
        if not isinstance(data,dict): raise ValueError('Wurzel ist kein Objekt')
        for key in ('openapi','info','paths'):
            if key not in data: raise ValueError(f'Pflichtfeld fehlt: {key}')
        print(f"OK: {path.relative_to(root)} ({data.get('openapi')})")
    except Exception as exc: errors.append(f"{path}: {exc}")
if errors:
    print('\n'.join(errors),file=sys.stderr); sys.exit(1)
