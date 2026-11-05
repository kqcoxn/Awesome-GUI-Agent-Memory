# Data dictionary

Companion data for *Memory in GUI Agents: A Survey*.
Version: `evidence-20261031-v1`.
Archive DOI: https://doi.org/10.5281/zenodo.23985925.
Fixed release: https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/releases/tag/evidence-20261031-v1.
The publication cutoff is 31 October 2026.

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
| `first_public_date` | Earliest located public date, retaining source precision, used for annual counts; exact earliest availability may be unestablished |
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

The subject categories contain 304 direct-memory works and 53 evaluation or security works. The analytical roles comprise 297 mechanism works, 43 evaluation works and 17 component-diagnostic works.

For mechanism works, `levels` and `operations` are projections of the documented pairs in `matrix_assignments.csv`, in L1–L5 and W/P/R/U/V/F order. The two lists do not imply their Cartesian product. For evaluation and component-diagnostic works, these fields describe tested capabilities, and no mechanism assignments are generated from them.

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

`matrix_assignments.csv` contains one reviewed work–cell assignment per row. Its 1,498 rows connect 297 mechanism works to the 30 layer–operation combinations.

| Field | Meaning |
|---|---|
| `work_id` | Work identifier in `catalogue.csv` |
| `citation_key` | Corresponding manuscript reference key |
| `cell` | Assigned layer and operation, written as `L1.W`, `L2.R`, etc. |

Join the matrix to the catalogue on `work_id` to obtain object and use descriptions, adopted versions and supporting source locations. The matrix rows specify the assigned object–operation pairs. Unassigned pairs remain unassessed; cell counts describe supported assignments in this selected corpus rather than field-wide prevalence or research gaps.

## Corpus counts

`corpus_counts.json` aggregates the catalogue and matrix:

- `included_works`: number of distinct catalogue works.
- `mechanism_works`: works with the `primary_mechanism` role.
- `work_cell_assignments`: number of matrix rows.
- `by_year`: distinct works grouped by the year in `first_public_date`.
- `by_theme`, `by_category`, `by_role`: distinct works grouped by the corresponding catalogue field.
- `by_cell`: distinct assigned works per matrix cell.

Each work contributes once to its annual, theme, category and role totals. A work assigned to several matrix cells contributes once to each of those cells. Annual totals are 12, 40, 105 and 200 for 2023–2026; the 2026 coverage ends on 31 October.

## Search records

`search_queries.csv` describes 14 query variants across Scopus, Web of Science Core Collection, IEEE Xplore, ACM Digital Library and arXiv.

| Field | Meaning |
|---|---|
| `search_id` | Unique database/query/field combination |
| `database` | Database or indexing service |
| `query_id` | Query family and platform variant |
| `fields` | Searched metadata fields |
| `query` | Database-adapted Boolean concept expression |
| `execution_dates` | Actual retrieval dates contributing to the consolidated query, separated by semicolons; includes a recorded zero-result execution |
| `records` | Distinct source records within this database/query/field combination |

`MAIN` identifies GUI-agent and model queries; `SUPP` identifies memory and experience-reuse queries. ACM suffixes specify `ABSTRACT`, `TITLE` or `KEYWORD`. A native source identifier is counted once within each combination. Overlap across query variants and databases is resolved in the candidate pool. Eligibility is checked against the public-version cutoff of 31 October 2026.

The four publisher/indexing databases were queried on 24 September and 1 November 2026; arXiv on 25 September and 1 November. These retrieval dates do not substitute for public availability dates. There was no language filter or lower publication-year limit; queries used English terms. Work identities are grouped using exact identifiers or recorded checks of versions, renamed titles, authors and distinctive source descriptions. A later formal publication can establish identity without replacing the adopted source version.

## Selection totals

`selection_summary.json` records the units used in literature acquisition and selection.

| Field | Meaning |
|---|---|
| `publication_cutoff` | Latest eligible public date |
| `search_queries` | Number of database/query/field combinations |
| `search_records` | Source records summed across the consolidated query variants |
| `merged_candidates` | Candidates after identifier-based merging |
| `duplicate_records` | Additional query hits merged into those candidates |
| `retained_for_fulltext` | Legacy field name for candidates selected at the broad title/abstract stage for further examination; does not mean that every candidate received full-text review |
| `not_selected_at_title_abstract` | Candidates not selected at that stage |
| `included_works` | Distinct works in the classification catalogue |
| `included_from_search_pool` | Classified works with candidate IDs registered in the catalogue's source table; an acquisition-route count |
| `included_from_additional_sources` | Classified works from verified existing sources, citation tracing, publication-venue checks or targeted supplementary searches |
| `candidate_accounting` | Retained-candidate total, mutually exclusive disposition counts, registered candidate and pool-work totals, additional represented records, and distinct represented works |

The 8,195 source records yield 5,445 identifier-merged candidates, with 2,750 duplicate occurrences across query variants and databases. Title/abstract selection retains 1,724 candidates for further examination. The classified corpus contains 357 works: 310 acquired through the search pool and 47 through supplementary identification. The same eligibility criteria apply to all included works.

## Candidate dispositions

`selection_accounting.csv` contains one row per retained candidate. It reconciles recorded decisions without performing a new relevance screen. Current inclusion links take precedence over earlier nonselection judgments; subsequent boundary decisions precede earlier source and metadata judgments. Original reasons and their evidence stages are preserved. Attaching a recorded nonselection judgment to its exact title does not establish an identity merge. Identity links use exact identifiers or explicit version/alias adjudications, including three recorded title–author–abstract identity checks for DOI-free records of COLA, Self-MAP and SPA-Bench.

| Field | Meaning |
|---|---|
| `candidate_id` | Stable candidate identifier after identifier-based record merging |
| `title` | Candidate title in the merged search pool |
| `disposition` | Mutually exclusive recorded status, as defined below |
| `evidence_stage` | Evidence stage of the decision or identity check; metadata judgments remain distinct from original-source checks |
| `work_id` | Current classified work representing the candidate, if established |
| `link_basis` | Registered candidate association, identifier/version linkage, or attachment of an existing decision by identifier/title |
| `recorded_reason` | Existing reason, or explanation of the registered inclusion/identity link; original reasons retain their recorded language |
| `evidence_record` | Relative source filename and record pointer in the research evidence; JSON list indices are zero-based, named IDs/ordinals retain the source's convention |

| Disposition | Candidates | Interpretation |
|---|---:|---|
| `included_registered` | 386 | Registered records of 310 classified pool works; 76 records beyond one per work |
| `included_additional_record` | 38 | Further indexed or version records of classified works; adds no catalogue work |
| `not_selected_boundary` | 15 | Candidate records covered by the GUI-memory boundary nonselection decisions |
| `not_selected_source_check` | 64 | Other recorded nonselection following source checks |
| `not_selected_followup` | 31 | Other recorded follow-up nonselection; source access and scope limitations remain in the reasons |
| `not_selected_work_judgment` | 4 | Other explicit work-level nonselection decisions |
| `not_selected_unverified` | 41 | Source follow-up did not establish eligibility; includes method, access or date uncertainty |
| `focused_adjacent_gui` | 842 | Focused memory-relevance assessment classified the record as adjacent GUI research |
| `focused_outside_scope` | 216 | Focused assessment classified the record as outside scope |
| `focused_uncertain` | 87 | Focused assessment retained uncertainty; no later inclusion established |

The 386 registered and 38 additional records represent 311 classified works: the 310 pool-acquired works and MobA, a supplementarily acquired work also indexed in the pool. Acquisition-route totals are mutually exclusive; database coverage overlaps them. The remaining 1,300 candidates have the dispositions above. These are candidate-record counts at different evidence stages, not full-text exclusion counts. In particular, the 87 uncertain relevance judgments remain distinct from verified irrelevance. Classified studies retain adopted-source evidence in the catalogue; the candidate ledger describes how records are represented or were not selected.


## Validation

Run `python validate.py` from the extracted directory using Python 3.9 or later. The script verifies the SHA-256 file manifest, unique work identifiers and citation keys, required source fields, legal codes, duplicate assignments, mechanism coverage, agreement between catalogue labels and paired assignments, query totals and execution-date fields, candidate disposition totals and work links, selection totals and aggregate counts. The manuscript build additionally checks the rendered candidate-disposition table, catalogue, exact source-index membership, both representative matrices, and mechanism citations in the reuse and maintenance tables against the same registries.
