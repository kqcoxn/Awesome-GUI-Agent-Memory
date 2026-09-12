# GUI/Computer-Use Agent 记忆 Systematic Mapping 协议

> 版本：v1.0-frozen（2026-08-31）
>
> 状态：**协议已冻结；后续阶段状态、来源可用性和偏差见 `data/systematic_mapping/` 运行清单。**
>
> 依据：[GUI-Agent记忆综述需求.md](./GUI-Agent记忆综述需求.md)
>
> 方法组合：AcademicForge `literature-review` 的系统综述七阶段流程 + ARIS `research-lit` 的多源发现、标识符去重、版本归并和原文证据追踪。

本文档是可冻结、可复核的 systematic mapping protocol。所有结果数、论文清单、效应数据和领域结论均留空；任何后续改动必须进入 deviation log，不得回填为“预先规定”。

## 1. 研究问题与分析单位

### 1.1 研究问题

| ID | 研究问题 | 主要编码轴 |
|---|---|---|
| RQ1 | 该领域在年份、发表状态、平台、任务和长程设置上如何分布？ | 年份、证据成熟度、Web/Mobile/Desktop/Cross-app、任务、horizon |
| RQ2 | GUI Agent 保存什么，以及跨越何种时间范围？ | 内容、任务内/跨任务/跨会话记忆 |
| RQ3 | 记忆如何表示与存放？ | 文本、结构、图、程序/技能、视觉、向量、潜变量、混合表示；prompt/外部存储/参数 |
| RQ4 | 记忆如何形成、写入、检索、更新、压缩、剪枝、修复与遗忘？ | lifecycle、触发条件、算法、读写策略 |
| RQ5 | 记忆如何参与感知、规划、动作、验证和恢复？ | pipeline stage、输入输出关系、失效传播 |
| RQ6 | 实验和 benchmark 实际测量了哪些记忆能力，能否支持方法主张？ | 研究设计、基线、消融、指标、样本量、统计与质量评价 |
| RQ7 | 已报告的成本、迁移、鲁棒性、失效和安全风险是什么？ | token/时延/存储成本、泛化、failure、安全与攻击 |

### 1.2 分析单位

- `record`：一次数据库命中；仅用于检索和 PRISMA 计数。
- `work_family`：同一工作的预印本、workshop、会议、期刊等版本集合；mapping 计数默认以此为单位。
- `study`：一个可独立解释的实验或分析单元。同一 `work_family` 只有在新增研究问题、数据集或实质性实验使结论不可合并时，才拆成多个 `study`。
- `claim`：一个由原文页码/章节/表/图定位支持的最小证据单元。

版本不得被当作独立研究重复计数；论文中的多个实验也不得在“论文数量”统计中膨胀计数。

## 2. 可复核工作流与冻结点

| 阶段 | 操作 | 自动化门槛 | 产物 |
|---|---|---|---|
| 0. Scope freeze | 冻结 RQ、时间窗、语种、纳排与分析单位 | 登记 protocol 版本；不中途等待人工签字 | 本协议、deviation log |
| 1. Pilot | 对每个主检索族做语法、结果量和种子召回诊断 | 自动记录诊断；不进行人工逐条复核 | pilot log、检索式 v1 |
| 2. Search freeze | 将每个数据库的最终原样检索式、界面/API、过滤器冻结 | 所有数据库完成语法验证 | search log |
| 3. Retrieval | 执行主数据库检索；补充来源与主检索分开记账 | 原始导出只读；文件计算 SHA-256 | RIS/BibTeX/CSV/JSON 原始导出 |
| 4. Dedup | 先书目去重，再建立版本家族 | 精确标识符自动合并；模糊项进入最终复核队列但不中断 | record、version、decision logs |
| 5. Screening | title/abstract 与 full text 两阶段自动筛选 | 输出 `include/exclude/provisional_include`、依据和不确定性标记 | screening log、provisional PRISMA counts |
| 6. Chaining | 对纳入工作做向后/向前引文追踪，最多 2 轮 | 完整一轮无新增纳入可提前停止 | citation-chaining log |
| 7. QA + coding | 自动质量评价、描述性编码、claim-level 原文定位 | 缺失填 `NR`，矛盾/低置信项进入最终复核队列 | QA 表、证据矩阵 |
| 8. Mapping | 按 RQ 汇总频次、交叉表和证据强度 | 同时给出含/不含 provisional 项的敏感性结果 | 可重建表格/图形的数据与脚本 |
| 9. Update search | 投稿前更新检索 | 使用冻结检索式；新增记录单独标批次 | update search log |
| 10. Final joint review | 成稿后集中复核语料、版本、纳排、编码、表图与措辞 | 一次性处理 review queue，随后统一重算与定稿 | final review log、定稿、最终 PRISMA |

### 2.1 自动执行与最终集中复核

- 检索、去重、筛选、质量评价、证据编码和初稿综合均连续自动执行；过程中不设置人工确认、双人筛选或人工裁决门槛。
- 每项自动决定必须记录运行标识、规则/依据、原文 locator 和 `high/medium/low` 不确定性。不得用模型自报置信度替代可检查依据。
- 明确满足规则的记录写 `include` 或 `exclude`；边界不清、元数据冲突、模糊版本、证据定位不足的记录写 `provisional_include` 或相应 review flag，默认保留以减少假阴性。
- 初稿表图同时报告主结果和排除 provisional 项的敏感性结果，不把 provisional 证据写成确定结论。
- 成稿后生成一次性 final review bundle，集中包含全文排除清单、模糊版本家族、低置信编码、数值结果、claim locator、证据强度和对应稿件句子。
- 最终共同复核完成后，锁定纳排和版本关系，重算 PRISMA、表图与结论；该轮以前的计数均标记 `provisional`。

### 2.2 Protocol deviation log

任何冻结后的变化先登记、后执行；不得根据已看到的效果方向修改标准。

| deviation_id | date | stage/clause | change | reason | outcome-blind? | expected impact | final_review_status |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## 3. 数据库与来源角色

### 3.1 主数据库

主数据库形成可重复的 identification 集合。若机构无权限，必须登记为 protocol deviation，不能静默用 Web 搜索替代。

| 来源 | 角色 | 覆盖重点 | 导出要求 |
|---|---|---|---|
| Scopus | 主综合索引 | 跨出版社会议、期刊；便于 DOI/题名去重 | 全字段 + cited references，RIS/CSV |
| Web of Science Core Collection | 主综合索引 | 与 Scopus 互补并支持引文追踪 | Full Record + Cited References |
| ACM Digital Library | 主领域库 | HCI、Web、软件与 Agent 会议/期刊 | BibTeX/CSV；保存检索界面截图或导出说明 |
| IEEE Xplore | 主领域库 | 系统、HCI、移动端、自动化与 Agent | Citation & Abstract + DOI，CSV/RIS |

### 3.2 补充来源

| 来源 | 用途 | 能否单独形成证据 |
|---|---|---|
| arXiv API | 捕获最新预印本和版本链 | 可纳入，但必须标记 `preprint`，并核对是否已有正式版本 |
| OpenAlex | 开放元数据、DOI/机构/引文图核验 | 不凭摘要生成结论；仅作为发现与元数据源 |
| Semantic Scholar | 发现 venue-only 记录、前向引文、标识符补全 | 不采信 TLDR 或自动摘要为证据 |
| DBLP | CS 作者、会议和版本元数据核验 | 仅元数据源 |
| Google Scholar | 补充检索、前后向追踪和题名核验 | 不作为主数据库；记录查询、日期和检查结果范围 |
| Zotero/本地 `papers/`、`literature/` | 用户已有语料与注释线索 | 仍须经过相同去重、纳排和全文证据规则 |

任何 AI 驱动发现工具只返回“候选记录”。候选必须在出版者页面、arXiv、Crossref/OpenAlex 或全文首页核验题名、作者、年份、DOI/标识符后，才能进入筛选库。

## 4. 检索式

### 4.1 时间、语种与字段

- 主时间窗：`2015-01-01` 至 `2026-08-31`。不设早期 GUI Agent 为“默认相关”；仅通过向后引文追踪纳入 2015 年前直接相关的奠基研究，并标记 `date_exception=foundational`。
- 语种：English。
- 检索字段：Title、Abstract、Author Keywords/Index Terms；不以全文检索结果作为主集合，避免参考文献和模板文本造成大量噪声。
- 更新检索：投稿前使用相同式子，将上限扩展到更新检索日。

### 4.2 概念块

`A`：GUI/Computer-Use Agent 对象

```text
(
  "GUI agent*" OR "UI agent*" OR "graphical user interface agent*" OR
  "user interface agent*" OR
  "computer-use agent*" OR "computer use agent*" OR "computer-using agent*" OR
  "web agent*" OR "web navigation agent*" OR "browser agent*" OR
  "mobile GUI agent*" OR "desktop agent*" OR "OS agent*" OR
  "operating system agent*" OR "software-use agent*" OR "cross-app* agent*" OR
  (
    ("large language model*" OR LLM* OR "vision-language model*" OR VLM* OR multimodal)
    NEAR/3 agent*
    AND
    (GUI OR "graphical user interface*" OR "computer use" OR browser* OR website* OR
     Android OR smartphone* OR "mobile app*" OR desktop OR "operating system*" OR
     "software application*" OR "cross-app*")
  )
)
```

`M`：显式记忆术语

```text
(
  memor* OR "working memory" OR "short-term memory" OR "long-term memory" OR
  "episodic memory" OR "semantic memory" OR "procedural memory" OR
  "external memory" OR "experience memory" OR "memory bank" OR "memory module" OR
  "memory retrieval" OR "memory update" OR "memory consolidation"
)
```

`P`：未必使用 memory 名称、但可操作化为状态/经验保持的代理术语

```text
(
  ("task state" OR "interaction histor*" OR "action histor*" OR "observation histor*" OR
   trajector* OR "context management" OR "context compression" OR "context summar*" OR
   "skill librar*" OR "experience replay" OR "experience retriev*" OR "experience reuse")
  AND
  (store* OR persist* OR retain* OR select* OR summar* OR compress* OR retriev* OR
   recall* OR reuse* OR update* OR prune* OR forget* OR recover*)
)
```

`E`：评测、失效与安全补充族

```text
(benchmark* OR evaluat* OR ablat* OR metric* OR fail* OR error* OR robust* OR
 generaliz* OR transfer* OR secur* OR attack* OR poison* OR privacy)
```

`H`：可能不使用 memory 术语的长程/状态评测

```text
("long-horizon" OR "long horizon" OR "multi-step" OR "multistep" OR
 "state track*" OR "progress track*" OR "history-aware" OR "history dependent" OR
 "long context" OR "context length")
```

正式检索运行三个 query family，最后取并集：

```text
Q1_CORE  = A AND M
Q2_PROXY = A AND P
Q3_EVAL  = A AND (M OR P OR H) AND E
```

`Q3_EVAL` 是召回检查，不单独增加证据权重。不得加入 `NOT robot*`、`NOT cache` 等负向条件；边界噪声在筛选阶段排除，以免误删 GUI 与系统交叉研究。

### 4.3 数据库专用翻译

下列语法须先在 pilot 中验证；数据库自动改写、停用词和通配符提示必须原样记入 search log。

#### Scopus

将 `NEAR/3` 替换为 `W/3`，分别运行 Q1、Q2、Q3：

```text
TITLE-ABS-KEY((A) AND (M))
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND (LIMIT-TO(LANGUAGE, "English"))

TITLE-ABS-KEY((A) AND (P))
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND (LIMIT-TO(LANGUAGE, "English"))

TITLE-ABS-KEY((A) AND ((M) OR (P) OR (H)) AND (E))
AND PUBYEAR > 2014 AND PUBYEAR < 2027
AND (LIMIT-TO(LANGUAGE, "English"))
```

这里的 `A/M/P/H/E` 在执行时必须展开为 4.2 的完整文本；search log 保存展开后的字符串，而不是变量名。

#### Web of Science Core Collection

将 `NEAR/3` 保持为 WoS 邻近算符，分别展开：

```text
TS=((A) AND (M)) AND PY=(2015-2026) AND LA=(English)
TS=((A) AND (P)) AND PY=(2015-2026) AND LA=(English)
TS=((A) AND ((M) OR (P) OR (H)) AND (E)) AND PY=(2015-2026) AND LA=(English)
```

#### ACM Digital Library

在 Advanced Search 中选择 `Title, Abstract, or Author Keyword`，年份选 2015--2026。ACM 不稳定支持邻近算符时，将 A 中的 LLM/VLM 分支改为布尔共现：

```text
("large language model agent*" OR "LLM agent*" OR "vision-language agent*" OR
 "VLM agent*" OR "multimodal agent*")
AND
(GUI OR "graphical user interface*" OR "computer use" OR browser* OR website* OR
 Android OR smartphone* OR "mobile app*" OR desktop OR "operating system*" OR
 "software application*" OR "cross-app*")
```

该分支与 A 中的精确 Agent 短语作 OR，再分别与 M、P、`(M OR P OR H) AND E` 组合。必须保存 ACM 界面实际显示的 canonical query。

#### IEEE Xplore

在 Command Search 中将每个短语映射到 `"All Metadata":`，并用年份、语种界面过滤。例如 Q1 的结构为：

```text
(
  "All Metadata":"GUI agent" OR
  "All Metadata":"UI agent" OR
  "All Metadata":"graphical user interface agent" OR
  "All Metadata":"user interface agent" OR
  "All Metadata":"computer-use agent" OR
  "All Metadata":"web agent" OR
  "All Metadata":"web navigation agent" OR
  "All Metadata":"browser agent" OR
  "All Metadata":"mobile GUI agent" OR
  "All Metadata":"desktop agent" OR
  "All Metadata":"operating system agent" OR
  "All Metadata":"software-use agent" OR
  "All Metadata":"cross-app agent" OR
  (
    ("All Metadata":"large language model agent" OR "All Metadata":"LLM agent" OR
     "All Metadata":"vision-language agent" OR "All Metadata":"VLM agent" OR
     "All Metadata":"multimodal agent")
    AND
    ("All Metadata":GUI OR "All Metadata":"graphical user interface" OR
     "All Metadata":"computer use" OR "All Metadata":browser OR
     "All Metadata":website OR "All Metadata":Android OR
     "All Metadata":"mobile app" OR "All Metadata":desktop OR
     "All Metadata":"operating system" OR "All Metadata":"software application" OR
     "All Metadata":"cross-app")
  )
)
AND
(
  "All Metadata":memory OR "All Metadata":"working memory" OR
  "All Metadata":"long-term memory" OR "All Metadata":"episodic memory" OR
  "All Metadata":"external memory" OR "All Metadata":"memory bank" OR
  "All Metadata":"memory retrieval"
)
```

Q2/Q3 按同一字段映射展开 P/H/E。若平台限制单次 terms 数，按术语块拆分为多个有编号的子查询并取并集，禁止删词后不留记录。

#### arXiv API

使用 `all:` 字段、API 返回时间过滤和三个独立查询族；不限制 arXiv category：

```text
(all:"GUI agent" OR all:"UI agent" OR all:"graphical user interface agent" OR
 all:"user interface agent" OR
 all:"computer-use agent" OR all:"computer use agent" OR
 all:"web agent" OR all:"web navigation agent" OR all:"browser agent" OR
 all:"mobile GUI agent" OR all:"desktop agent" OR all:"operating system agent" OR
 all:"software-use agent" OR all:"cross-app agent" OR
 ((all:"large language model agent" OR all:"LLM agent" OR
   all:"vision-language agent" OR all:"VLM agent" OR all:"multimodal agent")
  AND
  (all:GUI OR all:"graphical user interface" OR all:"computer use" OR all:browser OR
   all:website OR all:Android OR all:"mobile app" OR all:desktop OR
   all:"operating system" OR all:"software application" OR all:"cross-app")))
AND
(all:memory OR all:"working memory" OR all:"long-term memory" OR
 all:"episodic memory" OR all:"external memory" OR all:"memory bank" OR
 all:"memory retrieval")
```

Q2 将第二块替换为 P 的无通配符展开；Q3 将第二块替换为 `(M OR P OR H) AND E` 的无通配符展开。时间过滤为 `submittedDate:[201501010000 TO 202608312359]`；保留 arXiv base ID 和 version ID。

### 4.4 检索审计字段

每次运行必须填写 [search_log.csv](./templates/gui_agent_memory_search_log.csv)：数据库、界面/API 版本、完整原样字符串、过滤器、时区、命中数、导出文件名、格式和 SHA-256。主检索、补充检索、引文追踪和更新检索使用不同 `search_run_id`。

## 5. 纳入与排除标准

### 5.1 纳入标准（全部满足）

| ID | 标准 | 操作化判定 |
|---|---|---|
| I1 | 文献时间与语种符合协议 | 2015--2026 English；更早文献仅限引文追踪发现且直接奠基，登记例外 |
| I2 | 是可核验的完整学术报告 | 期刊、正式会议、workshop full paper、预印本或完整 technical report；可合法获得全文 |
| I3 | 研究对象是 GUI/Computer-Use Agent | Agent 通过截图、DOM、accessibility tree 或软件状态观察并对 Web、移动、桌面、OS、软件或跨应用界面采取动作 |
| I4 | 存在 Agent 决策闭环 | 系统至少涉及感知/状态、规划/选择、GUI 动作之一，且非纯离线界面理解 |
| I5 | 存在可识别的记忆能力 | 信息跨越当前瞬时观察被保留，并在后续感知、规划、动作、验证、恢复或经验复用中被读取/评价 |
| I6 | 提供与 GUI 记忆相关的证据 | 方法细节、实验、benchmark、failure analysis、安全/攻击分析至少一种，且能从全文定位 |

### 5.2 证据分层

- `primary_method`：提出/比较 GUI Agent 记忆机制并有可提取证据。
- `benchmark_analysis`：直接评价记忆能力、长程状态、失败、安全或攻击。
- `secondary_context`：综述/position paper，仅用于检索补漏、术语和已有综述对比，不与 primary study 混合计数。
- `background_only`：通用 Agent memory 或相邻领域，只能用于背景，不进入核心 evidence matrix。

### 5.3 排除代码与优先级

全文排除必须按下表从上到下选择一个主原因；其他原因可放 notes。

| 优先级 | Code | 主排除原因 |
|---:|---|---|
| 1 | X01 | 撤稿、withdrawn，或无法确认其有效版本 |
| 2 | X02 | 非完整学术报告、日期/语种不符且无预注册例外 |
| 3 | X03 | 经合法渠道仍无法取得足以判定和编码的全文 |
| 4 | X04 | 不是 GUI/Computer-Use 场景 |
| 5 | X05 | 没有执行 GUI 动作的 Agent 决策闭环 |
| 6 | X06 | 无可识别记忆：只使用当前屏幕、一般 prompt 或未受控的完整上下文 |
| 7 | X07 | 无 GUI-specific 方法、实验、benchmark、失效或安全证据 |
| 8 | X08 | 仅训练数据/轨迹收集，推理时不复用且不评价记忆 |
| 9 | X09 | 仅视觉理解、元素定位或 grounding，无跨时状态保持 |
| 10 | X10 | 仅 KV cache、推理服务/系统加速，且与 Agent 决策信息无关 |
| 11 | X11 | 仅物理机器人/具身环境，GUI 子任务证据不可分离 |

重复记录不是全文排除原因，使用 `DUP_RECORD`；同一工作的非 canonical 版本使用 `MERGED_VERSION`。二者单列 PRISMA 计数。

### 5.4 边界案例

- 将完整历史放入 prompt：只有在保留、选择、压缩、检索或更新策略被明确设计/评价时纳入；普通输入拼接排除。
- RAG：检索任务状态、GUI 证据或经验时纳入；只检索通用事实知识时不作为核心记忆研究。
- 技能/程序库：在后续 GUI 任务被选择和执行时纳入；仅离线生成、没有复用证据时排除。
- 轨迹作为训练集：只有推理阶段检索/复用，或研究明确评价记忆能力时纳入。
- 通用 Agent memory：只有 GUI 子实验可独立提取时进入核心语料，否则记为背景。

## 6. 去重与版本归并规则

### 6.1 书目记录去重

按以下顺序执行；每一步记录匹配依据和保留记录：

1. DOI：去掉 `https://doi.org/`、转小写、去首尾空白后精确匹配。
2. arXiv：按 base ID 匹配，版本号 `vN` 另存。
3. 其他稳定 ID：PMID、OpenAlex Work ID、Semantic Scholar Corpus ID、DBLP key。
4. 题名精确：Unicode NFKC、casefold、移除标点/HTML、合并空白后匹配，并核对第一作者与年份（允许 online/正式出版相差 1 年）。
5. 题名模糊：token/Jaro-Winkler 相似度 `>= 0.95` 只生成候选；流程中不得据此自动删除，写入 `provisional_duplicate` 等待成稿后的集中复核。

记录合并时采用字段级 provenance：DOI/正式 venue 优先 Crossref/出版者，arXiv PDF URL 优先 arXiv，引用数只保存来源与抓取日期，不作为质量分。

合并后必须逐条解析 DOI，并核对解析页面的题名、作者与版本；DOI 解析成功但元数据不匹配时不得自动覆盖，标记 `metadata_conflict` 进入最终复核队列。

### 6.2 同一工作多版本

满足任一强规则时自动归为同一 `work_family`；仅满足两项或以上弱规则时标记 `provisional_same_work`，在初稿中同时报告合并/不合并的敏感性计数，成稿后再集中确认：

- 强规则：arXiv `journal-ref`/DOI 明示对应；出版者页面明示 extended version；作者明确版本关系。
- 弱规则：规范化题名高度相似；作者核心集合重合；方法/系统名相同；摘要、benchmark 和主要结果显著重合。

Canonical 版本优先级：已更正的正式期刊扩展版 > 正式会议 full paper > peer-reviewed workshop full paper > 最新完整预印本。优先级不是盲目覆盖：若早期版本含 canonical 版未保留的独有实验，保留该版本 locator，但综合时仍只计一个 `work_family`。

若后续版本提出新的 RQ、加入实质性新系统或独立实验，使结论不能合理合并，可在同一 `work_family` 下拆为多个 `study_id`，并在 [version_log.csv](./templates/gui_agent_memory_version_log.csv) 写明 `unique_evidence` 与拆分理由。

## 7. 质量评价表

### 7.1 评分规则

- 每项 `1`：完整满足且填写原文 locator；`0.5`：部分满足；`0`：未满足或无法核验。
- `NA` 仅限依据评分规则可判定为客观不适用，并记录理由；有歧义则标记待最终复核。少于 7 个适用条目的研究标记 `noncomparable`。
- 归一化分数：`sum(scores) / applicable_items`。
- `High >= 0.75`；`Moderate = 0.50--0.749`；`Low < 0.50`。
- 质量分不作为机械排除阈值；Low 研究保留在 map 中，但不得单独支撑强结论。
- 发表状态/证据成熟度单独编码，不与 venue 声望、作者声望或引用数混入质量分。

| ID | 质量问题 | 1 分判据 | 0.5 分判据 | 0 分判据 |
|---|---|---|---|---|
| Q1 | 研究问题和 memory claim 是否明确？ | 明确目标、对象与可检验主张 | 目标明确但记忆主张含混 | 无法辨认 |
| Q2 | 记忆机制是否足以复现/比较？ | 内容、表示、写入、读取/更新关键步骤完整 | 仅部分机制细节 | 只有模块名/宣传性描述 |
| Q3 | GUI 环境、任务和长程设置是否充分描述？ | 环境、动作空间、任务、horizon/episode 均可核验 | 缺一至两项 | 场景无法重建 |
| Q4 | 比较是否能归因于记忆？ | 匹配基线/消融控制主要混杂 | 有基线但控制不足 | 无相关比较却声称增益 |
| Q5 | 指标是否对应所声称的记忆能力？ | task 指标与 memory-specific construct 对齐 | 仅间接代理且有限论证 | 指标不能支持主张 |
| Q6 | 实验执行与不确定性是否透明？ | 运行数/样本、设置、方差/区间或等价透明信息齐全 | 部分报告 | 单点结果且协议不明 |
| Q7 | 结果能否追溯到表、图、日志或逐例证据？ | 所有主结果有 locator 与分母/单位 | 部分主结果可追溯 | 只有无定位叙述 |
| Q8 | 是否检验鲁棒性、迁移或边界条件？ | 多任务/环境/模型或明确压力测试 | 单一有限检查 | 未检查却泛化表述 |
| Q9 | 是否分析失败、混杂和局限？ | 系统 failure analysis/threats | 简短但具体 | 缺失或明显回避 |
| Q10 | 是否提供复核资产？ | 代码、数据/任务、配置/日志或充分补充材料 | 只开放部分 | 无资产且细节不足 |

正式评分填写 [quality_assessment.csv](./templates/gui_agent_memory_quality_assessment.csv)。证据成熟度使用：`P4_peer_reviewed_journal`、`P3_peer_reviewed_conference`、`P2_peer_reviewed_workshop`、`P1_preprint_or_unreviewed`；该标签仅限定措辞，不改变 QA 分。

## 8. 证据编码矩阵

正式数据填写 [evidence_matrix.csv](./templates/gui_agent_memory_evidence_matrix.csv)。多选值使用 `|` 分隔；`NR` 表示原文未报告，`NA` 表示不适用，空值只允许尚未编码。

### 8.1 字段组与受控值

| 字段组 | 核心字段 | 受控值/决策规则 |
|---|---|---|
| 标识与溯源 | `study_id`, `work_family_id`, `version_id`, DOI/arXiv, `full_text_sha256` | 每个 claim 必须反向定位到具体版本全文 |
| 发表状态 | `publication_status`, `evidence_maturity` | journal/conference/workshop/preprint/technical_report；P1--P4 分开 |
| GUI 场景 | `platform`, `observation_interface`, `action_interface`, `task_domain` | platform: web/mobile/desktop_os/software/cross_app/mixed |
| 长程属性 | `horizon_definition`, `episode_length` | 优先原文定义与数值；不得由自动提取器臆测“长程” |
| 记忆显式性 | `memory_explicitness` | named / operational_proxy / evaluation_target |
| 时间范围 | `temporal_scope` | within_task / cross_task / cross_session / lifelong / mixed |
| 保存内容 | `memory_content` | goal、plan、action、observation、screenshot、DOM/A11y、task_state、tool_output、error、recovery、preference、demonstration、skill/program、fact、latent |
| 表示与位置 | `representation`, `storage_location` | raw_text/summary/slot/KV/graph/vector/trajectory/program/visual/latent/hybrid；prompt/external/parameter/hybrid |
| 形成与写入 | `formation_method`, `write_trigger` | append/extract/summarize/reflect/distill/learn/manual；step/event/error/success/episode/task/user/learned |
| 检索与更新 | `retrieval_trigger`, `retrieval_method`, `update_policy`, `forgetting_policy` | always/query/event/failure/learned；recency/similarity/rule/graph/planner/learned/hybrid |
| 使用阶段 | `pipeline_stage` | perception/planning/action/verification/recovery/learning |
| 实验设计 | `study_design`, `benchmark`, `baseline`, `ablation`, `sample_size` | 原样记录；无报告写 NR，不得补估 |
| 结果 | `metric`, `effect_direction`, `effect_value`, `uncertainty` | 数值、单位、分母、版本和 comparator 必须同一 locator 可核对 |
| 代价与风险 | `cost`, `transfer`, `failure_mode`, `safety_risk` | 区分作者报告与自动归纳 |
| Claim 证据 | `author_claim_quote`, `evidence_type`, `evidence_locator`, `extractor_interpretation` | locator 至少为页码+章节，表/图证据加编号；自动摘要不能作 locator |
| 支持强度 | `support_status`, `qa_score`, `independence_notes` | supported/partial/contradicted/not_tested；同一工作版本不算独立支持 |
| 执行与最终复核 | `extraction_run_id`, `uncertainty_flag`, `final_review_status` | 中间自动执行；所有主分类、数值和强结论在成稿后的 final review bundle 中统一复核 |

### 8.2 空白矩阵预览

| study_id | work_family_id | platform | temporal_scope | memory_content | representation | write/retrieve/update | pipeline_stage | benchmark/metric | claim + locator | QA | review |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |

一条记录只编码一个最小 claim；同一 study 的不同指标、不同 comparator 或相互冲突结果分成多行，以免把“方法存在”和“效果成立”混为一体。

## 9. 综合与结论约束

- 描述性 mapping 按 `work_family` 去重；实验设计/效应可按 `study_id` 展开，并同时报告 family 数。
- 不因高引用、高级别 venue 或作者知名度跳过质量评价。
- 不把任务成功率自动解释为“记忆能力”；只有实验设计能隔离/测量记忆构念时才编码为 memory evidence。
- 异质 benchmark、模型、任务和指标不直接合并效应；无预先定义的可比组时只做方向性/分层映射。
- `convergent` 强结论要求至少 3 个独立 `work_family`，其中至少 2 个 QA 为 Moderate/High、至少 1 个 P3/P4 正式 full paper，且无未解决的高质量反证。
- 2 个独立 family 可写 `supported`；单篇、仅预印本或 Low QA 只能写 `preliminary`；方向不一致写 `mixed`。
- 所有结论必须能由 evidence matrix 重建；没有 locator 的内容不得进入结果和讨论。
- 最终集中复核前，稿件、PRISMA 数字和所有结论均带 `provisional` 状态；最终复核后的修改必须触发全量重算，禁止只改正文不改矩阵。

## 10. 审计文件与命名

建议执行阶段使用以下只增不改的目录：

```text
data/systematic_mapping/
  protocol/
  raw_exports/
  normalized/
  screening/
  fulltext_manifest/
  coding/
  synthesis/
```

命名规则：`SRC-{DATABASE}-{YYYYMMDD}-{NN}`、`REC-{NNNNNN}`、`WF-{NNNNN}`、`ST-{NNNNN}`、`CL-{NNNNNN}`。所有原始导出和纳入全文只登记路径、合法来源与 SHA-256；公开补充材料不得包含受版权限制的全文。

模板清单：

- [gui_agent_memory_search_log.csv](./templates/gui_agent_memory_search_log.csv)
- [gui_agent_memory_screening_log.csv](./templates/gui_agent_memory_screening_log.csv)
- [gui_agent_memory_version_log.csv](./templates/gui_agent_memory_version_log.csv)
- [gui_agent_memory_quality_assessment.csv](./templates/gui_agent_memory_quality_assessment.csv)
- [gui_agent_memory_evidence_matrix.csv](./templates/gui_agent_memory_evidence_matrix.csv)
- [gui_agent_memory_final_review_queue.csv](./templates/gui_agent_memory_final_review_queue.csv)

`final_review_queue.csv` 是成稿后共同复核的唯一入口；各阶段通过 `item_type + item_id` 把待确认项汇总到此表，不在中间阶段单独请求人工决定。

## 11. 当前明确未做事项

- 未执行任何数据库查询，也没有结果条数。
- 未列出或评价任何具体论文。
- 未填写 DOI、作者、venue、实验数值或结论。
- 未生成 PRISMA 数字；流程图只能在检索和筛选日志锁定后生成。
- 未进行 taxonomy 频次统计、benchmark 比较或研究缺口判断。
