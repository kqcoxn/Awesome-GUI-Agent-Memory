# Evidence methods

## Source acquisition and selection

Literature is collected through Scopus, Web of Science Core Collection, IEEE Xplore, ACM Digital Library, arXiv, and targeted retrieval of named mechanism papers and surveys. The publication cutoff is 10 September 2026. Database publication filters cover 2015–2026. arXiv date intervals and literal queries are specified in `acquisition_records.json` and `search_queries.tex`. English-language selection applies at retrieval in Scopus, WoS and ACM and at screening for IEEE and arXiv.

| Channel | Query hits | Distinct records within channel |
|---|---:|---:|
| Scopus | 216 | 128 |
| Web of Science | 75 | 47 |
| IEEE Xplore | 13 | 8 |
| ACM Digital Library | 10 | 7 |
| arXiv | 544 | 346 |

arXiv results are combined by base identifier across all recorded successful API and keyword queries. The API date intervals are 2015-01-01–2026-08-31 and 2026-08-25–2026-09-08; the advanced-search interval is 2026-09-02–2026-09-10 (latest submission). The ledger records membership and removes overlap. Failed query attempts have no hit count.

Cross-channel matching uses normalized DOI, arXiv base ID, database identifiers, and normalized title with first author and publication year (within one year). The 155-family selection inventory is a source-selection collection containing both search and citation-tracing candidates.


The inventory supplies 34 coded sources; 113 families are not selected for claim extraction and eight are contextual candidates. The 21 coded sources outside it comprise ten arXiv retrievals, one Scopus retrieval, five survey-collection sources and five targeted source retrievals. `acquisition_records.json` identifies each source, its available acquisition record, record locator and hash. Retrieval evidence does not establish a first-discovery query when that query was not retained. The five survey-collection sources are documented in the local reference catalogue; their original discovery queries are unavailable.

The coded subset contains 55 sources (33 primary mechanisms and 22 auxiliary sources) and 75 claims. The manuscript has 91 references and 24 other mechanism-comparison records. Selection is purposive; broad non-selection categories are available, but detailed individual exclusion reasons and some first-discovery records are incomplete.

## Coding

Each claim links a retained object and operation to a source version, passage, and location. Related versions form one work family. The package contains the source-level assignments and decision boundaries.

| Evidence role | Content | Use |
|---|---|---|
| Mechanism (M) | Retained object, operation, consumption path | Compare designs |
| Construct / protocol (C) | Task, endpoint, execution conditions | Identify measured capabilities |
| Comparative effect (E) | Intervention, baseline, budget, outcome | Interpret conditional differences |
| Survey organization (S) | Scope, categories, perspective | Position the framework |

The matrix contains 123 positive source-cell assignments: 119 primary and 4 auxiliary. Across 30 cells, 27 have primary support, one has auxiliary-only support, and two remain unassessed. A dash denotes an unassessed cell in this coded subset.

Assignment follows the retained object. PAL-UI's screenshot-based action validator checks an execution transition (L3–V). AutoDroid retrieves UI states and elements from app memory (L2–R). CausalCache restores archived images into active context (L1–R/U). Verifying an archived image or changing its retention lifetime would concern L1–V/F instead.

## Source profile and analytical examples

The platform profile partitions the 33 primary mechanisms: Web 12, mobile 10, desktop 6, Web/mobile 3, and desktop/mobile 2. Desktop includes OS benchmark tasks performed in browsers. Source years, venue metadata, platform labels, and PDF locations appear in `corpus_profile.csv`. Three venue labels use the consulted PDF title page: WebCoach (ICLR 2026), AutoDroid (ACM MobiCom 2024), and Synapse (ICLR 2024). Venue metadata is unidentified for 47 consulted versions.

The manuscript's failure and maintenance scenarios are analytical examples based on documented mechanisms. CausalCache uses PC-015 (PDF p.3), HIM-Agent uses PC-025/026 (PDF pp.6–7), and UFO2 uses version 2504.14603v1 (§§3.2–3.3). UFO2's append-only blackboard supports superseding a result. TRACE, GraphDroid, and Cao's procedural-memory study provide version-specific qualitative comparisons with source hashes and section locations in the retrieval records.

## Search example

Scopus Advanced Search, Q1_CORE: 74 query hits, executed 2 September 2026. Line wrapping below is for display.

```text
TITLE-ABS-KEY((("GUI agent*" OR "UI agent*" OR "graphical user
interface agent*" OR "user interface agent*" OR "computer-use agent*"
OR "computer use agent*" OR "computer-using agent*" OR "web agent*" OR
"web navigation agent*" OR "browser agent*" OR "mobile GUI agent*" OR
"desktop agent*" OR "OS agent*" OR "operating system agent*" OR
"software-use agent*" OR "cross-app* agent*" OR (("large language
model*" OR LLM* OR "vision-language model*" OR VLM* OR multimodal) W/3
agent* AND (GUI OR "graphical user interface*" OR "computer use" OR
browser* OR website* OR Android OR smartphone* OR "mobile app*" OR
desktop OR "operating system*" OR "software application*" OR
"cross-app*"))) AND (memor* OR "working memory" OR "short-term memory"
OR "long-term memory" OR "episodic memory" OR "semantic memory" OR
"procedural memory" OR "external memory" OR "experience memory" OR
"memory bank" OR "memory module" OR "memory retrieval" OR "memory
update" OR "memory consolidation"))) AND PUBYEAR > 2014 AND PUBYEAR <
2027 AND (LIMIT-TO(LANGUAGE, "English"))
```
