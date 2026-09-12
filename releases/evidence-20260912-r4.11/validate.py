"""Structural checks only; no semantic or human validation."""
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
m=c('current/capability_matrix.csv')
assert len(m)==1650 and sum(r['status']=='present' for r in m)==123
for r in j('current/outside_inventory_uses.json'):
    assert set(r['claim_ids'].split(';'))<=ids
extra=j('current/mechanism_comparisons.json')
assert len(extra)==21 and all(r['locator'] and r['manuscript_uses'] for r in extra)
sample=c('baseline/validation/human_review.csv')
assert len(sample)==15 and all(not r['judgement'] for r in sample)
review=c('current/human_review.csv'); by={r['claim_id']:r for r in claims}
assert [r['claim_id'] for r in review]==[r['claim_id'] for r in sample]
for r in review:
    claim=by[r['claim_id']]
    assert list(filter(None,r['cells'].split(';')))==claim['cells']
    assert r['passage']==claim['evidence_excerpt'] and r['paraphrase']==claim['claim_zh']
    assert r['locator']==claim['locator']
    assert r['attachment_version']==j('version.json')['evidence_version']
    encoded=(json.dumps(claim,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    assert r['claim_content_sha256']==hashlib.sha256(encoded).hexdigest()
    assert all(not r[k] for k in ['judgement','issue_types','reviewer','review_date','notes','added_L2_R_judgement'])
assert next(r for r in review if r['claim_id']=='PC-037')['change_to_review']

print('Hashes, current accounting and record links passed; historical sample fields remain blank; user-reported full review is recorded in version.json.')
