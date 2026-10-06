#!/usr/bin/env python3
import pathlib, re, sys
root=pathlib.Path(__file__).resolve().parents[1]
errors=[]
for p in (root/'content').rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): errors.append(f'{p}: Front Matter fehlt')
    if re.search(r'<meta\s+name=["\']robots',text,re.I): errors.append(f'{p}: robots-Meta gehört ins Layout')
if errors:
    print('\n'.join(errors),file=sys.stderr); sys.exit(1)
print('Content-Prüfung erfolgreich.')
