# GUI-agent memory evidence

Evidence for *Memory for GUI Agents: A Framework Survey of Lifecycles and State Layers*.
Publication coverage: 10 September 2026.

## Contents

- `current/evidence_methods.md`: retrieval, counting units, coding and source profile.
- `current/claims.json`: 75 claims from 55 sources, with source versions, passages, locations and matrix assignments.
- `current/capability_matrix.csv`, `matrix_examples.csv`, `matrix_counts.json`: 123 positive source-cell assignments; 27 primary-supported cells, one auxiliary-only cell, and two unassessed cells.
- `current/corpus_profile.csv`: years, venue metadata and platform settings.
- `current/mechanism_comparisons.json`: 24 version-specific comparisons with manuscript locations.
- `current/outside_inventory_uses.json`, `selection_summary.csv`: source uses and selection counts.
- `current/effects.json`, `evaluation_protocols.csv`, `survey_comparison.csv`: numerical comparisons, evaluation conditions and related surveys.
- `current/*references.bib` and `.tex` tables: bibliographies and manuscript evidence tables.
- `current/cutoff_*.json`, `baseline/search/`: retrieval records, queries and source hashes.
- `baseline/source_registry.csv`, `family_disposition.csv`, `family_aliases.csv`: source identities and candidate records.
- `current/matrix_changes.json`: assignment differences relative to the historical baseline.

## Validation and versions

Run `python validate.py` from this directory to check hashes, counts and record links.
`version.json` identifies this package and its manuscript hashes; `manifest.sha256` lists file hashes.
Historical packages are available through the repository's version tags.

## Source access

The package provides research annotations, attributed excerpts and supporting data. Source URLs identify the original publications. Third-party full texts and manuscript PDFs are distributed by their respective owners. Rights in source material remain with its owners.
