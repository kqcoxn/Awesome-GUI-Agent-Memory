# GUI 智能体记忆配套数据

对应《GUI 智能体记忆综述》。
版本：**evidence-20261031-v1**。[固定版本](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/releases/tag/evidence-20261031-v1)。
归档DOI：https://doi.org/10.5281/zenodo.23985925。
文献截止日期：**2026-10-31**。[English](README.md)。

作者：高天寒、马锦艺、张晋，东北大学软件学院。

目录收录 **357 项工作**：304 项直接记忆研究、53 项评测或安全研究。矩阵记录 **297 项机制研究**的 **1,498 项工作—单元格赋值**，涵盖五类记忆对象和六种生命周期操作。

| 文件 | 内容 |
|---|---|
| [catalogue.csv](catalogue.csv) | 书目信息、分类、中英文对象与用途描述、采用版本及原文定位 |
| [matrix_assignments.csv](matrix_assignments.csv) | 每行一项工作—单元格赋值，通过工作标识关联目录 |
| [corpus_counts.json](corpus_counts.json) | 按公开年份、主题、类别、分析角色及矩阵单元格汇总的计数 |
| [search_queries.csv](search_queries.csv) | 五个数据库的14组检索变体、字段、真实执行日期及记录数 |
| [selection_summary.json](selection_summary.json) | 检索、去重、题名摘要筛选及纳入数量 |
| [selection_accounting.csv](selection_accounting.csv) | 每条保留候选的去向、工作关联、判断阶段、理由及来源定位 |
| [data_dictionary.md](data_dictionary.md) | 字段含义、分类代码及计数单位 |

使用 Python 3.9 或更高版本运行 `python validate.py`，校验文件哈希、记录关联和计数。文件哈希列于 `manifest.sha256`。

许可证：[知识共享署名 4.0 国际许可协议（CC BY 4.0）](LICENSE.md)。
