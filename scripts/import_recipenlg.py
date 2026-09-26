#!/usr/bin/env python3
"""Convert RecipeNLG full_dataset.csv into Feastly's compact JSON schema.
Download RecipeNLG from its official project page first; this script never scrapes sites.
Usage: python scripts/import_recipenlg.py path/to/full_dataset.csv data/recipenlg.json
"""
import csv,json,sys,re,hashlib

def arr(v):
    if not v:return []
    try:
        x=json.loads(v)
        return x if isinstance(x,list) else [str(x)]
    except Exception:
        return [x.strip() for x in re.split(r'\s*\|\s*',v) if x.strip()]

def main():
    if len(sys.argv)<2: raise SystemExit('Usage: python scripts/import_recipenlg.py full_dataset.csv [output.json]')
    src=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else 'data/recipenlg.json'; rows=[]; seen=set()
    with open(src,encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            title=(row.get('title') or '').strip(); ingredients=arr(row.get('ingredients','')); directions=arr(row.get('directions',''))
            if not title or not ingredients: continue
            key=hashlib.sha1((title.lower()+'|'+ '|'.join(ingredients).lower()).encode()).hexdigest()
            if key in seen: continue
            seen.add(key); rows.append({'id':key[:12],'slug':re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-'),'title':title,'category':'RecipeNLG','ingredients':ingredients,'directions':directions,'source':row.get('link') or ''})
    with open(out,'w',encoding='utf-8') as f: json.dump(rows,f,ensure_ascii=False,separators=(',',':'))
    print(f'Wrote {len(rows):,} recipes to {out}')
if __name__=='__main__':main()
