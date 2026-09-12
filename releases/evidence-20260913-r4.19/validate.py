"""Validate package hashes, counts and record links."""
import csv, hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parent
def j(n): return json.loads((P/n).read_text(encoding='utf-8'))
def c(n): return list(csv.DictReader((P/n).open(encoding='utf-8-sig')))
for line in (P/'manifest.sha256').read_text(encoding='utf-8').splitlines():
    digest,name=line.split('  ',1)
    assert hashlib.sha256((P/name).read_bytes()).hexdigest()==digest,name
claims=j('current/claims.json'); ids={r['claim_id'] for r in claims}
assert len(claims)==len(ids)==75
assert len({r['source_id'] for r in claims})==55
profile=c('current/corpus_profile.csv')
assert len(profile)==55 and {r['source_id'] for r in profile}=={r['source_id'] for r in claims}
assert sum(not r['platform'].startswith('Not profiled') for r in profile)==33
m=c('current/capability_matrix.csv')
assert len(m)==1650 and sum(r['status']=='present' for r in m)==123
acq = j('current/acquisition_records.json')
assert acq['arxiv_raw_hits'] == sum(q['hits'] for q in acq['queries']) == 544
assert len({r['arxiv_id'] for r in acq['arxiv_records']}) == acq['arxiv_unique_records'] == 346
assert len(acq['outside_inventory_sources']) == 21
assert all(r['acquisition_record'] and r['evidence_sha256'] for r in acq['outside_inventory_sources'])
for r in j('current/outside_inventory_uses.json'):
    assert set(r['claim_ids'].split(';'))<=ids
extra=j('current/mechanism_comparisons.json')
assert len(extra)==24 and all(r['locator'] and r['manuscript_uses'] for r in extra)
print('Package hashes, counts and record links passed.')
