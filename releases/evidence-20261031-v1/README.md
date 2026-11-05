# GUI-agent memory companion data

Companion data for *Memory in GUI Agents: A Survey*.
Version: **evidence-20261031-v1**. [Fixed release](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/releases/tag/evidence-20261031-v1).
Archive DOI: https://doi.org/10.5281/zenodo.23985925.
Publication cutoff: **31 October 2026**. [中文说明](README.zh-CN.md).

Authors: Tianhan Gao, Jinyi Ma and Jin Zhang, Software College, Northeastern University.

The catalogue contains **357 works**: 304 direct-memory studies and 53 evaluation or security studies. The matrix records **1,498 work–cell assignments** for **297 mechanism studies**, covering five memory-object layers and six lifecycle operations.

| File | Contents |
|---|---|
| [catalogue.csv](catalogue.csv) | Bibliographic information, classifications, bilingual object and use descriptions, adopted versions and source locations |
| [matrix_assignments.csv](matrix_assignments.csv) | One work–cell assignment per row, linked to the catalogue by work identifier |
| [corpus_counts.json](corpus_counts.json) | Counts by publication year, theme, category, analytical role and matrix cell |
| [search_queries.csv](search_queries.csv) | 14 consolidated query variants across five databases, with fields, actual execution dates and record counts |
| [selection_summary.json](selection_summary.json) | Search, deduplication, title/abstract selection and inclusion totals |
| [selection_accounting.csv](selection_accounting.csv) | One recorded disposition per retained candidate, with work links, decision stages, reasons and provenance |
| [data_dictionary.md](data_dictionary.md) | Field definitions, classification codes and counting units |

Run `python validate.py` with Python 3.9 or later to verify file hashes, record relationships and counts. The file hashes are listed in `manifest.sha256`.

License: [Creative Commons Attribution 4.0 International](LICENSE.md).
