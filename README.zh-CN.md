<div align="center">

![Awesome GUI Agent Memory — research library](assets/library-banner.svg)

# Awesome GUI Agent Memory

### GUI 智能体记忆文献库

围绕 GUI／Computer-Use Agent 记忆的精选论文、机制导读与可追溯证据。

[English](README.md) · **简体中文**

[阅读起点](#start) · [主题书架](#shelves) · [基准](#benchmarks) · [我们的综述](#survey) · [证据](#evidence)

**论文链接 — 待公开** · **精选书目：30 项** · **证据覆盖截止：2026-09-10**

</div>

---

<a id="start"></a>

## 🧭 阅读起点

| 阅读目标 | 建议路线 |
|---|---|
| 建立整体认识 | [相关综述](#surveys) → [我们的框架](#survey) |
| 理解长任务中的信息保持 | [任务状态与视觉历史](#state)：ATMem → PAL-UI → MementoGUI |
| 理解跨任务经验复用 | [轨迹与经验](#experience)：Synapse → Agent S → [工作流与技能](#skills)：AWM |
| 研究记忆可靠性 | [维护与安全](#maintenance)：HYMEM → Darwinian Memory → VerificAgent |
| 设计评测或核查论断 | [基准与评测](#benchmarks) → [固定证据包](#evidence) |

<a id="shelves"></a>

## 📚 主题书架

这些主题是阅读导航；具体生命周期与状态对象编码见证据矩阵。当前精选书目来自已有证据材料。书目收录与正式编码分别维护，固定证据版本记录各条主张的依据与范围。

[🖥️ 任务状态与视觉历史](#state) · [🧭 轨迹与经验](#experience) · [🛠️ 工作流与技能](#skills) · [👤 用户偏好与任务信息](#personalization) · [🔄 记忆维护与安全](#maintenance) · [🧪 基准与评测](#benchmarks) · [📖 相关综述](#surveys)

<a id="state"></a>

### 🖥️ 任务状态与视觉历史

保留后续操作需要的信息。

**ATMem** · 2026<br>
[What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States](https://arxiv.org/abs/2606.31612v2)<br>
将任务数据组织为执行状态，区分数据适用性、工作流进度与剩余操作。<br>
[证据: PC-016](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L375)

**PAL-UI** · 2025<br>
[PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents](https://arxiv.org/abs/2510.00413v2)<br>
需要回看时，按历史步骤索引取回截图。<br>
[证据: PC-003](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L54)

**Chain-of-Memory** · 2025<br>
[Chain-of-Memory: Enhancing GUI Agents for Cross-Application Navigation](https://arxiv.org/abs/2506.18158v1)<br>
用有容量上限的短期记忆保留近期动作结果，并筛选屏幕中的任务相关信息写入长期记忆（PC-002）。<br>
[证据: PC-001](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L3)

**MementoGUI** · 2026<br>
[MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652v1)<br>
将筛选后的事件保存为文字摘要与图像区域，供后续动作判断使用。<br>
[证据: PC-013](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L298)

**CausalCache** · 2026<br>
[CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](https://arxiv.org/abs/2608.22577v2)<br>
在固定活动图像预算内，将选中的已总结历史事件恢复为图文形式。<br>
[证据: PC-015](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L351)

**Mem-W** · 2026<br>
[Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1)<br>
将历史经验及即将移出的上下文前缀压缩为潜在记忆块，供冻结的 GUI 策略使用。<br>
[证据: PC-012](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L274)

[↑ 返回书架](#shelves)

<a id="experience"></a>

### 🧭 轨迹与经验

从以往交互中提取可复用的指导。

**Synapse** · 2023<br>
[Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863v3)<br>
按任务元数据检索示例轨迹；其 Mind2Web 示例库使用训练集。<br>
[代码](https://github.com/ltzheng/Synapse) · [证据: PC-041](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L979)

**Agent S** · 2024<br>
[Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164v1)<br>
检索成功子任务经验，并在完成后写回策略摘要。<br>
[代码](https://github.com/simular-ai/Agent-S) · [证据: PC-044](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1056)

**ReasoningBank** · 2025<br>
[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2)<br>
保存从成功和失败经历中提取的结构化经验。<br>
[证据: PC-035](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L834)

**WebCoach** · 2025<br>
[WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997v2)<br>
任务结束后保存完整轨迹摘要，执行中依据部分轨迹检索经验。<br>
[证据: PC-011](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L249)

[↑ 返回书架](#shelves)

<a id="skills"></a>

### 🛠️ 工作流与技能

将交互历史转化为可复用的操作流程。

**Agent Workflow Memory** · 2024<br>
[Agent Workflow Memory](https://arxiv.org/abs/2409.07429v1)<br>
从经历中归纳子任务流程，将实例值抽象为参数，辅助动作生成。<br>
[代码](https://github.com/zorazrw/agent-workflow-memory) · [证据: PC-034](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L809)

**ActionEngine** · 2026<br>
[ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502v1)<br>
记录界面状态转移，为动态内容保留基于选择器的访问模式。<br>
[证据: PC-017](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L400)

**State-Grounded Dynamic Retrieval** · 2026<br>
[Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1)<br>
从轨迹窗口提取局部技能，通过替换动作片段并重执行进行验证。<br>
[证据: PC-021](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L503)

**AppAgent** · 2023<br>
[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771v3)<br>
在探索中建立并更新界面元素文档，部署时提供当前页面的功能说明。<br>
[代码](https://github.com/TencentQQGYLab/AppAgent) · [证据: PC-042](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1005)

[↑ 返回书架](#shelves)

<a id="personalization"></a>

### 👤 用户偏好与任务信息

在明确的适用范围内复用用户上下文。

**PersonaTrail / PACMEM** · 2026<br>
[PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails](https://arxiv.org/abs/2607.20482v2)<br>
将浏览历史分为事实记忆与偏好记忆，结合语义和时间线索检索。<br>
[证据: PC-022](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L529)

**PersonalAlign / HIM-Agent** · 2026<br>
[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://arxiv.org/abs/2601.09636v2)<br>
将 GUI 用户记录聚合为原型，每日更新层级化的偏好与例行意图记忆。<br>
[证据: PC-025](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L602)

**MemAgent** · 2025<br>
[MemAgent: A cache-inspired framework for augmenting conversational Web Agents with task-specific information](https://ceur-ws.org/Vol-4028/paper8.pdf)<br>
将任务信息收集与执行分开，并为缓存的任务实体设置过期策略。<br>
[证据: PC-024](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L575)

[↑ 返回书架](#shelves)

<a id="maintenance"></a>

### 🔄 记忆维护与安全

更新有效记忆，并处理过时或有害内容。

**HYMEM** · 2026<br>
[Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291v1)<br>
检索相邻经验节点并检查冗余后，选择新增、合并或替换。<br>
[证据: PC-009](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L198)

**Darwinian Memory** · 2026<br>
[Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528v1)<br>
结合使用效用、时间衰减和执行验证失败惩罚，调节记忆存留与剪枝。<br>
[证据: PC-008](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L175)

**PANDO** · 2026<br>
[PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/abs/2605.24785v2)<br>
通过关键词检索规则与程序技能，并对反复失败的技能进行持久降级。<br>
[证据: PC-020](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L478)

**VerificAgent** · 2025<br>
[VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents](https://arxiv.org/abs/2506.02539v3)<br>
使用经专家核查的轨迹教训，测试推理时保持记忆冻结。<br>
[证据: PC-005](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L102)

**环境注入式记忆投毒** · 2026<br>
[Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents](https://arxiv.org/abs/2604.02623v2)<br>
研究网页内容如何污染保存的轨迹，并通过记忆召回影响后续任务。<br>
[证据: PC-031](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L745)

[↑ 返回书架](#shelves)

<a id="benchmarks"></a>

### 🧪 基准与评测

结合交互协议理解报告的指标。

**MemGUI-Bench · GUI 在线执行** · 2026<br>
[MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075v3)<br>
在 Android GUI 在线执行中评测失败后重置与镜像任务对之间的经验迁移。<br>
[证据: PC-053](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1268)

**AndroTMem · 预录轨迹** · 2026<br>
[AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents](https://arxiv.org/abs/2603.18429v1)<br>
在预录轨迹的固定截图和标注动作上，评测状态锚点及依赖关系。<br>
[证据: PC-052](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1248)

**LongMemEval-V2 · 记忆问答** · 2026<br>
[LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493v1)<br>
按序插入轨迹，再以答案准确率和查询延迟评测固定 reader。<br>
[证据: PC-055](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1308)

**MemGym · 长程环境** · 2026<br>
[MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833v1)<br>
使用相同 reasoner 衡量记忆收益，同时考虑记忆会改变后续动作分布。<br>
[证据: PC-056](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1328)

**Web 智能体预算约束研究** · 2026<br>
[Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/abs/2606.15017v2)<br>
将动作生成、流程归纳、技能合成、记忆构建、检索及验证调用计入每任务 token 成本。<br>
[证据: PC-058](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1369)

[↑ 返回书架](#shelves)

<a id="surveys"></a>

### 📖 相关综述

用于理解 GUI 记忆研究背景的更广泛视角。

**LLM 智能体记忆机制** · 2024<br>
[A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501v1)<br>
按定义、来源、形式、操作及评测组织的通用记忆导读。<br>
[证据: PC-059](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1389)

**Memory in the Age of AI Agents** · 2025<br>
[Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)<br>
通过形式、功能和动态过程组织智能体记忆。<br>
[证据: PC-061](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1431)

**LLM-Brained GUI Agents** · 2024<br>
[Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279v12)<br>
梳理 GUI 智能体的组件、框架、数据、模型、评测与应用。<br>
[证据: PC-064](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json#L1493)

[↑ 返回书架](#shelves)

<a id="survey"></a>

## 📘 我们的综述

**Memory for GUI Agents: A Framework Survey of Lifecycles and State Layers**

**论文链接 — 待公开。** 公开后将在此提供论文链接与正式引用信息。

综述以“记忆生命周期 × GUI 状态层级”组织研究，关联记忆保留的对象、使用与维护方式，以及评测条件。阅读时可以从三个角度对照方法：

- **记住什么**：界面信息、任务状态、可复用流程或用户上下文。
- **怎样使用和维护**：如何取回、更新、验证与淘汰。
- **怎样评测**：在线交互、离线轨迹或记忆问答，各自使用什么预算和终点。

<a id="evidence"></a>

## 🔎 证据与复现

固定版本 **`evidence-20260913-r4.19`** 包含 **55 个编码来源、75 条主张与 24 项机制比较**，文献覆盖截止于 **2026-09-10**。这些计数描述证据包，不是上方精选书目的数量。

- [证据包总览](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/README.md)
- [获取与编码方法](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/evidence_methods.md)
- [主张与原文定位](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/claims.json)
- [生命周期—状态矩阵](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/capability_matrix.csv)
- [来源画像](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/corpus_profile.csv)
- [机制比较](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/mechanism_comparisons.json)
- [获取记录](https://github.com/kqcoxn/gui-memory-evidence/blob/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/current/acquisition_records.json)
- [检索式与执行记录](https://github.com/kqcoxn/gui-memory-evidence/tree/evidence-20260913-r4.19/releases/evidence-20260913-r4.19/baseline/search/)

校验固定证据包的哈希、计数与记录关联：

```sh
cd releases/evidence-20260913-r4.19
python3 validate.py
```

[历史版本](https://github.com/kqcoxn/gui-memory-evidence/tags)通过 Git 标签保留。注释与引文链接到原始出版物；来源材料保留其适用权利，全文可通过记录的来源链接访问。

## 🤝 参与贡献

欢迎通过 [Issue](https://github.com/kqcoxn/gui-memory-evidence/issues) 或 Pull Request 推荐论文、修正链接或改进导读。请提供原始论文链接、建议分类及一两句话说明与 GUI 记忆的关系；代码链接应指向作者发布的实现。修改条目时同步更新中英文版本。涉及证据修正时，请附主张编号与原文定位，作为新版本处理。

## 🌐 延伸阅读

- [GUI Agents Paper List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List)
- [LLM-Brained GUI Agents Survey](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey)
- [From Storage to Experience](https://github.com/FeishuLuo/Evolving-LLM-Agent-Memory-Survey)

---

<div align="center">

[English](README.md) · **简体中文**

从文献发现到证据核查。

</div>
