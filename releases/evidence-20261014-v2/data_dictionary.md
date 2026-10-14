# Data dictionary

Companion data for *The State of Memory in GUI Agents: A Lifecycle-Centric Survey*.
Version: `evidence-20261014-v2`. DOI: https://doi.org/10.5281/zenodo.23366556.
The publication cutoff is 20 September 2026.

## Literature catalogue

`catalogue.csv` contains one row per classified work. CSV files use UTF-8 encoding and a header row. Dates retain their recorded precision: year, year–month or year–month–day. Empty identifier or version-date fields indicate that the corresponding value is unrecorded.

| Field | Meaning |
|---|---|
| `work_id` | Stable identifier connecting a work across the data tables |
| `citation_key` | Bibliographic key used for the work in the manuscript |
| `title` | Work title |
| `authors` | Registered author names |
| `doi` | Publication DOI, where recorded |
| `arxiv_ids` | Registered arXiv identifiers |
| `first_public_date` | Recorded first public date, used for annual counts |
| `date_basis_url` | Public-date evidence and its source link |
| `adopted_version` | Version consulted for the classification |
| `adopted_version_date` | Recorded date of the consulted version |
| `source_url` | Public link to the consulted source |
| `source_locator` | Page, section or passage supporting the classification |
| `theme` | Reading theme assigned to the work |
| `category` | Subject category: `direct_memory` or `memory_evaluation_security` |
| `role` | Analytical role: `primary_mechanism`, `primary_evaluation` or `component_diagnostic` |
| `levels` | Memory-object labels, separated by semicolons |
| `operations` | Lifecycle-operation labels, separated by semicolons |
| `object_en`, `object_zh` | English and Chinese descriptions of retained information |
| `use_en`, `use_zh` | English and Chinese descriptions of its subsequent GUI use |
| `model_role` | The language or vision-language model's role in the work |

The subject categories contain 250 direct-memory works and 39 evaluation or security works. The analytical roles comprise 246 mechanism works, 33 evaluation works and 10 component-diagnostic works.

### Reading themes

| Code | Theme |
|---|---|
| `visual` | Visual evidence |
| `interface` | Interface knowledge |
| `state` | Task state and trajectories |
| `skill` | Reusable skills |
| `user` | User and session context |
| `evaluation` | Evaluation |
| `security` | Security |

### Memory-object layers

| Code | Object |
|---|---|
| `L1` | Visual evidence |
| `L2` | Interface knowledge |
| `L3` | Task state and trajectories |
| `L4` | Reusable skills |
| `L5` | User and session context |

### Lifecycle operations

| Code | Operation |
|---|---|
| `W` | Write |
| `P` | Represent |
| `R` | Retrieve |
| `U` | Use |
| `V` | Verify/recover |
| `F` | Update/forget |

## Matrix assignments

`matrix_assignments.csv` contains one reviewed work–cell assignment per row. Its 1,119 rows connect 246 mechanism works to the 30 layer–operation combinations.

| Field | Meaning |
|---|---|
| `work_id` | Work identifier in `catalogue.csv` |
| `citation_key` | Corresponding manuscript reference key |
| `cell` | Assigned layer and operation, written as `L1.W`, `L2.R`, etc. |

Join the matrix to the catalogue on `work_id` to obtain object and use descriptions, adopted versions and supporting source locations. The matrix rows specify the assigned object–operation pairs.

## Corpus counts

`corpus_counts.json` aggregates the catalogue and matrix:

- `included_works`: number of distinct catalogue works.
- `mechanism_works`: works with the `primary_mechanism` role.
- `work_cell_assignments`: number of matrix rows.
- `by_year`: distinct works grouped by the year in `first_public_date`.
- `by_theme`, `by_category`, `by_role`: distinct works grouped by the corresponding catalogue field.
- `by_cell`: distinct assigned works per matrix cell.

Each work contributes once to its annual, theme, category and role totals. A work assigned to several matrix cells contributes once to each of those cells. Annual totals are 12, 40, 103 and 134 for 2023–2026; the 2026 coverage ends on 20 September.

## Search records

`search_runs.csv` records thirteen executed queries across Scopus, Web of Science Core Collection, IEEE Xplore, ACM Digital Library and arXiv.

| Field | Meaning |
|---|---|
| `database` | Database or indexing service |
| `date` | Query execution date |
| `query_id` | Query family and platform variant |
| `query` | Exact executed query expression |
| `hits` | Records returned by that query |

`MAIN` identifies the main GUI-agent and model queries; `SUPP` identifies the memory and experience-reuse queries. ACM suffixes identify the searched field (`ABSTRACT`, `TITLE` or `KEYWORD`); arXiv's `ATOM` suffix identifies the API query variant. The query expressions retain database-specific field syntax. Retrieval dates and the publication cutoff are recorded separately.

## Selection totals

`selection_summary.json` records the units used in literature acquisition and selection.

| Field | Meaning |
|---|---|
| `publication_cutoff` | Latest eligible public date |
| `query_runs` | Number of executed query records |
| `search_records` | Total records across the query results |
| `merged_candidates` | Candidates after identifier-based merging |
| `duplicate_records` | Additional query hits merged into those candidates |
| `retained_for_fulltext` | Candidates selected at the title/abstract stage for further examination |
| `not_selected_at_title_abstract` | Candidates not selected at that stage |
| `included_works` | Distinct works in the classification catalogue |
| `included_from_search_pool` | Classified works linked to the search candidate pool |
| `included_from_additional_sources` | Classified works from verified existing sources or citation tracing |

The 7,409 search records yield 4,951 merged candidates, with 2,458 duplicate occurrences. Title/abstract selection retains 1,601 candidates for further examination. The classified corpus contains 289 works: 271 linked to the search pool and 18 from additional sources.

## Validation

Run `python validate.py` from the extracted directory using Python 3.9 or later. The script verifies the SHA-256 file manifest, work identifiers, source fields, matrix assignments, query totals, selection totals and aggregate counts.
