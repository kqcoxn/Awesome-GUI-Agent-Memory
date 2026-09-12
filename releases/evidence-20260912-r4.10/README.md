# GUI-agent memory evidence: evidence-20260912-r4.10

Evidence for *Memory for GUI Agents: A Framework Survey of Lifecycles and State Layers*.
Source collection ended on 10 September 2026; the publication window ends on 8 September 2026.

## Reading guide

- `current/evidence_methods.md`: collection and coding details, counting units, evidence roles, acquisition flow, and the full Scopus search example.
- `current/claims.json`: 75 claims from 55 coded sources, with versions, source URLs, passages, locations, paraphrases, scope, and matrix assignments. Source identities are in `baseline/source_registry.csv`.
- `current/capability_matrix.csv`, `matrix_examples.csv`, `matrix_counts.json`: the current matrix. There are 123 positive source-cell assignments: 119 primary and four auxiliary. Of 30 cells, 27 have primary support, one has auxiliary-only support, and two remain unassessed.
- `current/matrix_changes.json`: changes from the frozen baseline. PC-037 adds AutoDroid L2-R support; source and claim counts are unchanged.
- `current/outside_inventory_uses.json`: analytical uses of the 21 coded sources outside the 155-family inventory.
- `current/mechanism_comparisons.json`: 21 additional source-specific comparison records, with consulted versions, URLs, locations, paraphrases, boundaries, and manuscript section-file/paragraph locations. These are a different set from the 21 outside-inventory coded sources and do not add matrix claims.
- `current/selection_summary.csv`: 34 inventory families selected for core claims, 113 not selected for claims, eight contextual non-selections, plus 21 coded sources acquired outside the inventory. Individual dispositions remain in `baseline/family_disposition.csv`.
- `current/effects.json`, `evaluation_protocols.csv`, `survey_comparison.csv`, and the three comparison-table `.tex` files: effects, evaluation conditions, survey comparisons, representative systems, and maintenance operations.
- `current/*references.bib`: source bibliographies.
- `baseline/search/`: recorded searches and returned records. The full `baseline/` directory preserves the evidence-20260908 release byte-for-byte.

## Validation and versioning

Run `python validate.py` from this directory to check file hashes, counts, and record links. The baseline has its own validator for the previous 122-assignment matrix. Use the current matrix in place of the baseline matrix, without adding their rows together.

`version.json` identifies the evidence version and corresponding manuscript hashes; `manifest.sha256` identifies the package files. The historical sample forms and verification provenance remain available in the data records. Blank sample forms are historical artifacts, not outstanding review tasks or individual correctness judgments.

Selection is purposive. Counts describe the assembled evidence, not field prevalence. Some historical screening decisions are incompletely documented. Additional records retain their specific scope limits; Mobile-Agent-E has a fixed source URL and section locations but no archived full-text hash. Hash and schema checks establish technical consistency, not scientific correctness.

## Access and rights

This package is published under `releases/` in https://github.com/kqcoxn/gui-memory-evidence with a matching immutable version tag. The earlier `evidence-20260908` tag remains available.

The package contains research annotations, attributed source excerpts, and supporting data. Third-party full texts, manuscript PDFs and full manuscript paragraphs, credentials, institutional-access sessions, and private repository history are not distributed. Source documents are accessed through their recorded URLs and retain their applicable rights. No blanket license is asserted over third-party material.
