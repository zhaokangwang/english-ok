"""Batch loading and referential identity guards. No user learning data touched."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def identities(data):
    result={}
    for w in data['words']:
        result[w['id']]=['word',w['spelling']]
        for s in w['senses']:result[s['id']]=['sense',w['id']]
        for e in w['examples']:result[e['id']]=['example',w['id'],e['sense_id']]
        for r in w['related']:result[r['id']]=['related',w['id'],r['spelling']]
    return result
def guard_identities(old,new):
    for key,value in old.items():
        if key not in new: raise ValueError(f'Existing ID removed: {key}; explicit migration required')
        if new[key]!=value: raise ValueError(f'Existing ID repurposed: {key}; explicit migration required')
def load_content():
    plan=read('content/import-plan.json'); data=read('content/sample.json')
    data['words']=[];data['content_version']=plan['content_version'];batches=[]
    seen_batches=set()
    for batch in plan['approved_batches']:
        if batch['id'] in seen_batches:raise ValueError('Duplicate batch in import plan')
        seen_batches.add(batch['id'])
        part=read(batch['file'])
        if part['source_id']!=plan['source_id'] or part['format_version']!=1:raise ValueError('Batch source/format mismatch')
        lo,hi=batch['context_pages']
        associated=read(batch['associated_file'])
        for item in associated['items']:
            if not lo<=item['pdf_page']<=hi:raise ValueError('Associated material page outside batch')
        for w in part['words']:
            if not w['pdf_pages'] or any(not isinstance(p,int) or not lo<=p<=hi for p in w['pdf_pages']):raise ValueError(f'Out of batch page range: {w["id"]}')
            for e in w['examples']:
                if e['pdf_page'] not in w['pdf_pages'] or e['printed_page']!=f'{e["pdf_page"]-8:03}':raise ValueError('Wrong example page attribution')
        data['words'].extend(part['words']);batches.append((batch,part))
    registry=ROOT/'content/id-registry.json'
    if registry.exists():guard_identities(read('content/id-registry.json'),identities(data))
    return data,plan,batches
