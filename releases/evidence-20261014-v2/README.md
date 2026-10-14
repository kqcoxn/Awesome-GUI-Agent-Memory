# GUI-agent memory companion data

Companion data for *The State of Memory in GUI Agents: A Lifecycle-Centric Survey*.
Version: **evidence-20261014-v2**. DOI: https://doi.org/10.5281/zenodo.23366556.
Publication cutoff: **20 September 2026**. [中文说明](README.zh-CN.md).

Authors: Tianhan Gao, Jinyi Ma and Jin Zhang, Software College, Northeastern University.

The catalogue contains **289 works**: 250 direct-memory studies and 39 evaluation or security studies. The matrix records **1,119 work–cell assignments** for **246 mechanism studies**, covering five memory-object layers and six lifecycle operations.

| File | Contents |
|---|---|
| [catalogue.csv](catalogue.csv) | Bibliographic information, classifications, bilingual object and use descriptions, adopted versions and source locations |
| [matrix_assignments.csv](matrix_assignments.csv) | One work–cell assignment per row, linked to the catalogue by work identifier |
| [corpus_counts.json](corpus_counts.json) | Counts by publication year, theme, category, analytical role and matrix cell |
| [search_runs.csv](search_runs.csv) | Thirteen executed queries across five databases, with dates and hit counts |
| [selection_summary.json](selection_summary.json) | Search, deduplication, title/abstract selection and inclusion totals |
| [data_dictionary.md](data_dictionary.md) | Field definitions, classification codes and counting units |

Run `python validate.py` with Python 3.9 or later to verify file hashes, record relationships and counts. The file hashes are listed in `manifest.sha256`.

License: [Creative Commons Attribution 4.0 International](LICENSE.md).
