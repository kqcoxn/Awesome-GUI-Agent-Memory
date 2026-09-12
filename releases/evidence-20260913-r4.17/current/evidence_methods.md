# Evidence collection and coding

## Scope and retrieval

The survey examines retained state and experience in GUI agents. Source selection supports comparisons of retained objects, consumption paths, maintenance operations, and evaluation conditions. Publication coverage extends through 10 September 2026.

Scopus, Web of Science, IEEE Xplore, and ACM Digital Library searches ran on 2–3 September 2026 with a 2015–2026 publication-year filter. Scopus, Web of Science, and ACM applied English-language filtering during retrieval; IEEE records applied the language restriction during source selection. The wide date window includes foundations preceding LLM-driven GUI systems. Passage-level analysis uses English-language sources.

The three arXiv query families cover submission dates from 25 August to 8 September 2026. Q1, Q2, and Q3 returned 3, 6, and 3 records respectively: 12 hits and 8 distinct records. The focused `GUI memory` search covers latest-submission dates from 2 to 10 September 2026, searches all fields, includes cross-listed records, and returns 6 records. One targeted source joins this set; three sources support qualitative comparisons. Exact queries, execution times, returned records, and selection decisions are included in the package.

| Unit | Count | Interpretation |
|---|---|---|
| Database query hits | 216 / 75 / 13 / 10 | Scopus / WoS / IEEE / ACM; queries overlap |
| arXiv query-family hits | 12 / 8 | Returned / distinct records |
| Focused retrieval | 6 + 1 | Keyword-search records plus one targeted source |
| Candidate families | 155 | 34 selected for claims; 113 not selected for claims; 8 contextual candidates |
| Coded sources | 55 | 34 from the candidate inventory and 21 outside it |
| Source roles | 33 + 22 | Primary mechanisms and auxiliary roles |
| Claims | 75 | Source-located statements, each with an explicit scope |
| Other mechanism comparisons | 24 | Version-specific comparisons outside the coded claim set |
| Manuscript references | 91 | 55 coded sources and 36 other cited works |

Selection is purposive. Counts describe this collection. Historical records provide broad non-selection categories; detailed individual exclusion reasons and the complete cross-database deduplication chain are unavailable. Query attempts that returned HTTP errors or timed out have no hit count. These outcomes are recorded separately from successful searches.

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
