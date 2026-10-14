"""Check file integrity, data relationships and reported counts offline."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

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
check(len(rows) == len(by_id) == len({r['citation_key'] for r in rows}) == 289,
      'Catalogue identity mismatch')
check(Counter(r['category'] for r in rows) == {'direct_memory': 250, 'memory_evaluation_security': 39},
      'Category counts mismatch')
check(Counter(r['role'] for r in rows) == {'primary_mechanism': 246, 'primary_evaluation': 33, 'component_diagnostic': 10},
      'Role counts mismatch')
for row in rows:
    for field in ['title', 'authors', 'adopted_version', 'source_url', 'source_locator', 'first_public_date']:
        check(bool(row[field]), f'Missing {field}: {row["work_id"]}')
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
check(len(matrix) == len(pairs) == 1119, 'Matrix assignment count mismatch')
check({r['work_id'] for r in matrix} == {r['work_id'] for r in rows if r['role'] == 'primary_mechanism'},
      'Matrix work coverage mismatch')
check({cell for _, cell in pairs} == valid_cells, 'Matrix cell coverage mismatch')
profile = readjson('corpus_counts.json')
check(profile['included_works'] == len(rows), 'Corpus size mismatch')
check(profile['mechanism_works'] == 246 and profile['work_cell_assignments'] == len(pairs),
      'Matrix summary mismatch')
for field in ['theme', 'category', 'role']:
    check(profile['by_' + field] == dict(Counter(r[field] for r in rows)), f'{field} counts mismatch')
check(profile['by_year'] == dict(Counter(r['first_public_date'][:4] for r in rows)), 'Year counts mismatch')
check(profile['by_cell'] == dict(Counter(cell for _, cell in pairs)), 'Cell counts mismatch')
runs = readcsv('search_runs.csv')
summary = readjson('selection_summary.json')
check(len(runs) == summary['query_runs'] == 13, 'Query count mismatch')
check(len({(r['database'], r['query_id']) for r in runs}) == len(runs), 'Duplicate query run')
check(len({r['database'] for r in runs}) == 5, 'Database count mismatch')
check(all(r['date'] and r['query'] for r in runs), 'Incomplete query record')
check(sum(int(r['hits']) for r in runs) == summary['search_records'] == 7409, 'Search total mismatch')
check(summary['merged_candidates'] == 4951 and summary['duplicate_records'] == 2458,
      'Candidate counts mismatch')
check(summary['search_records'] - summary['duplicate_records'] == summary['merged_candidates'],
      'Deduplication total mismatch')
check(summary['retained_for_fulltext'] == 1601 and summary['not_selected_at_title_abstract'] == 3350,
      'Selection counts mismatch')
check(summary['retained_for_fulltext'] + summary['not_selected_at_title_abstract'] == summary['merged_candidates'],
      'Selection total mismatch')
check(summary['included_from_search_pool'] == 271 and summary['included_from_additional_sources'] == 18,
      'Inclusion routes mismatch')
check(summary['included_from_search_pool'] + summary['included_from_additional_sources'] == summary['included_works'] == len(rows),
      'Inclusion total mismatch')
print(f'Verified {len(rows)} works, {len(pairs)} matrix assignments, {len(runs)} query runs, selection totals and all file hashes.')
