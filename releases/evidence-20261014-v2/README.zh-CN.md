# GUI 智能体记忆配套数据

对应《GUI 智能体记忆研究现状：以生命周期为中心的综述》。
版本：**evidence-20261014-v2**。DOI：https://doi.org/10.5281/zenodo.23366556。
文献截止日期：**2026-09-20**。[English](README.md)。

作者：高天寒、马锦艺、张晋，东北大学软件学院。

目录收录 **289 项工作**：250 项直接记忆研究、39 项评测或安全研究。矩阵记录 **246 项机制研究**的 **1,119 项工作—单元格赋值**，涵盖五类记忆对象和六种生命周期操作。

| 文件 | 内容 |
|---|---|
| [catalogue.csv](catalogue.csv) | 书目信息、分类、中英文对象与用途描述、采用版本及原文定位 |
| [matrix_assignments.csv](matrix_assignments.csv) | 每行一项工作—单元格赋值，通过工作标识关联目录 |
| [corpus_counts.json](corpus_counts.json) | 按公开年份、主题、类别、分析角色及矩阵单元格汇总的计数 |
| [search_runs.csv](search_runs.csv) | 五个数据库的十三组实际查询、执行日期及命中数 |
| [selection_summary.json](selection_summary.json) | 检索、去重、题名摘要筛选及纳入数量 |
| [data_dictionary.md](data_dictionary.md) | 字段含义、分类代码及计数单位 |

使用 Python 3.9 或更高版本运行 `python validate.py`，校验文件哈希、记录关联和计数。文件哈希列于 `manifest.sha256`。

许可证：[知识共享署名 4.0 国际许可协议（CC BY 4.0）](LICENSE.md)。
