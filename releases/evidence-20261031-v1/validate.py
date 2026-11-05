"""Check file integrity, data relationships and reported counts offline."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent

def readcsv(name):
    with (ROOT / name).open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream))

def readjson(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def check(condition, message):
    if not condition:
        raise ValueError(message)

manifest = {}
for line in (ROOT / 'manifest.sha256').read_text(encoding='utf-8').splitlines():
    sha, name = line.split('  ', 1)
    path = (ROOT / name).resolve()
    check(path.is_relative_to(ROOT), f'Invalid path: {name}')
    check(name not in manifest, f'Duplicate manifest entry: {name}')
    manifest[name] = sha
    check(hashlib.sha256(path.read_bytes()).hexdigest() == sha, f'Hash mismatch: {name}')
actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
          if p.is_file() and '__pycache__' not in p.parts}
check(actual == set(manifest) | {'manifest.sha256'}, 'File inventory mismatch')
rows = readcsv('catalogue.csv')
by_id = {r['work_id']: r for r in rows}
check(len(rows) == len(by_id) == len({r['citation_key'] for r in rows}) ,
      'Catalogue identity mismatch')
check(Counter(r['category'] for r in rows) == readjson('corpus_counts.json')['by_category'],
      'Category counts mismatch')
check(Counter(r['role'] for r in rows) == readjson('corpus_counts.json')['by_role'],
      'Role counts mismatch')
for row in rows:
    check(row['role'] in {'primary_mechanism', 'primary_evaluation', 'component_diagnostic'}, 'Invalid catalogue role')
    check(row['category'] in {'direct_memory', 'memory_evaluation_security'}, 'Invalid catalogue category')
    for field in ['title', 'authors', 'adopted_version', 'source_url', 'source_locator', 'first_public_date']:
        check(bool(row[field]), f'Missing {field}: {row["work_id"]}')
    check(urlparse(row['source_url']).scheme in {'http', 'https'},
          f'Non-public source URL: {row["work_id"]}')
    check(bool(row['object_zh']) and bool(row['use_zh']),
          f'Missing Chinese description: {row["work_id"]}')
    check(not re.search(r'(?<![A-Za-z])[A-Za-z]:[/\\]|file://', ' '.join(row.values())),
          f'Local path in public catalogue: {row["work_id"]}')
matrix = readcsv('matrix_assignments.csv')
valid_cells = {f'L{level}.{operation}' for level in range(1, 6) for operation in 'WPRUVF'}
pairs = set()
for row in matrix:
    check(row['work_id'] in by_id, 'Unknown matrix work')
    work = by_id[row['work_id']]
    check(work['citation_key'] == row['citation_key'], 'Matrix citation mismatch')
    check(work['role'] == 'primary_mechanism', 'Matrix role mismatch')
    check(row['cell'] in valid_cells, 'Invalid matrix cell')
    pairs.add((row['work_id'], row['cell']))
check(len(matrix) == len(pairs), 'Matrix assignment count mismatch')
check({r['work_id'] for r in matrix} == {r['work_id'] for r in rows if r['role'] == 'primary_mechanism'},
      'Matrix work coverage mismatch')
check({cell for _, cell in pairs} == valid_cells, 'Matrix cell coverage mismatch')
for work in rows:
    levels = [] if work['levels'].strip() == 'not assigned' else [s.strip() for s in work['levels'].split(';') if s.strip()]
    operations = [] if work['operations'].strip() == 'not assigned' else [s.strip() for s in work['operations'].split(';') if s.strip()]
    check(len(levels) == len(set(levels)) and set(levels) <= {f'L{i}' for i in range(1, 6)}, 'Invalid catalogue layers')
    check(len(operations) == len(set(operations)) and set(operations) <= set('WPRUVF'), 'Invalid catalogue operations')
    if work['role'] == 'primary_mechanism':
        assigned = {cell for wid, cell in pairs if wid == work['work_id']}
        check(set(levels) == {cell.split('.')[0] for cell in assigned}, 'Catalogue/matrix layer mismatch')
        check(set(operations) == {cell.split('.')[1] for cell in assigned}, 'Catalogue/matrix operation mismatch')
profile = readjson('corpus_counts.json')
check(profile['included_works'] == len(rows), 'Corpus size mismatch')
check(profile['mechanism_works'] == sum(r['role'] == 'primary_mechanism' for r in rows) and profile['work_cell_assignments'] == len(pairs),
      'Matrix summary mismatch')
for field in ['theme', 'category', 'role']:
    check(profile['by_' + field] == dict(Counter(r[field] for r in rows)), f'{field} counts mismatch')
check(profile['by_year'] == dict(Counter(r['first_public_date'][:4] for r in rows)), 'Year counts mismatch')
check(profile['by_cell'] == dict(Counter(cell for _, cell in pairs)), 'Cell counts mismatch')
searches = readcsv('search_queries.csv')
summary = readjson('selection_summary.json')
check(len(searches) == summary['search_queries'], 'Query count mismatch')
check(len({r['search_id'] for r in searches}) == len(searches), 'Duplicate query variant')
check(len({r['database'] for r in searches}) == 5, 'Database count mismatch')
check(all(r['fields'] and r['query'] and r['execution_dates'] for r in searches), 'Incomplete query record')
check(all(all(len(d) == 10 and d[:4] == '2026' for d in r['execution_dates'].split('; ')) for r in searches),
      'Invalid execution dates')
check(sum(int(r['records']) for r in searches) == summary['search_records'], 'Search total mismatch')
check(summary['search_records'] - summary['duplicate_records'] == summary['merged_candidates'],
      'Deduplication total mismatch')
check(summary['retained_for_fulltext'] + summary['not_selected_at_title_abstract'] == summary['merged_candidates'],
      'Selection total mismatch')
check(summary['included_from_search_pool'] + summary['included_from_additional_sources'] == summary['included_works'] == len(rows),
      'Inclusion total mismatch')
accounting = readcsv('selection_accounting.csv')
detail = summary['candidate_accounting']
check(len(accounting) == len({r['candidate_id'] for r in accounting}) == summary['retained_for_fulltext'],
      'Candidate accounting coverage mismatch')
check(dict(Counter(r['disposition'] for r in accounting)) == detail['by_disposition'], 'Disposition totals mismatch')
check(all(r['evidence_record'] and r['evidence_stage'] and r['recorded_reason'] for r in accounting),
      'Incomplete decision provenance')
check({r['disposition'].startswith('included_') for r in accounting if r['work_id']} == {True},
      'Unexpected non-inclusion work link')
check(all(r['work_id'] in by_id for r in accounting if r['work_id']), 'Unknown candidate work link')
check(all(bool(r['work_id']) == r['disposition'].startswith('included_') for r in accounting),
      'Missing or unexpected candidate work link')
check(sum(r['disposition'] == 'included_registered' for r in accounting) == detail['registered_candidates'],
      'Registered candidate total mismatch')
check(len({r['work_id'] for r in accounting if r['disposition'] == 'included_registered'}) == detail['registered_pool_works'] == summary['included_from_search_pool'],
      'Registered work total mismatch')
check(sum(r['disposition'] == 'included_additional_record' for r in accounting) == detail['additional_represented_candidates'],
      'Additional identity total mismatch')
check(len({r['work_id'] for r in accounting if r['work_id']}) == detail['represented_works'],
      'Represented work total mismatch')
print(f'Verified {len(rows)} works, {len(pairs)} matrix assignments, {len(searches)} query variants, selection totals and all file hashes.')
