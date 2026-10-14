# GUI 智能体记忆分类目录

[English](CATALOGUE.md) · **简体中文** · [精选阅读](README.zh-CN.md#shelves) · [CSV 数据](catalogue.csv)

文献覆盖截止 **2026-09-20**；目录整理于 **2026-10-14**。按工作去重共 **289 项**：250 项直接记忆研究、39 项相关评测／安全研究。

收录范围为 LLM/VLM 参与 GUI 决策、操作或记忆处理的研究，依据原文中的保留对象及后续 GUI 用途选材。目录按框架贡献组织，允许存在覆盖遗漏。每项有原文分类依据；分类核验不代表所有效果数字或机制细节均已完成主张级审计。

下列主题用于阅读导航，每项只列一次；主题分区与直接记忆／评测安全类别是两种不同的组织口径。保留对象与用途是综述者综合描述。年份取首次公开日期，可能早于正式发表年份。CSV 保留稳定标识、类别、采用版本、双语描述和原文定位；原文定位沿用核验记录的语言。

[配套数据](README.zh-CN.md#evidence) 保存本目录、逐格赋值、统计汇总、实际检索式及筛选数量汇总。精选阅读还包含目录范围之外的背景综述。

[视觉历史 (17)](#visual) | [界面结构与导航 (48)](#interface) | [任务状态与经验 (90)](#state) | [工作流与技能 (83)](#skill) | [用户上下文与个性化 (14)](#user) | [基准与评测 (22)](#evaluation) | [安全与可靠性 (15)](#security)

## 年度分布

| 首次公开年份 | 工作数 |
|---|---:|
| 2023 | 12 |
| 2024 | 40 |
| 2025 | 103 |
| 2026* | 134 |

*2026 年截至 9 月 20 日。计数描述本目录选材的年份分布，每项工作只计一次；不能据此估计全领域增长率。

<a id="visual"></a>

## 视觉历史 · 17

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2026 | <a id="mem_fc9f615907"></a>[AnchorGUI: Asymmetric Memory for Dual-Scale Learning in GUI Navigation](https://arxiv.org/abs/2609.15457v1) | 异常转移截图与预测误差 | 后续手机GUI导航 |
| 2026 | <a id="mem_fdf6f62b8b"></a>[AQuaUI: Visual Token Reduction for GUI Agents with Adaptive Quadtrees](https://arxiv.org/html/2605.19260v1) | 前序 GUI 截图及压缩签名 | 后续 GUI 视觉定位和动作 |
| 2024 | <a id="mem_8eff266b2d"></a>[Aria-UI: Visual Grounding for GUI Instructions](https://arxiv.org/html/2412.16256v2) | 历史 GUI 截图和动作 | 后续网页/手机 GUI 控件定位 |
| 2025 | <a id="comem"></a>[Auto-scaling Continuous Memory for GUI Agent](https://arxiv.org/abs/2510.09038v1) | 历史GUI截图与操作轨迹 | 陌生界面长程任务 |
| 2026 | <a id="mem_5dc012329c"></a>[Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction](https://arxiv.org/html/2606.29445v1) | 视频教程关键帧集合 | 后续视频指导 GUI 动作 |
| 2026 | <a id="gui_wf_0333"></a>[CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](https://arxiv.org/abs/2608.22577v2) | 归档的高保真视觉观测 | 为后续 GUI 决策恢复视觉证据 |
| 2025 | <a id="mem_b8a7ad37fe"></a>[GUI-KV: Efficient GUI Agents via KV Cache with Spatio-Temporal Awareness](https://arxiv.org/html/2510.00536v1) | 历史 GUI 视觉 token KV 缓存 | 后续 GUI 动作预测 |
| 2026 | <a id="gui_wf_0235"></a>[MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652v1) | 任务相关界面事件与历史轨迹 | 长程GUI操作 |
| 2025 | <a id="gui_wf_0078"></a>[PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents](https://arxiv.org/abs/2510.00413v2) | 历史截图、观测线索及动作结果 | 手机及网页GUI导航 |
| 2026 | <a id="mem_c1851f8f2f"></a>[Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/html/2603.26041v1) | 历史截图及视觉嵌入 | 后续GUI导航推理 |
| 2024 | <a id="mem_721a3ba219"></a>[Seeing is Believing: Vision-Driven Non-Crash Functional Bug Detection for Mobile Apps](https://arxiv.org/html/2407.03037) | 连续截图与测试进度 | 检测跨 GUI 转移的非崩溃错误 |
| 2025 | <a id="mem_37bd08fb78"></a>[SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/html/2512.22322v1) | 任务完成证据截图 | 移动GUI任务自验证 |
| 2026 | <a id="mem_99368811d3"></a>[STaR-KV: Spatio-Temporal Adaptive Re-weighting for KV Cache Compression in GUI Vision-Language Models](https://arxiv.org/html/2606.01790v1) | 先前截图视觉token缓存 | 后续GUI动作推理 |
| 2026 | <a id="mem_29f8342932"></a>[Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory](https://arxiv.org/abs/2604.07863v1) | 截图、超文本标记语言（HTML）、结构信号历史图 | 网页代理后续任务成功 |
| 2024 | <a id="mem_e971245432"></a>[Training a Vision Language Model as Smartphone Assistant](https://arxiv.org/html/2404.08755v1) | 过往屏幕和动作 | 手机 GUI 后续控制 |
| 2025 | <a id="mem_891f9b6c38"></a>[UI-Hawk: Unleashing the Screen Stream Understanding for Mobile GUI Agents](https://aclanthology.org/2025.emnlp-main.920.pdf) | 屏幕序列与动作历史 | 手机 GUI 下一步动作 |
| 2026 | <a id="mem_2fb8583d04"></a>[ViBR: Automated Bug Replay from Video-Based Reports using Vision-Language Models](https://arxiv.org/html/2604.19905v1) | 历史 GUI 行动视频 | 在 Android 应用重演错误 |

<a id="interface"></a>

## 界面结构与导航 · 48

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2025 | <a id="mem_db766e2179"></a>[A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants](https://arxiv.org/html/2510.06223v2) | 应用导航树和能力语义 | LLM 解释语音请求并触发后续 GUI 导航 |
| 2026 | <a id="gui_wf_0156"></a>[ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502v1) | GUI页面状态、动作模板和转移 | 在线GUI任务执行与修复 |
| 2026 | <a id="mem_5be5a7fdd4"></a>[Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution](https://arxiv.org/html/2605.28607v1) | 知识图、动作轨迹与状态差分历史 | 后续 GUI 工作流动作 |
| 2025 | <a id="mem_8c1405dbc1"></a>[Agent-SAMA: State-Aware Mobile Assistant](https://ojs.aaai.org/index.php/AAAI/article/view/40187) | 界面状态与动作转移状态机 | 跨应用移动任务的规划、核验与恢复 |
| 2026 | <a id="mem_e606dad11b"></a>[An LLM-Driven Visual Automation Script Generation Framework for Mixed-State Testing in Industrial Applications](https://journals.sagepub.com/doi/10.3233/ATDE260391) | 由 文档对象模型/OpenAPI/抽象语法树 建立的 界面 元素—后端实体关系图；历史断言通过率；LLM 判定的步骤嵌入—标签缓存。 | 后续测试步骤查询关系图并结合历史通过率选取视觉代理，生成 GUI 可视断言；缓存标签供相似步骤分类，VLM 在执行层定位交互目标。 |
| 2024 | <a id="appagentv2"></a>[AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/html/2408.11824v4) | 控件知识文档与执行摘要 | 指导后续移动界面操作 |
| 2024 | <a id="mem_e74f43e107"></a>[AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation](https://arxiv.org/html/2412.18116v3) | 应用界面文档与转移依赖 | 后续手机 GUI 操作 |
| 2023 | <a id="gui_add_autodroid"></a>[AutoDroid: LLM-powered Task Automation in Android](https://arxiv.org/abs/2308.15272v4) | 应用功能及导航知识 | 后续Android任务 |
| 2024 | <a id="mem_222e458f60"></a>[AUTONODE: A Neuro-Graphic Self-Learnable Engine for Cognitive GUI Automation](https://arxiv.org/pdf/2403.10171v2) | 网站 界面 结构知识图 | 后续网页 GUI 导航 |
| 2026 | <a id="mem_1c4d93aa53"></a>[Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts](https://arxiv.org/html/2602.02468v1) | 外部网页程序知识与执行反思 | 后续网页 GUI 操作 |
| 2026 | <a id="mem_34938daf29"></a>[Breaking the Illusion: Automated Reasoning of GDPR Consent Violations](https://arxiv.org/pdf/2512.22789v1) | 政策提取的同意目的及相关页面信息 | LLM 网页 agent 按目的导航并收集表单 |
| 2026 | <a id="mem_e7f4f362da"></a>[BugRepro: enhancing android bug reproduction with domain-specific knowledge integration](https://arxiv.org/pdf/2505.14528v2) | 已标注 bug 报告步骤及应用 界面 转移图 | LLM 据检索示例抽取重现步骤，并据 界面 图导航应用 |
| 2025 | <a id="mem_8bd245235d"></a>[Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/html/2505.14141v1) | 应用状态与转移知识库 | 后续手机 GUI 路径执行 |
| 2026 | <a id="mem_3cd49de261"></a>[ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](https://arxiv.org/html/2601.07262v3) | 网页专家知识与动态更新经验 | 后续浏览器 GUI 操作 |
| 2026 | <a id="mem_a1874e29bf"></a>[Curiosity Driven Knowledge Retrieval for Mobile Agents](https://arxiv.org/pdf/2601.19306v1) | 应用功能、参数、界面映射和交互模式的 AppCards | DroidRun 手机 GUI 决策和多步操作 |
| 2026 | <a id="mem_6acef98d3f"></a>[From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants](https://arxiv.org/pdf/2607.11387v1) | GUI 测试派生的能力描述、意图映射及动作计划 | 后续语音请求匹配到应用 GUI 操作 |
| 2025 | <a id="mem_c0036ba3fe"></a>[From Redundancy to Efficiency: Exploiting Shared UI Interactions towards Efficient LLM-Based Testing](https://tskghs17.github.io/papers/wang2025testweaver.pdf) | 语义注释的 界面 转移图、共享交互与 多模态大语言模型 产生的动作缓存 | 同一交互在后续手机 GUI 测试案例中复用操作 |
| 2025 | <a id="mem_2d7d77d00e"></a>[From User Interface to Agent Interface: Efficiency Optimization of UI Representations for LLM Agents](https://arxiv.org/html/2512.13438v1) | 界面 转换程序 | 后续 LLM 网页 GUI 决策输入 |
| 2025 | <a id="mem_6167a7446c"></a>[Go-Browse: Training Web Agents with Structured Exploration](https://arxiv.org/html/2506.03533v2) | 网页图、探索边界和动作历史 | 后续浏览器 GUI 探索 |
| 2026 | <a id="gui_wf_0373"></a>[Graph-Structured Persistent Memory for Efficient LLM-Based Computer Use Agents](https://doi.org/10.3390/axioms15060415) | GUI 状态与操作路径 | 复用桌面 GUI 子任务 |
| 2026 | <a id="graphdroid"></a>[GraphDroid: Asynchronous LLM-Based Mobile App GUI Testing via History-Aware Exploration and Hybrid Intent Fulfillment](https://arxiv.org/html/2609.10031v1) | 界面 转移图和功能簇记忆 | 后续手机 GUI 测试 |
| 2026 | <a id="mem_86cae9112f"></a>[GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph](https://arxiv.org/html/2601.17418v1) | 应用页面功能与转移知识图 | 后续手机 GUI 任务 |
| 2025 | <a id="mem_f0e871bcdb"></a>[Grounded Test-Time Adaptation for LLM Agents](https://arxiv.org/html/2511.04847v1) | 网页环境转移规律 | WebArena新站点任务执行 |
| 2025 | <a id="mem_80ec58d665"></a>[GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/) | 界面状态—动作—结果知识 | 目标移动应用中的导航与操作 |
| 2025 | <a id="mem_aceb660bb5"></a>[Improving Language Agents through BREW: Bootstrapping expeRientially-learned Environmental knoWledge](https://arxiv.org/html/2511.20297v2) | 轨迹经验知识文档 | 后续 OSWorld 电脑 GUI 操作 |
| 2024 | <a id="mem_655ee4e4a6"></a>[Improving Web Element Localization by Using a Large Language Model](https://arxiv.org/pdf/2310.02046v1) | 旧版网页目标元素属性 | 新版本测试中定位对应 GUI 元素 |
| 2025 | <a id="mem_35d568c4f4"></a>[InfraMind: A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management](https://arxiv.org/html/2509.13704v1) | 工业 GUI 元素知识与成功流程 | 后续工业 GUI 自动化 |
| 2025 | <a id="mem_a6fb9e1b79"></a>[KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.274/) | 应用界面转移图 | 规划移动界面导航路径 |
| 2025 | <a id="mem_9d976f07bc"></a>[KuiTest: Leveraging Knowledge in the Wild as GUI Testing Oracle for Mobile Apps](https://tskghs17.github.io/papers/hu2025kuitest.pdf) | 图标库及对应功能说明 | 对当前移动 GUI 控件预测功能并验证操作后响应 |
| 2024 | <a id="mem_b51478fe80"></a>[Large Language User Interfaces: Voice Interactive User Interfaces Powered by LLMs](https://arxiv.org/html/2402.07938v2) | 界面 组件元描述、状态与注释树 | 后续语音驱动 GUI 操作 |
| 2026 | <a id="mem_a80fc6b0ea"></a>[Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration](https://arxiv.org/abs/2605.31365v1) | 已探索网页状态、URL、动作转移和覆盖标签 | 利用探索图规划未覆盖节点并回溯，驱动后续网页探索操作 |
| 2025 | <a id="mem_4c210c8eab"></a>[LLM-Explorer: Towards Efficient and Affordable LLM-based Exploration for Mobile Apps](https://arxiv.org/html/2505.10593v1) | 应用探索知识 | 指导移动应用后续探索动作 |
| 2025 | <a id="mem_26e88d6b7a"></a>[LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance](https://tmliu06.github.io/pdfs/llmdroid-fse2025.pdf) | 已访问页面与功能摘要 | 指导后续手机 GUI 测试 |
| 2023 | <a id="mem_7e656ec648"></a>[Make LLM a Testing Expert: Bringing Human-Like Interaction to Mobile GUI Testing via Functionality-Aware Decisions](https://arxiv.org/html/2310.15780v1) | 测试过程功能知识 | 指导后续手机 GUI 探索 |
| 2025 | <a id="mem_9c79ad23f3"></a>[MapAgent: Trajectory-Constructed Memory-Augmented Planning for Mobile Task Automation](https://arxiv.org/abs/2507.21953v1) | 页面布局与功能快照 | 移动GUI任务规划及执行 |
| 2025 | <a id="mem_cc179f2ee3"></a>[PG-Agent: An Agent Powered by Page Graph](https://arxiv.org/html/2509.03536v1) | 页面转移图与界面指南 | 规划未见过的 GUI 场景 |
| 2025 | <a id="mem_a7d48888e2"></a>[ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps](https://tingsu.github.io/files/fse2025-ProphetAgent.pdf) | 语义 界面 转移图 | 生成可执行移动 GUI 测试路径 |
| 2026 | <a id="mem_fb8a22e354"></a>[Region4Web: Rethinking Observation Space Granularity for Web Agents](https://arxiv.org/html/2605.07134v1) | 页面区域功能摘要 | 后续网页动作 |
| 2026 | <a id="mem_8d2b4314ae"></a>[Reproducing UI contexts described in app reviews with large language models](https://tmliu06.github.io/pdfs/ui-contexts-asej2026.pdf) | 预探索的 界面 状态库 | 定位并到达评论所述手机界面 |
| 2026 | <a id="mem_ce89d4f027"></a>[Social-Annotate: Self-Healing Browser Extension to Annotate and Collect Social Media Data](https://arxiv.org/html/2607.01460v1) | 目标界面选择器及结构变化 | 后续浏览器插件操作 |
| 2025 | <a id="mem_96957a7efd"></a>[Temac: Multi-Agent Collaboration for Automated Web GUI Testing](https://arxiv.org/html/2506.00520v1) | 界面状态转移图与覆盖记录 | 网页GUI定向测试 |
| 2026 | <a id="mem_b49a013559"></a>[Testing Text Input Components of Web Applications Based on Large Language Models; &#91;基于大语言模型的 Web 文本输入组件测试方法&#93;](https://www.ejournal.org.cn/rc-pub/front/front-article/download/153611942/lowqualitypdf/Testing%20Text%20Input%20Components%20of%20Web%20Applications%20Based%20on%20Large%20Language%20Models.pdf) | 控件上下文与测试结果 | Web 表单输入测试 |
| 2026 | <a id="mem_f1e4fb7771"></a>[UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided GUI Agents](https://arxiv.org/html/2605.29534v1) | 应用界面状态与转移图 | 后续移动GUI任务 |
| 2025 | <a id="mem_7fbe083c3a"></a>[UICOMPASS: UI Map Guided Mobile Task Automation via Adaptive Action Generation](https://aclanthology.org/2025.emnlp-main.1346.pdf) | 应用 界面 图与动作历史 | 移动 GUI 导航与路径修订 |
| 2025 | <a id="mem_9c52f9d28f"></a>[WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732v2) | 网页地图与交互结果 | 新网站长程导航 |
| 2026 | <a id="mem_bbe1ea2894"></a>[WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/html/2606.10423v1) | 页面层级和元素行为地图 | 后续网页任务 |
| 2024 | <a id="mem_e17bac36bb"></a>[WebMap: Improving LLM Web Agents with Semantic Search for Relevant Web Pages](https://nlp.fi.muni.cz/raslan/2024/paper5.pdf) | 预处理网页导航资源 | Web GUI 资源定位 |
| 2026 | <a id="mem_5e44ec43ce"></a>[WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements](https://arxiv.org/html/2602.11724v1) | 元素符号及跨状态依赖 | 验证 Web GUI 行为 |

<a id="state"></a>

## 任务状态与经验 · 90

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2026 | <a id="mem_cf78c6ae73"></a>[A Subgoal-driven Framework for Improving Long-Horizon LLM Agents](https://arxiv.org/html/2603.19685v1) | 交互历史与任务子目标 | 后续网页导航动作及进度判断 |
| 2023 | <a id="mem_93a681a63e"></a>[A Zero-Shot Language Agent for Computer Control with Structured Reflection](https://arxiv.org/html/2310.08740v3) | 历史动作错误与反思 | 后续 MiniWoB 网页 GUI 动作 |
| 2025 | <a id="gui_wf_0027"></a>[Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906v1) | shared task context and specialist execution state | coordinate specialist actions in desktop and mobile GUIs |
| 2026 | <a id="mem_aa54ce666c"></a>[AgentExplorer: Parallel Online Exploration for Enhancing On-Device Mobile GUI Agents](https://doi.org/10.1109/fmsys72110.2026.00011) | 探索历史、界面 分支与结果的紧凑结构化提示 | 下一步 VLM 手机 GUI 决策 |
| 2025 | <a id="mem_38af3cf8ff"></a>[Aime: Towards Fully-Autonomous Multi-Agent Framework](https://arxiv.org/html/2507.11988v2) | 任务层级、完成状态和执行反馈 | WebVoyager 网页 GUI 任务重规划 |
| 2023 | <a id="mem_4832b985b4"></a>[AllTogether: Investigating the Efficacy of Spliced Prompt for Web Navigation using Large Language Models](https://arxiv.org/html/2310.18331v1) | 网页动作历史轨迹 | 后续 HTML 网页元素操作 |
| 2024 | <a id="mem_4dbf6df898"></a>[Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://arxiv.org/html/2403.02713v2) | 动作描述与上一动作结果 | 下一步手机 GUI 动作 |
| 2026 | <a id="gui_wf_0179"></a>[AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents](https://arxiv.org/abs/2603.18429v1) | state-anchored memory and dependencies from interaction trajectories | retrieve and maintain anchors for mobile GUI action prediction |
| 2025 | <a id="mem_5c25220256"></a>[AppCopilot: Toward General, Accurate, Long-Horizon, and Efficient Mobile Agent](https://arxiv.org/abs/2509.02444v2) | 历史任务查询、状态、截图和动作序列；跨应用暂存数据 | LLM语义匹配旧操作，重放移动GUI任务；跨应用计划将暂存信息用于后续界面输入 |
| 2023 | <a id="mem_4aff73538a"></a>[Autonomous Large Language Model Agents Enabling Intent-Driven Mobile GUI Testing](https://arxiv.org/html/2311.08649v1) | 手机 GUI 测试历史和空间记忆 | 后续手机 GUI 测试行动 |
| 2026 | <a id="mem_cc84562bba"></a>[AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling](https://arxiv.org/html/2604.27253v1) | 探索阶段保存的页面队列、已访问页面和行动路径 | 探索代理利用历史跳过重复页面并重建后续 GUI 导航前缀；不表述为部署时检索 |
| 2025 | <a id="gui_chain_r1_wf_0269"></a>[BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212/) | prior mobile action states and detected error evidence | backtrack and recover subsequent mobile GUI execution |
| 2026 | <a id="mem_0041b9067c"></a>[BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://doi.org/10.1109/icassp55912.2026.11464343) | 历史操作轨迹、失败分支与子任务状态 | OSWorld 桌面 GUI 回退、更新计划及后续动作 |
| 2025 | <a id="gui_wf_0346"></a>[Beyond Static GUI Agent: Evolving LLM-based GUI Testing via Dynamic Memory](https://doi.org/10.1109/ase63991.2025.00135) | 功能轨迹、反思和探索策略 | 指导 GUI 测试并避开无效路径 |
| 2025 | <a id="mem_07db8f0fb4"></a>[Branch-and-Browse: Efficient and Controllable Web Exploration with Tree-Structured Reasoning and Action Memory](https://arxiv.org/html/2510.19838v2) | 网页探索树与页面动作历史 | 后续网页 GUI 导航 |
| 2025 | <a id="mem_936b23119b"></a>[BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions](https://arxiv.org/html/2510.10666v2) | 浏览历史与关键结论 | 后续网页浏览操作 |
| 2026 | <a id="mem_52b7dc4ee0"></a>[CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/html/2603.24157v1) | 临床 GUI 历史、纠错反馈与双层记忆 | 后续医疗软件 GUI 操作 |
| 2025 | <a id="gui_wf_0046"></a>[Chain-of-Memory: Enhancing GUI Agents for Cross-Application Navigation](https://arxiv.org/abs/2506.18158v1) | 动作描述及关键屏幕信息 | 跨应用GUI导航 |
| 2024 | <a id="mem_fbc3b0000a"></a>[CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://arxiv.org/html/2402.11941v3) | 手机 GUI 交互记录 | 后续手机 GUI 动作 |
| 2025 | <a id="mem_e50500ac57"></a>[COLA: Collaborative Multi-Agent Framework with Dynamic Task Scheduling for GUI Automation](https://aclanthology.org/2025.emnlp-main.227.pdf) | 执行状态与回退点 | GUI 任务回退 |
| 2025 | <a id="mem_1837b0096d"></a>[CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/html/2510.15455v1) | 手机 GUI 决策历史 | 后续手机 GUI 点击/输入 |
| 2025 | <a id="mem_a8771ae780"></a>[D-Artemis: A Deliberative Cognitive Framework for Mobile GUI Multi-Agents](https://arxiv.org/html/2509.21799v3) | 任务提示与工作记忆 | 后续手机 GUI 操作 |
| 2026 | <a id="mem_33b716376d"></a>[Does The Way You Plan Matter? An Empirical Study of Planning Representations for LLM Web Agents](https://arxiv.org/html/2605.29927v1) | 子目标清单、伪代码等任务计划 | 后续 WebArena GUI 行动 |
| 2026 | <a id="mem_37c7b428f4"></a>[Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/html/2604.05477v1) | 历史动作、预期效果与验证反馈 | 后续 GUI 自纠错操作 |
| 2024 | <a id="mem_9f0255f977"></a>[Dynamic Planning for LLM-based Graphical User Interface Automation](https://arxiv.org/html/2410.00467v3) | GUI 执行历史和动态计划 | 后续 GUI 动作 |
| 2026 | <a id="mem_627406dbf7"></a>[Falsifiable Commitment Planning for Self-Correcting Web Agents](https://arxiv.org/html/2607.24167v1) | 计划承诺、技能与失败修复经验 | 后续 WebArena GUI 行动 |
| 2026 | <a id="mem_5dbe38d0ef"></a>[Fixpad++: Automated Bug Fix Verification using LLM Agents](https://www.researchgate.net/publication/403258864_Fixpad_Automated_Bug_Fix_Verification_Using_LLM_Agents) | 跨复现迭代的 ActionAgent 推理—GUI 动作轨迹及前一步反思反馈。 | Gemini 2.5 Flash ActionAgent 在复现阶段使用历史轨迹与反思选择后续桌面 GUI 动作；补丁版本轨迹由 Action Manager 确定性重放 |
| 2026 | <a id="gui_wf_0317"></a>[FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory](https://arxiv.org/abs/2608.04530v1) | factorized latent GUI memory content with trust signal | read memory for later web actions |
| 2026 | <a id="mem_0e23d7fb68"></a>[From Bug Reports to Browser-Executable Procedures: An LLM-Driven Agent for Web GUI Bug Reproduction](https://arxiv.org/html/2608.03598v1) | bug 复现计划、资源清单与执行轨迹 | 后续浏览器 GUI 复现步骤 |
| 2024 | <a id="mem_075cbf2661"></a>[From Context to Action: Analysis of the Impact of State Representation and Context on the Generalization of Multi-Turn Web Navigation Agents](https://arxiv.org/html/2410.23555v1) | 网页交互历史 | 后续网页 GUI 元素选择 |
| 2025 | <a id="mem_6ee83388ce"></a>[General Agentic Planning Through Simulative Reasoning with World Models](https://arxiv.org/html/2507.23773v3) | 网页环境世界模型和模拟轨迹 | 后续浏览器 GUI 行动 |
| 2024 | <a id="mem_11da797c0d"></a>[GUARDIAN: A Runtime Framework for LLM-Based UI Exploration](https://dezhi-ran.com/publication/issta24-guardian/issta24-guardian.pdf) | 已访问 界面 状态、动作历史和受阻动作集合 | LLM 基于历史选下一 GUI 测试动作并在失败后回退 |
| 2025 | <a id="mem_c506ef96b2"></a>[GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](https://arxiv.org/abs/2510.27210v1) | 任务进度与行动历史摘要 | 下一步 GUI 导航 |
| 2024 | <a id="mem_d3ec2da938"></a>[GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451v2) | historical screenshots and actions with contextual summaries | guide cross-app mobile GUI navigation |
| 2026 | <a id="mem_9bbb29905d"></a>[GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/html/2601.04500v1) | 测试子任务及执行历史 | 后续手机 GUI 缺陷探索 |
| 2025 | <a id="mem_85b940ac68"></a>[History-Aware Reasoning for GUI Agents](https://ojs.aaai.org/index.php/AAAI/article/view/40966) | 交互历史与错误纠正规则 | 指导决策与错误恢复 |
| 2026 | <a id="mem_2e790649cf"></a>[HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents](https://arxiv.org/html/2607.14548v1) | 手机 GUI 步骤历史 | 后续手机 GUI 操作 |
| 2023 | <a id="mem_bc9314e21c"></a>[LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/html/2309.08172v2) | 网页状态与探索历史 | 后续网页 GUI 导航 |
| 2024 | <a id="mem_29565e9bba"></a>[LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing](https://arxiv.org/pdf/2402.10294v1) | 对话历史、视频标题/摘要和帧描述 | 后续视频编辑 GUI 的时间线排序与剪辑 |
| 2026 | <a id="mem_27213371dd"></a>[LDMDroid: Leveraging LLMs for Detecting Data Manipulation Errors in Android Apps](https://arxiv.org/pdf/2604.00458v2) | GUI 动作历史、变化摘要、任务进展与已发现的数据操作功能实例 | 后续 Android 界面探索和数据操作缺陷测试 |
| 2025 | <a id="mem_37b8090ed4"></a>[Learning GUI Grounding with Spatial Reasoning from Visual Feedback](https://arxiv.org/html/2509.21552v1) | 光标移动历史与空间关系 | 下一步GUI光标操作 |
| 2025 | <a id="mem_358154d3a0"></a>[LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents](https://arxiv.org/html/2512.04105v1) | 先前网页获取的任务信息 | 法律网站表单与日程操作 |
| 2025 | <a id="mem_ee67b1add7"></a>[Less is More: Empowering GUI Agent with Context-Aware Simplification](https://arxiv.org/html/2507.03730v1) | 先前界面及操作上下文 | 网页与手机GUI导航 |
| 2025 | <a id="mem_132daa5f0a"></a>[LightAgent: Mobile Agentic Foundation Models](https://arxiv.org/html/2510.22009v1) | 手机任务交互历史 | 移动GUI后续操作 |
| 2026 | <a id="mem_8fc549d94a"></a>[LLM-as-Code: Agentic Programming for Agent Harness](https://arxiv.org/html/2606.15874v1) | 调用树执行历史 | 后续电脑GUI操作 |
| 2025 | <a id="mem_47ed45cdbb"></a>[LLM-Empowered Scriptless Functional Testing](https://doi.org/10.1109/qrs65678.2025.00012) | 最近 X 个已执行 GUI 动作及上一已达成测试目标；测试过程中还记录状态转移模型。 | 每步把行动历史、上一目标、当前界面及可执行动作提交给 LLM，由其选取下一次 Web GUI 点击/输入/选择；模型内已实现目标检查。 |
| 2025 | <a id="mem_0e7c9a6a76"></a>[LLM-Guided Scenario-based GUI Testing](https://arxiv.org/html/2506.05079v1) | GUI 操作与测试过程 | 移动应用场景测试的后续决定 |
| 2026 | <a id="gui_wf_0337"></a>[LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents](https://arxiv.org/abs/2608.25777v1) | 子目标、证据及运行反馈 | 后续桌面GUI操作 |
| 2026 | <a id="mem_f2bc990ed3"></a>[M$^2$: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval](https://arxiv.org/abs/2603.00503v1) | 轨迹摘要和离线经验洞见 | 长程网页导航 |
| 2026 | <a id="mem_970c5d5d71"></a>[Mango: Multi-Agent Web Navigation via Global-View Optimization](https://arxiv.org/html/2604.18779v1) | 历史导航尝试 | 后续网页导航 |
| 2026 | <a id="gui_wf_0222"></a>[Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1) | latent persistent state across GUI interactions | condition later web and mobile GUI decisions |
| 2026 | <a id="mem_c72a11d0bd"></a>[MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management](https://arxiv.org/abs/2606.19926v1) | 折叠动作历史及界面状态 | 后续跨应用手机操作 |
| 2025 | <a id="mga"></a>[MGA: Memory-Driven GUI Agent for Observation-Centric Interaction](https://arxiv.org/html/2510.24168v1) | 屏幕状态增量与转移链 | 桌面GUI长程任务 |
| 2025 | <a id="mem_11cdbbfd00"></a>[MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://aclanthology.org/2025.naacl-demo.43/) | task outcomes, app-page interactions and user preferences | retrieve and adapt plans for later mobile GUI actions |
| 2026 | <a id="mem_b53aef7406"></a>[MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration](https://arxiv.org/html/2605.26546v1) | 探索动作轨迹和界面提示 | 后续移动GUI动作 |
| 2025 | <a id="mem_e66cca9ab5"></a>[MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation](https://papers.neurips.cc/paper_files/paper/2025/file/3994410d63ec68ce9a66011a34c9a2c4-Paper-Conference.pdf) | 执行错误与探索发现 | 长程手机 GUI 恢复 |
| 2026 | <a id="mem_ddb97803ba"></a>[Navigating the Infinite Dynamic Web Space: Effective In-Context Exploration via Cognitive Multi-Agent Collaboration](https://aclanthology.org/2026.eacl-long.384.pdf) | 观察历史与行动轨迹 | 动态网页导航回溯 |
| 2024 | <a id="mem_e070b3ae22"></a>[On the Multi-turn Instruction Following for Conversational Web Agents](https://aclanthology.org/2024.acl-long.477/) | 多轮对话与网页交互历史 | 指导后续对话式网页导航 |
| 2026 | <a id="mem_483b6e1939"></a>[OpAgent: Operator Agent for Web Navigation](https://arxiv.org/abs/2602.13559v2) | 前序推理与网页动作文本、待办清单、专家提示和结构化笔记 | Planner用历史及反馈选后续导航策略，Grounder执行浏览器动作 |
| 2026 | <a id="gui_wf_0124"></a>[OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent](https://arxiv.org/abs/2601.07779v1) | 任务里程碑与应用教程 | 桌面GUI长程任务 |
| 2024 | <a id="mem_6f8e302e89"></a>[OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://arxiv.org/html/2410.18963v1) | 当前流程状态与执行计划 | 桌面及移动GUI后续操作 |
| 2025 | <a id="mem_9a999b5414"></a>[PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC](https://arxiv.org/html/2502.14282v1) | 子任务进度与错误反馈 | 电脑跨应用任务操作 |
| 2025 | <a id="mem_b964a8de67"></a>[PLAN-AND-ACT: Improving Planning of Agents for Long-Horizon Tasks](https://arxiv.org/html/2503.09572v1) | 结构化高层任务计划 | 指导长程网页操作 |
| 2026 | <a id="mem_2cc9e86940"></a>[Plan-MCTS: Plan Exploration for Action Exploitation in Web Navigation](https://arxiv.org/html/2602.14083v1) | 抽象语义历史 | 后续网页导航规划 |
| 2026 | <a id="mem_9341bec452"></a>[Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning](https://arxiv.org/html/2605.02168v1) | 长期任务上下文 | 后续网页与OS操作 |
| 2026 | <a id="mem_4eadbdd6f9"></a>[Read More, Think More: Revisiting Observation Reduction for Web Agents](https://arxiv.org/html/2604.01535v1) | 历史网页观察及界面差分 | 后续网页动作 |
| 2026 | <a id="mem_56411d8457"></a>[SecAgent: Efficient Mobile GUI Agent with Semantic Context](https://arxiv.org/html/2603.08533v1) | 历史界面和动作语义摘要 | 后续移动GUI导航 |
| 2026 | <a id="mem_a6a464584a"></a>[See and Remember: A Multimodal Agent for Web Traversal](https://arxiv.org/html/2603.02626v1) | 结构化遍历路径 | 后续网页导航及回溯 |
| 2025 | <a id="mem_cc0284e6e2"></a>[See, Think, Act: Online Shopper Behavior Simulation with VLM Agents](https://arxiv.org/html/2510.19245v1) | 网页观测与动作历史 | 下一GUI动作预测 |
| 2026 | <a id="mem_96bab57611"></a>[Speech-visual integration multimodal multi-agents framework for mobile operation](https://link.springer.com/content/pdf/10.1007/s44443-026-00584-y.pdf) | 动态记录器的操作状态；知识池的任务模板与用户习惯 | 恢复执行并复用手机 GUI 操作 |
| 2026 | <a id="mem_eee7e82c40"></a>[Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/html/2604.27151v1) | 近期推理动作历史与任务里程碑 | 电脑代理后续GUI操作 |
| 2026 | <a id="mem_7611155082"></a>[StepReflect: Structured UI Transition Reflection for Mobile GUI Agents](https://arxiv.org/html/2608.05587v1) | 前一步和当前界面及转移预期 | 后续手机GUI纠错 |
| 2026 | <a id="mem_59bee19263"></a>[StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](https://arxiv.org/html/2607.11388v1) | 可验证进展、修改和失败状态 | 后续电脑GUI任务 |
| 2026 | <a id="mem_f24837cee4"></a>[STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks](https://arxiv.org/html/2603.05294v1) | 计划树、子目标与执行状态 | 长程网页任务执行 |
| 2025 | <a id="mem_effc1923f1"></a>[Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/html/2510.19949v1) | 长程任务上下文 | Web桌面移动GUI操作 |
| 2025 | <a id="mem_37a149a962"></a>[Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/html/2511.22235v1) | 任务进度与执行上下文 | 长程GUI操作 |
| 2024 | <a id="mem_2efe59c925"></a>[Tree Search for Language Model Agents](https://jykoh.com/search-agents/paper.pdf) | 搜索树状态及试探结果 | 真实 Web 交互规划 |
| 2025 | <a id="mem_dd64174a7b"></a>[TreeMind: Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search](https://arxiv.org/html/2509.22431v1) | 已探索界面动作历史 | Android缺陷复现导航 |
| 2025 | <a id="mem_ad5250d497"></a>[UFO3: Weaving the Digital Agent Galaxy](https://arxiv.org/abs/2511.11332v2) | 设备代理短期/长期任务进展与执行结果 | 更新状态供Windows HostAgent/AppAgent后续推理及GUI操作 |
| 2026 | <a id="mem_313d2389fe"></a>[UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/html/2604.13822v1) | 持久GUI观察和任务上下文 | 后续GUI任务执行 |
| 2026 | <a id="mem_16729366f4"></a>[VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/html/2606.24525v1) | 前后界面状态 | 后续GUI动作纠错 |
| 2026 | <a id="mem_cf6e59941f"></a>[VLAA-GUI: Knowing When to Stop, Recover, and Search, A Modular Framework for GUI Automation](https://arxiv.org/html/2604.21375v1) | 失败动作及重复屏幕状态 | 后续桌面GUI纠错 |
| 2024 | <a id="mem_d6240e522a"></a>[WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/html/2402.05930v1) | 网页动作与屏幕历史 | 指导对话式导航 |
| 2025 | <a id="mem_22cd31f6ad"></a>[WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](https://arxiv.org/html/2512.12692v1) | 浏览器导航路径和动作候选 | 网页任务安全回退 |
| 2024 | <a id="mem_b621b90477"></a>[WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration](https://arxiv.org/html/2408.15978v1) | 任务计划、执行进度与先前尝试 | 指导后续网页探索 |
| 2025 | <a id="mem_7bb832d88d"></a>[WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](https://arxiv.org/html/2504.11788v1) | 导航路径与先前状态 | Web 代理回滚及路径搜索 |
| 2025 | <a id="mem_6016a9ab72"></a>[WebRouter: Query-specific Router via Variational Information Bottleneck for Cost-sensitive Web Agent](https://arxiv.org/html/2510.11221v1) | 动作历史与网页状态 | 后续网页操作模型路由 |
| 2025 | <a id="mem_47f0d52734"></a>[WebSight: A Vision-First Architecture for Robust Web Agents](https://arxiv.org/html/2508.16987v1) | 任务情节 | 网页导航与动作验证 |
| 2026 | <a id="gui_wf_0298"></a>[What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States](https://arxiv.org/abs/2606.31612v2) | active task-driving states distilled from mobile records | use task state for subsequent mobile GUI planning |
| 2023 | <a id="mem_3f85fad284"></a>[You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/html/2309.11436v1) | 动作历史与待执行计划 | 选择后续移动界面动作 |

<a id="skill"></a>

## 工作流与技能 · 83

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2024 | <a id="mem_bd2603acc5"></a>[AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://arxiv.org/html/2411.13451v1) | 人类网页操作演示 | 后续网页 GUI 任务 |
| 2024 | <a id="gui_wf_0469"></a>[AGENT S: AN OPEN AGENTIC FRAMEWORK THAT USES COMPUTERS LIKE A HUMAN](https://arxiv.org/abs/2410.08164v1) | 外部应用知识与内部任务经验 | 桌面GUI规划与执行 |
| 2024 | <a id="gui_add_awm"></a>[Agent Workflow Memory](https://arxiv.org/abs/2409.07429v1) | parameterized workflows distilled from prior web tasks | retrieve workflow examples to generate subsequent web actions |
| 2024 | <a id="mem_e6c10c610b"></a>[AGENTTREK: AGENT TRAJECTORY SYNTHESIS VIA GUIDING REPLAY WITH WEB TUTORIALS](https://arxiv.org/html/2412.09605v2) | 网页教程与多模态指导轨迹 | 教程指导数据生成阶段的 VLM 多步网页 GUI 重放；不表述为部署时检索 |
| 2025 | <a id="mem_aafd37bfbc"></a>[ALLOY: Generating Reusable Agent Workflows from User Demonstration](https://arxiv.org/html/2510.10049v1) | 用户演示生成的工作流模板 | 跨网页任务复用与执行 |
| 2023 | <a id="gui_add_appagent"></a>[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771v3) | 应用操作知识库 | 选择手机 GUI 操作序列 |
| 2025 | <a id="appagentx"></a>[AppAgentX: Evolving GUI Agents as Proficient Smartphone Users](https://arxiv.org/html/2503.02268v3) | 手机 GUI 页面转移与动作结果 | 后续手机 GUI 操作 |
| 2024 | <a id="mem_377cdc507a"></a>[Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/html/2410.22552v1) | 示范轨迹、动作意图与意图预测器 | 后续网页 GUI 动作预测 |
| 2024 | <a id="mem_9377e9276f"></a>[AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://arxiv.org/abs/2403.08978v2) | 具有情境适用条件的导航指南 | 为网页操作选择适用指引 |
| 2025 | <a id="mem_1b0c025efd"></a>[Automated Test Transfer across Android Apps using Large Language Models](https://seal.ics.uci.edu/publications/2025_ISSTA.pdf) | 源应用测试事件及其语义抽象 | LLM 选择目标 Android 应用的逐步 GUI 事件 |
| 2023 | <a id="mem_33b60a25fc"></a>[Automatic Macro Mining from Interaction Traces at Scale](https://arxiv.org/html/2310.07023v2) | 用户 GUI 轨迹与可重放宏 | 后续手机界面宏执行 |
| 2026 | <a id="mem_8094943a75"></a>[AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](https://arxiv.org/html/2605.21082v1) | GUI 交互轨迹库 | 后续 GUI 机器人流程自动化 代码生成与执行 |
| 2024 | <a id="mem_4773250d93"></a>[BAGEL: Bootstrapping Agents by Guiding Exploration with Language](https://arxiv.org/abs/2403.08140v2) | synthetic instruction and action-observation demonstrations | retrieve examples to guide later MiniWoB++ web actions |
| 2026 | <a id="mem_6f421e4af8"></a>[Beyond Browser Agents: Distilling Experience for Accessible Web Automation](https://doi.org/10.1145/3800424.3800431) | 成功 GUI 操作轨迹、编译的脚本及异常修复片段 | 后续重复网页任务执行及失败时局部修复 |
| 2026 | <a id="mem_637c6dc8ce"></a>[Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns](https://arxiv.org/html/2606.17645v1) | 可迁移网页交互技能记录 | 跨站网页 GUI 控件操作 |
| 2026 | <a id="mem_62a54557e6"></a>[CAPTCHAs in the Agentic Era: Solvers That Learn from Every Encounter](https://arxiv.org/html/2609.02393v1) | 历史 验证码 图像及 VLM 标签 | 后续 GUI 验证码 视觉求解与点击 |
| 2025 | <a id="mem_efe0271b79"></a>[CHOP: Mobile Operating Assistant with Constrained High-frequency Optimized Subtask Planning](https://arxiv.org/html/2503.03743v1) | 高频手机 GUI 子任务库 | 后续手机 GUI 行动规划 |
| 2026 | <a id="mem_e5ebc58e38"></a>[CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications](https://arxiv.org/html/2608.11588v1) | 工作流步骤、失败与恢复经验 | 未见过的手机 GUI 应用后续操作 |
| 2026 | <a id="mem_d63ba396ed"></a>[Context-Aware Functional Test Generation via Business Logic Extraction and Adaptation](https://arxiv.org/html/2602.24108v1) | 历史测试案例与业务逻辑 | 生成目标应用 GUI 测试 |
| 2025 | <a id="mem_e7fb5956b9"></a>[Contextual Experience Replay for Self-Improvement of Language Agents](https://arxiv.org/html/2506.06698v1) | 轨迹蒸馏经验与动态缓冲区 | 后续网页 GUI 任务 |
| 2025 | <a id="mem_b190e0f2ed"></a>[Cracking the Code of Action: a Generative Approach to Affordances for Reinforcement Learning](https://arxiv.org/html/2504.17282v1) | GUI 可行动作代码 | 后续 MiniWoB++ 网页 GUI 行动约束 |
| 2025 | <a id="mem_9179d638a4"></a>[Cybernaut: Towards Reliable Web Automation](https://arxiv.org/html/2508.16688v1) | 用户演示及 标准操作流程 | 后续企业网页 GUI 操作 |
| 2026 | <a id="gui_wf_0134"></a>[Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528v1) | 可复用GUI轨迹单元 | 后续跨应用GUI任务 |
| 2026 | <a id="mem_9de61577a9"></a>[Domain Adaptation of MLLM-Based GUI Agents in Documentation-Rich Environments with Standard Operating Procedures](https://doi.org/10.1007/978-981-92-2856-0_34) | 技术手册页面及生成的任务专属 标准操作流程 页面转移序列 | 多模态大语言模型 座舱 GUI 代理逐步规划点击/滚动/输入 |
| 2026 | <a id="gui_wf_0242"></a>[DRIVE: Modeling Skills at the Reasoning and Interaction Levels for Web Agents under Continual Learning](https://arxiv.org/abs/2605.23939v1) | reasoning and interaction skills learned across web tasks | retrieve and update skills for subsequent web navigation |
| 2025 | <a id="mem_fb97493684"></a>[EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/html/2512.19396v3) | GUI 探索轨迹及整合记忆 | 后续 GUI 任务执行 |
| 2026 | <a id="mem_b8dede6c76"></a>[EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/html/2604.09815v1) | GUI/模型上下文协议（MCP） 动作轨迹与训练策略 | 后续电脑 GUI 动作选择 |
| 2024 | <a id="mem_f3dec444a3"></a>[Enabling Cost-Effective UI Automation Testing with Retrieval-Based LLMs: A Case Study in WeChat](https://researchmgt.monash.edu/ws/files/694588803/652457437.pdf) | 既有任务说明及对应 GUI 操作示例 | 新测试任务的 GUI 动作序列生成 |
| 2026 | <a id="mem_a9ac62b770"></a>[Enhancing Web Agents with a Hierarchical Memory Tree](https://arxiv.org/abs/2603.07024v1) | 分层任务流程与语义动作模式 | 跨网站网页操作 |
| 2026 | <a id="gui_wf_0224"></a>[Executable Agentic Memory for GUI Agent](https://arxiv.org/abs/2605.12294v1) | GUI状态、动作组及例程 | 后续移动GUI任务 |
| 2026 | <a id="mem_1db918cc57"></a>[Expanding LLM Agent Boundaries with Strategy-Guided Exploration](https://arxiv.org/html/2603.02045v1) | 探索轨迹与策略提示 | 后续 AndroidWorld GUI 操作 |
| 2024 | <a id="mem_73c5c9fc62"></a>[Explainable Behavior Cloning: Teaching Large Language Model Agents through Learning by Demonstration](https://arxiv.org/html/2410.22916v1) | 手机 GUI 用户示范动作序列 | 后续手机 GUI 任务 |
| 2026 | <a id="mem_2adf16983d"></a>[Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/html/2604.27996v3) | ParaView 任务经验与持久记忆 | 后续科学可视化 GUI 工作流 |
| 2026 | <a id="gui_add_2609_04869"></a>[From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents](https://arxiv.org/abs/2609.04869v1) | interaction traces distilled into persistent executable skills | skill reuse and revision during later desktop GUI tasks |
| 2025 | <a id="mem_55534f231d"></a>[From Operation to Cognition: Automatic Modeling Cognitive Dependencies from User Demonstrations for GUI Task Automation](https://pi.cs.tsinghua.edu.cn/wp-content/uploads/2025/06/3706598.3713356.pdf) | GUI 演示任务图、操作参数关系与认知依赖 | 重复任务时生成新参数并执行 GUI 任务 |
| 2026 | <a id="mem_082ac25de3"></a>[GLOVE: Global Verifier for LLM Memory-Environment Realignment](https://arxiv.org/abs/2601.19249v1) | 过去网页状态-动作-结果经验及修正记录 | 检索旧经验指导WebShop按钮/产品决策，发现漂移后探查并更新经验库 |
| 2026 | <a id="mem_a3ce0a1bc9"></a>[GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/html/2603.26266v3) | 视频教程中的操作步骤 | 后续电脑 GUI 任务 |
| 2026 | <a id="mem_7bd1196719"></a>[GUITrans2Act: Understanding User Operational Behaviors from Mobile GUI Interactions with Vision-Language Models](https://arxiv.org/html/2606.12817v2) | 手机 GUI 示范与操作描述 | 后续手机 GUI 重放 |
| 2026 | <a id="gui_wf_0172"></a>[Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291v1) | 结构化GUI轨迹及符号节点 | 后续GUI任务执行 |
| 2026 | <a id="mem_44b75fe96f"></a>[IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/html/2602.17049v2) | 意图向量、技能与计划记忆 | 后续电脑 GUI 任务 |
| 2025 | <a id="mem_2039589e4c"></a>[Intention-Based GUI Test Migration for Mobile Apps using Large Language Models](https://seg.nju.edu.cn/uploadPublication/copyright/1251771328477.pdf) | 源应用测试轨迹衍生的意图及探索事件历史 | 目标 Android 应用的逐步 GUI 测试迁移 |
| 2025 | <a id="mem_10448b01db"></a>[JEF-Hinter: Leveraging Offline Knowledge for Improving Web Agents Adaptation](https://arxiv.org/html/2510.04373v2) | 网页轨迹经验与反馈提示 | 后续网页 GUI 任务 |
| 2025 | <a id="mem_a04115503b"></a>[LEARN-BY-INTERACT: A DATA-CENTRIC FRAMEWORK FOR SELF-ADAPTIVE AGENTS IN REALISTIC ENVIRONMENTS](https://arxiv.org/html/2501.10893v1) | 环境交互轨迹与训练数据 | 后续电脑及网页 GUI 操作 |
| 2026 | <a id="mem_915a24bd29"></a>[Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents](https://arxiv.org/html/2606.31270v1) | 失败轨迹与修复策略/代码补丁 | 后续 OSWorld 电脑 GUI 任务 |
| 2025 | <a id="mem_0a87047f0a"></a>[Learning from Online Videos at Inference Time for Computer-Use Agents](https://arxiv.org/html/2511.04137v1) | 视频教程操作示范 | 计算机使用下一步GUI操作 |
| 2026 | <a id="mem_26f8a1013f"></a>[Learning Simple Test-Time Environments for LLM Web Agents](https://arxiv.org/html/2608.29305v1) | 子环境交互经验 | 后续网页自动化 |
| 2025 | <a id="mem_f645c3c0b6"></a>[LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://arxiv.org/html/2503.02950v1) | 代理工作流 | 浏览器任务规划与操作 |
| 2025 | <a id="mem_15b08655ec"></a>[Log2Plan: An Adaptive GUI Automation Framework Integrated with Task Mining Approach](https://arxiv.org/html/2509.22137v1) | 用户行为模式与任务字典 | 规划并执行 GUI 操作 |
| 2025 | <a id="mem_69df37e68d"></a>[Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358v1) | 已完成任务的计划及浏览器会话状态 | 新任务检索计划交给Orchestrator，再由WebSurfer执行网页点击等动作 |
| 2025 | <a id="mem_319b45f66d"></a>[Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills](https://arxiv.org/abs/2506.10387v1) | 分层GUI操作技能 | 跨平台长程GUI任务 |
| 2026 | <a id="mem_436a3bce45"></a>[MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?](https://arxiv.org/html/2606.01993v1) | 可执行步骤技能 | 后续GUI控制任务 |
| 2025 | <a id="mem_adaa85b94f"></a>[Mobile-Agent-RAG: Driving Smart Multi-Agent Coordination with Contextual Knowledge Empowerment for Long-Horizon Mobile Automation](https://arxiv.org/html/2511.12254v1) | 经验证的计划与应用操作指南 | 指导后续多应用移动任务执行 |
| 2023 | <a id="mobilegpt"></a>[MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation](https://arxiv.org/abs/2312.03003v3) | 应用子任务与操作流程 | 完成不同手机 GUI 任务 |
| 2026 | <a id="mem_6bd4636764"></a>[Motif: Discovering and Automating Personal Web Workflows](https://arxiv.org/html/2607.10531v1) | 重复网页工作流模式及程序 | 未来浏览器自动化 |
| 2025 | <a id="mem_43d635f955"></a>[NetGent: Agent-Based Automation of Network Application Workflows](https://arxiv.org/html/2509.00625v1) | 网页工作流状态与执行代码 | 重复网页任务执行 |
| 2026 | <a id="mem_9bff151ee5"></a>[OmegaUse-SOP: SOP Engineering for Professional Computer Use from Human Demonstrations](https://arxiv.org/html/2609.02149v1) | 专家流程和领域规则 | 后续专业GUI任务 |
| 2026 | <a id="gui_wf_0263"></a>[Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1) | 历史轨迹技能和动作代码 | 后续网页动作 |
| 2024 | <a id="mem_7f315017a0"></a>[PAFFA: Premeditated Actions For Fast Agents](https://arxiv.org/html/2412.07958v1) | 浏览器交互模式与动作 | 网页任务操作 |
| 2026 | <a id="gui_wf_0243"></a>[PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/abs/2605.24785v2) | distilled online interaction skills | reuse skills in subsequent multimodal web actions |
| 2026 | <a id="mem_50b7a11276"></a>[PCLLM: An Integrated LLM-Driven System for Automating Desktop Operations via Direct Mouse and Keyboard Control](https://mdpi-res.com/d_attachment/computers/computers-15-00351/article_deploy/computers-15-00351.pdf) | 软件架构与操作序列知识 | 桌面 GUI 鼠标键盘控制 |
| 2026 | <a id="mem_123c68649f"></a>[PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](https://arxiv.org/html/2603.03296v1) | 情景经验的命题和处方知识 | 网页代理后续任务 |
| 2023 | <a id="mem_ad3777085b"></a>[Prompting Is All You Need: Automated Android Bug Replay with Large Language Models](https://arxiv.org/html/2306.01987v1) | 缺陷回放示例 | 为新的 Android 缺陷生成复现操作序列 |
| 2025 | <a id="mem_43c402feb9"></a>[R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/html/2510.11892v1) | 外部操作教程 | OSWorld及WebArena任务规划 |
| 2024 | <a id="mem_f9fb586f04"></a>[RaDA: Retrieval-augmentedWeb Agent Planning with LLMs](https://aclanthology.org/2024.findings-acl.802.pdf) | 动作示范及其上下文 | 分解网页任务并生成动作 |
| 2025 | <a id="mem_323a806137"></a>[Real-Time Procedural Learning From Experience for AI Agents](https://arxiv.org/abs/2511.22074v2) | 状态-动作-结果经历 | Web 浏览下一步行动 |
| 2025 | <a id="gui_add_reasoningbank"></a>[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2) | stored reasoning experiences and self-evolving strategies | retrieve and refine plans for subsequent web actions |
| 2025 | <a id="mem_2976bcd4b4"></a>[Retrieval-augmented GUI Agents with Generative Guidelines](https://arxiv.org/html/2509.24183v1) | 网页教程与生成指南 | 数字 GUI 操作 |
| 2025 | <a id="mem_ed2d101659"></a>[ReuseDroid: A VLM-empowered Android UI Test Migrator Boosted by Active Feedback](https://arxiv.org/html/2504.02357v1) | 源应用测试操作逻辑 | 目标应用GUI测试 |
| 2026 | <a id="mem_6f5908ef54"></a>[See, Record, Do: Automated Generation of UI Workflows from Tutorial Videos](https://openaccess.thecvf.com/content/WACV2026/papers/Beauchaine_See_Record_Do_Automated_Generation_of_UI_Workflows_from_Tutorial_WACV_2026_paper.pdf) | 视频来源工作流与任务表 | 桌面 GUI 工作流执行 |
| 2024 | <a id="mem_6d3437948f"></a>[Skill-Adpative Imitation Learning for UI Test Reuse](https://arxiv.org/html/2409.13311v1) | 源测试中的可迁移操作技能 | 目标移动应用测试操作生成 |
| 2026 | <a id="mem_fc8efb4733"></a>[SkillDroid: Compile Once, Reuse Forever](https://arxiv.org/html/2604.14872v1) | 动作模板及元素定位器 | 未来移动GUI任务 |
| 2026 | <a id="mem_1884939353"></a>[SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation](https://arxiv.org/html/2608.10775v1) | 程序技能、视觉证据和验证信号 | 后续GUI操作 |
| 2025 | <a id="mem_ce2ba22ac8"></a>[Standing on the Shoulders of Giants: Bug-Aware Automated GUI Testing via Retrieval Augmentation](https://mediatum.ub.tum.de/doc/1832986/1832986.pdf) | 历史相似应用缺陷报告及其结构化知识库 | 目标 Android 应用的缺陷导向 GUI 测试路径规划 |
| 2023 | <a id="gui_wf_0488"></a>[SYNAPSE: TRAJECTORY-AS-EXEMPLAR PROMPTING WITH MEMORY FOR COMPUTER CONTROL](https://arxiv.org/abs/2306.07863v3) | 抽象状态—动作示范 | 指导后续网页操作 |
| 2024 | <a id="mem_0c31922846"></a>[TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision](https://arxiv.org/html/2403.06221v1) | 历史思路与示范步骤 | 指导后续网页动作决策 |
| 2025 | <a id="ufo2"></a>[UFO2: The Desktop AgentOS](https://arxiv.org/html/2504.14603v1) | 应用领域知识 | Windows GUI及应用程序编程接口（API）任务执行 |
| 2024 | <a id="mem_0408187a4f"></a>[VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://arxiv.org/abs/2406.14596v6) | 示范与子目标的程序化抽象 | 指导多模态网页决策 |
| 2025 | <a id="gui_wf_0106"></a>[WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997v2) | 浏览轨迹与任务经验 | 跨会话网页导航 |
| 2026 | <a id="mem_a695d565aa"></a>[WebGrader: Training LLMs for Web Development with Self-Evolving Programmatic Grader](https://arxiv.org/html/2608.06474v1) | 先前 GUI 验证失败痕迹抽象的可路由 SkillGraph | 后续 live browser Flow Contract 规划、grounding 与证据判断 |
| 2025 | <a id="mem_8df7178cb0"></a>[WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents](https://arxiv.org/html/2504.12682v1) | 网页操作程序与层叠样式表（CSS）选择器 | 相似网站页面数据抽取 |
| 2025 | <a id="mem_85eb734c18"></a>[WebSurfer: Enhancing LLM Agents with Web-Wise Feedback for Web Navigation](https://doi.org/10.1109/icassp49660.2025.10889961) | 专家轨迹样例、网页操作洞见与失败经验 | 后续网页导航步骤的元素/动作预测 |
| 2026 | <a id="mem_e58f01140b"></a>[WebXSkill: Skill Learning for Autonomous Web Agents](https://arxiv.org/html/2604.13318v1) | 参数化动作程序和步骤指导 | 后续网页任务执行 |
| 2024 | <a id="wilbur"></a>[WILBUR: Adaptive In-Context Learning for Robust and Accurate Web Agents](https://arxiv.org/html/2404.05902v1) | 先前 Web 任务示范与错误路径 | 网页导航和错误恢复 |

<a id="user"></a>

## 用户上下文与个性化 · 14

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2026 | <a id="mem_7f2655ac49"></a>[Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions](https://arxiv.org/html/2608.14132v1) | 手机行为描述与意图历史 | 预测并执行后续手机 GUI 任务 |
| 2025 | <a id="mem_204f29eed1"></a>[Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM](https://arxiv.org/html/2512.15784v1) | 用户画像、任务模板和动作记录 | 后续手机 GUI 任务 |
| 2026 | <a id="mem_6dad5bd2d7"></a>[Exploring Recommender System Evaluation: A Multi-Modal User Agent Framework for A/B Testing](https://arxiv.org/pdf/2601.04554v1) | 跨会话推荐交互、视觉/文本偏好及当前会话行为 | 模拟用户在推荐 GUI 中点击、查看、评分、翻页 |
| 2026 | <a id="mem_ba19f0a17f"></a>[KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/html/2607.12625v2) | 用户偏好、任务记忆与技能 | 后续个人 GUI 任务 |
| 2024 | <a id="gui_wf_0339"></a>[Large Language Models Empowered Personalized Web Agents](https://doi.org/10.1145/3696410.3714842) | 用户画像与历史 Web 行为 | 理解个性化指令并执行 Web 动作 |
| 2025 | <a id="gui_wf_0395"></a>[MemAgent: A cache-inspired framework for augmenting conversational Web Agents with task-specific information](https://ceur-ws.org/Vol-4028/paper8.pdf) | 任务特定用户信息 | 完成重复网页任务 |
| 2026 | <a id="gui_wf_0125"></a>[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://arxiv.org/abs/2601.09636v2) | 用户偏好、习惯和长期记录 | 手机GUI个性化操作 |
| 2025 | <a id="mem_234fdc406a"></a>[Quick on the Uptake: Eliciting Implicit Intents from Human Demonstrations for Personalized Mobile-Use Agents](https://arxiv.org/html/2508.08645v1) | 操作规程与用户习惯 | 移动GUI个性化任务执行 |
| 2026 | <a id="mem_efbc9702cc"></a>[Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227v1) | 跨日事务、用户画像、通知事件、反馈及跨设备会话结果 | 据记忆形成可执行任务并选手机/电脑GUI代理；共享会话结果用于重规划 |
| 2026 | <a id="mem_373c352731"></a>[SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents](https://arxiv.org/html/2602.01443v1) | 买家画像、意图和行为原型；买家画像与会话经验 | 模拟浏览器购物交互；后续商店浏览 |
| 2026 | <a id="mem_584eda464a"></a>[SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents](https://arxiv.org/html/2605.14205v1) | 买家历史行为类型 | 模拟买家网页操作 |
| 2026 | <a id="mem_9e2b16e0a6"></a>[Towards Automated Crowdsourced Testing via Personified-LLM](https://arxiv.org/html/2603.24160v1) | 测试角色的习惯与策略 | 生成多样化 GUI 测试事件 |
| 2026 | <a id="mem_9479f6783a"></a>[Towards Faithful Simulation of Human Shopping Behavior](https://arxiv.org/html/2608.20707v1) | 会话轨迹和购物偏好 | 后续电商GUI操作 |
| 2026 | <a id="mem_398ebf466a"></a>[TRACE: A Scalable and Extensible Framework for Auditing YouTube's Recommendation Algorithm](https://research.dial.uclouvain.be/bitstreams/b64910f1-bd40-413b-bd2e-7f7985ab8bc8/download) | 用户角色画像 | 驱动 Web 界面交互模拟 |

<a id="evaluation"></a>

## 基准与评测 · 22

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2026 | <a id="gui_wf_0277"></a>[Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/abs/2606.15017v2) | 在线工作流记忆和技能 | 后续网页操作 |
| 2024 | <a id="mem_8a0c25bfd0"></a>[Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474v3) | execution trajectories and evaluator judgments | evaluate and refine later web or device-control actions |
| 2026 | <a id="mem_5d57f6aaad"></a>[Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World](https://arxiv.org/html/2605.26086v1) | 跨设备持久状态与历史事件 | 跨手机和桌面 GUI 的后续任务 |
| 2026 | <a id="mem_8a368533a6"></a>[DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments](https://arxiv.org/html/2607.13465v1) | 基线输入中最近十步行动与反馈 | 后续手机/桌面 GUI 动作 |
| 2026 | <a id="mem_0d7de943af"></a>[DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents](https://arxiv.org/html/2605.17439v2) | 失败轨迹摘要与分支证据 | 后续 GUI 重探与软件诊断 |
| 2025 | <a id="mem_0c787d498c"></a>[FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://arxiv.org/html/2507.21071v2) | 用户画像与历史意图 | 后续手机 GUI 任务建议和执行 |
| 2025 | <a id="mem_2b1f95c536"></a>[FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games](https://arxiv.org/html/2509.01052v2) | 游戏 GUI 线索与任务轨迹 | 后续游戏 GUI 操作 |
| 2026 | <a id="mem_e50ada3c2a"></a>[GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/html/2604.07429v1) | 游戏 GUI 多轮截图和行动 | 后续游戏 GUI 键鼠动作 |
| 2026 | <a id="mem_883eca9986"></a>[KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/html/2604.08455v1) | 用户画像与历史手机操作日志 | 后续个人化手机 GUI 任务评测 |
| 2025 | <a id="mem_15a6944ee7"></a>[MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/html/2509.06477v1) | 预设与代理生成的快捷工作流 | 手机GUI与快捷操作混合执行 |
| 2026 | <a id="gui_wf_0140"></a>[MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075v3) | 跨动作及跨会话信息 | 移动GUI任务评测 |
| 2026 | <a id="gui_wf_0241"></a>[MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833v1) | 长程代理经历 | 后续网页任务 |
| 2025 | <a id="mem_067bd369ad"></a>[NatureGAIA: Pushing the Frontiers of GUI Agents with a Challenging Benchmark and High-Quality Trajectory Dataset](https://arxiv.org/html/2508.01330v1) | 任务计划与演进上下文 | 长程GUI任务执行 |
| 2025 | <a id="mem_a1448e1af0"></a>[OPeRA: A Dataset of Observation, Persona, Rationale, and Action for Evaluating LLMs on Human Online Shopping Behavior Simulation](https://arxiv.org/html/2506.05606v1) | 用户画像与购物操作历史 | 网页下一动作预测 |
| 2026 | <a id="mem_97b28f23ad"></a>[OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/html/2606.29537v1) | 跨来源任务信息与用户档案 | 后续电脑GUI任务 |
| 2026 | <a id="mem_2807793b6c"></a>[Persona2Web: Benchmarking Personalized Web Agents for Contextual Reasoning with User History](https://arxiv.org/abs/2602.17003v3) | 用户历史与隐含偏好 | 个性化网页操作 |
| 2026 | <a id="gui_wf_0306"></a>[PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails](https://arxiv.org/abs/2607.20482v2) | 历史事实与用户偏好 | 后续个性化网页操作 |
| 2024 | <a id="mem_28a8173dfe"></a>[SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://arxiv.org/abs/2410.15164v2) | cross-step task context and agent memory retention as evaluation targets | evaluates retention during interactive Android task execution |
| 2025 | <a id="mem_e80d0330b9"></a>[WEB-SHEPHERD: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/html/2505.15277v1) | 网页任务轨迹与步骤检查 | Web 任务下一步验证 |
| 2025 | <a id="mem_e9a3fe5356"></a>[WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks](https://arxiv.org/html/2506.01952v1) | 跨网页观察信息 | 网页复杂任务完成 |
| 2025 | <a id="mem_6b3ed2ddf7"></a>[WebMall - A Multi-Shop Benchmark for Evaluating Web Agents](https://arxiv.org/html/2508.13024v1) | 代理短期任务记忆 | 多商店 Web 购物任务 |
| 2026 | <a id="mem_e2b3c41f62"></a>[When Users Change Their Mind: Evaluating Interruptible Agents in Long-Horizon Web Navigation](https://arxiv.org/html/2604.00892v1) | 已执行网页状态与用户目标变更 | 中断后的网页导航 |

<a id="security"></a>

## 安全与可靠性 · 15

| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |
|---|---|---|---|
| 2026 | <a id="mem_680ac02d1c"></a>[CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/abs/2609.21686v1) | 网页代理检索的用户敏感记忆记录 | 记忆指导网页动作时评测经动作、过程或最终输出通道泄漏 |
| 2025 | <a id="mem_9077f1805d"></a>[Context manipulation attacks : Web agents are susceptible to corrupted memory](https://arxiv.org/html/2506.17318v1) | 被注入的知识、行动历史和计划 | 网页 GUI 后续行动安全评测 |
| 2026 | <a id="gui_wf_0338"></a>[CURA: Certified Runtime Alarms for Computer-Use Agents](https://arxiv.org/abs/2608.27808v1) | 执行轨迹风险状态 | 后续GUI监督和恢复 |
| 2026 | <a id="mem_f0227aecf6"></a>[Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces](https://arxiv.org/html/2605.09497v1) | 欺骗性界面风险经验 | 后续网页 GUI 点击审查 |
| 2024 | <a id="gui_wf_0012"></a>[GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning](https://arxiv.org/abs/2406.09187v3) | 先前任务示例经验 | 网页代理操作的安全核验 |
| 2025 | <a id="mem_0ee3ad606e"></a>[HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization](https://arxiv.org/html/2508.04010v1) | 统一安全策略数据库 | 后续网页 GUI 动作审批 |
| 2026 | <a id="gui_wf_0249"></a>[MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution](https://arxiv.org/abs/2605.28646v2) | 个性化隐私政策与纠正技能 | 后续GUI代理屏幕处理 |
| 2026 | <a id="gui_wf_0271"></a>[MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/abs/2606.10742v1) | 被投毒的图记忆及图文证据 | 未来网页任务 |
| 2026 | <a id="gui_add_2609_02057"></a>[Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision](https://arxiv.org/abs/2609.02057v1) | observable web-agent trajectory and key-step supervision signal | external monitor judges and intervenes in later web-agent actions |
| 2026 | <a id="mem_9d7e2d0d16"></a>[OpenAgentFlow: Enabling System-Wide Safety Boundaries for Heterogeneous AI Agent Fleets](https://arxiv.org/abs/2609.00015v2) | 外部策略执行点的会话来源、敏感值及策略状态 | 历史来源用于审核/阻止后续Android GUI动作提交，复杂案可交模型裁决 |
| 2025 | <a id="mem_af47dbc20f"></a>[Permission Manifests for Web Agents](https://arxiv.org/html/2601.02371v1) | 网站允许的交互规则 | 网页导航与操作许可 |
| 2026 | <a id="gui_wf_0190"></a>[Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents](https://arxiv.org/abs/2604.02623v2) | 被污染的网页交互轨迹 | 跨会话网页任务 |
| 2026 | <a id="mem_c7553f9bac"></a>[ProjGuard: Safety Monitoring for Computer-Use Agents via Low-Dimensional Projections](https://arxiv.org/html/2605.13631v1) | 累积操作轨迹及风险 | 后续电脑GUI安全纠偏 |
| 2026 | <a id="mem_73d703b4a3"></a>[SynChain: Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains](https://arxiv.org/html/2608.06862v1) | 被污染的技能及记忆条目 | 未来电脑代理工作流 |
| 2025 | <a id="gui_wf_0040"></a>[VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents](https://arxiv.org/abs/2506.02539v3) | domain-specific memory records and verification judgments | verify memory before later desktop GUI actions |

## 数据维护

`catalogue.csv` 是本目录的数据源。修改记录后运行 `python scripts/build_catalogue.py`；使用 `python scripts/build_catalogue.py --check` 检查双语页面是否同步。
