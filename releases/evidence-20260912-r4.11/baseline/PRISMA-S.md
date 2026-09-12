# Search reporting crosswalk

PRISMA-S is used as a reporting checklist, not a claim of complete systematic-review compliance. Item numbering follows [Rethlefsen et al. (2021), Table 1](https://doi.org/10.1186/s13643-020-01542-z). Entries describe this artifact's records, including missing documentation.

| Item | Artifact evidence / status |
|---|---|
| 1 | Database and platform fields: `search/historical_database_runs.json`; arXiv API: `search/arxiv_update_runs.json`. |
| 2 | Historical databases were queried separately. |
| 3 | No study-registry search documented. |
| 4 | Targeted source URLs and survey sources are in the source register; this is not a complete historical browsing diary. |
| 5 | Historical protocol describes citation chaining; MobileGPT correction preserves its chaining ID. This export does not reconstruct every historical seed and edge. |
| 6 | No author/expert contact used in the current synthesis. |
| 7 | Named-source completion and scope checks are separately recorded. |
| 8 | Literal database queries and three arXiv strings are provided, with raw arXiv returns. |
| 9 | Historical date/language filters are recorded. The 2015 boundary is inherited; no stronger substantive rationale was documented. |
| 10 | Project-defined query families; no validated published search filter documented. |
| 11 | Same project's unpublished preparatory protocol; frozen original and hash supplied. |
| 12 | Three arXiv overlap queries and targeted completion; four databases not rerun. |
| 13 | Execution dates/times are retained in run records. |
| 14 | No independent search peer review documented. |
| 15 | Per-run counts supplied; repeated hits overlap. Historical raw query-hit totals: Scopus216, WoS75, ACM10, IEEE13. arXiv12 → 8 unique. These cannot be summed as unique studies. |
| 16 | Python identity matching uses DOI/arXiv identifiers, family aliases and content hashes. This export does not independently reconstruct the complete historical cross-database deduplication graph. |

The 155-family table reports bounded claim adoption, not a reconstructed PRISMA eligibility flow: 34 adopted and 121 unselected, plus 21 adopted sources outside that inventory. Per-family non-selection reasons do not establish irrelevance. Missing historical detail remains a reporting limitation.
