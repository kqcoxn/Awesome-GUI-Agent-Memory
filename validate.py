#!/usr/bin/env python3
"""Validate artifact accounting and sampling, not scientific correctness."""
import csv, hashlib, json
from pathlib import Path
from collections import Counter
P=Path(__file__).resolve().parent
def j(n): return json.loads((P/n).read_text())
def c(n): return list(csv.DictReader((P/n).open(encoding='utf-8-sig')))
claims=j('claims.json'); sources=c('source_registry.csv'); by={s['source_id']:s for s in sources}
assert len(claims)==75 and len(sources)==192
assert len({x['source_id'] for x in claims})==55
for x in claims:
 assert x['source_id'] in by
 assert x['evidence_excerpt'] and x['scope_limit'] and x['pdf_page']
assert len(c('family_disposition.csv'))==155
assert Counter(r['core_adoption'] for r in c('family_disposition.csv'))=={'adopted':34,'not_selected':121}
assert len(c('adopted_outside_155.csv'))==21
m=c('capability_matrix.csv');assert len(m)==1650
assert Counter(r['status'] for r in m)=={'present':122,'unassessed':1528}
assert Counter(r['cell'].split('.')[1] for r in m if r['status']=='present')==j('matrix_counts.json')['by_operation']
ids=[x['claim_id'] for x in sorted(claims,key=lambda x:hashlib.sha256(f'20260908:{x["claim_id"]}'.encode()).hexdigest())[:15]]
assert ids==j('validation/selected_claim_ids.json')
assert ids==[x['claim_id'] for x in c('validation/human_review.csv')]
assert len(c('search/arxiv_returned_records.csv'))==12
assert len({x['arxiv_url'] for x in c('search/arxiv_returned_records.csv')})==8
manifest=P/'manifest.sha256'
if manifest.exists():
 for line in manifest.read_text().splitlines():
  expected,name=line.split('  ',1);assert hashlib.sha256((P/name).read_bytes()).hexdigest()==expected,name
pending=sum(not x['judgement'] for x in c('validation/human_review.csv'))
print(f'Accounting, identities, sample and manifest passed. Human judgements pending: {pending}/15.')
