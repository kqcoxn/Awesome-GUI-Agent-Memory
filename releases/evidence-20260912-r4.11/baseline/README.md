# GUI-agent memory: evidence artifact

Companion evidence for **Memory for GUI Agents: A Unified Architecture of Lifecycles and State Layers**. Search coverage is fixed at **8 September 2026**. This is a frozen, selective framework synthesis with a traceable evidence map; its counts do not estimate field prevalence. This repository is public under its owner's personal GitHub account and is not anonymous.

## Contents and units

- `claims.json`: 75 core claims (44 mechanism, 19 construct/protocol, 2 comparative effect, 10 survey organization), with original passages, paraphrases, scope, page, version, source URL and matrix cells.
- `source_registry.csv`: 192 source locations, including version/role overlap; 55 locations supply the core claims. Original PDFs are identified by hash, not redistributed.
- `family_disposition.csv`: all 155 inherited candidate families, with individual disposition and reason. **34 adopted + 121 not selected**. Non-selection is not a scope exclusion.
- `adopted_outside_155.csv`: 21 further core sources; **34 + 21 = 55**.
- `capability_matrix.csv`: 1,650 source–cell rows, 122 supported and 1,528 unassessed; 118 supported primary and four supported auxiliary assignments. Operation counts are W21, P24, R21, U29, V9, F18.
- `search/`: literal historical queries and execution counts, three arXiv query strings, raw returned XML and hit lists, and protocol provenance. Historical database searches were **not rerun** for the framework synthesis.
- `validation/targeted_scope_checks.csv`: six named in-scope works cited as contextual examples outside the 75 core claims. MobileGPT's historical metadata-based exclusion is recorded as a false negative; the original screening record is not rewritten.
- `validation/`: reproducible sample and blank human review form; separately attributed external bibliographic spot-check; official arXiv identity checks of three questioned references.
- Comparison tables, effect records, aliases, boundary decisions and bibliographies retain their separate evidence roles. The supporting bibliography contains methodology and contextual citations outside the 55 core sources.

## Verification status

Extraction, coding, source checks and bilingual drafting were assisted by OpenAI Codex (LLM), with Python for parsing, identity/hash checks, schemas and table construction. Local PDF text and page renderings supported source checks. These are **not independent human or dual-reviewer adjudication**. Exact model revisions and per-claim prompts were not retained and cannot be reconstructed reliably.

The 15/75 claim sample is prepared but **human review is pending**. No claim-level human error rate or inter-reviewer agreement is available. The fixed seed is 20260908; IDs are sorted by SHA256 of `20260908:<claim_id>`, taking the first 15 without replacement. This differs from NumPy's random generator; the precise algorithm and judgement definitions are in `validation/random_sample_protocol.json`. `validate.py` reproduces the sample. Blank judgements must never be counted as correct.

The separately supplied 18-source bibliographic spot-check confirmed 15 entries (11 direct, four indirect) and left three unresolved. Its reported zero errors concerns existence/metadata/abstract-level interpretation only, and is automation-assisted. Official arXiv metadata subsequently confirmed those three identities. Neither check establishes the correctness of all page-level claims.

## Search provenance and limits

The historical protocol was an unpublished preparatory document from this same project, frozen on 31 August 2026; it was not an externally preregistered or previously published study. Its original wording is preserved byte-for-byte. Relative links inside it refer to the private project's historical layout and may not resolve here. The original search execution logs are exported with an explicit field whitelist to omit institutional access identities and session URLs; each export retains the original log's SHA256.

Historical execution: Scopus and Web of Science on 2 September, ACM on 3 September, IEEE on 2 September 2026. The inherited search window starts in 2015 as an administrative boundary; no stronger historical rationale was recorded. The current arXiv update covers 25 August–8 September 2026 and returned 12 hits, eight unique identities. Its date is an indexed-at-execution boundary, not a guarantee against indexing delay. See `PRISMA-S.md` for reporting coverage and remaining gaps.

## Reuse and rights

This package contains research annotations and limited source excerpts for verification, not third-party full texts. Bibliographic records and excerpts retain their original attribution and applicable rights; no blanket license is asserted over third-party material. No paper PDFs, credentials, account contact details, institutional access sessions or private Git history are included. Technical integrity checks do not replace research validation.

Run `python3 validate.py` with the Python standard library. `manifest.sha256` fixes file identities for this release. Revisions require a new version; search coverage remains fixed.
