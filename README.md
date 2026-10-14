<div align="center">

![Awesome GUI Agent Memory — research library](assets/library-banner.svg)

# Awesome GUI Agent Memory

### A reading library for agents that remember

Curated papers, mechanism guides and traceable evidence on memory for GUI and computer-use agents.

**English** · [简体中文](README.zh-CN.md)

[Start Here](#start) · [Paper Library](#shelves) · [Full Catalogue](CATALOGUE.md) · [Benchmarks](#benchmarks) · [Our Survey](#survey) · [Evidence](#evidence)

**Paper — Coming soon** · **43 curated readings** · **289 classified works through 2026-09-20**

</div>

---

<a id="start"></a>

## 🧭 Start Here

| Reading goal | Suggested route |
|---|---|
| Get oriented | [Related surveys](#surveys) → [Our framework](#survey) |
| Compare visual history representations | [Task state & visual history](#state): UI-TARS / OpenCUA → PAL-UI → CausalCache → MementoGUI |
| Explore visual compression and verification | [Task state & visual history](#state): GUI-KV → [Maintenance & safety](#maintenance): SmartSnap |
| Connect interface knowledge to procedures | [Task state & visual history](#state): MapAgent → [Workflows & skills](#skills): MobileGPT |
| Connect execution state to reusable procedures | [Task state](#state): ATMem → [Workflows & skills](#skills): AWM → Mobile-Agent-E |
| Explore reuse across tasks | [Trajectories & experience](#experience): Synapse → Agent S → [Workflows & skills](#skills): AWM |
| Understand information sharing between agents | [Task state & visual history](#state): UFO2 → [Our framework](#survey): dependencies and scope |
| Study memory reliability | [Maintenance & safety](#maintenance): HYMEM → Darwinian Memory → VerificAgent |
| Design an evaluation or check a claim | [Benchmarks](#benchmarks) → [Fixed evidence package](#evidence) |
| Browse the wider literature | [289-work catalogue](CATALOGUE.md) → [Downloadable CSV](catalogue.csv) |

<a id="shelves"></a>

## 📚 Paper Library

These shelves offer 43 selected readings, including background surveys. The [full catalogue](CATALOGUE.md) covers 289 distinct works selected for the survey through **2026-09-20**: 250 direct-memory studies and 39 related evaluation/security studies. Its seven themes provide reading routes, with retained objects, subsequent GUI uses and original-source links; the [CSV](catalogue.csv) also records consulted versions and source passages. Selection is based on contribution to the framework and may omit relevant work.

The [companion data](#evidence) provide the 289-work catalogue, explicit matrix assignments, corpus statistics, executed queries and selection totals. Reading notes below link to the consulted sources.

[🖥️ Task State & Visual History](#state) · [🧭 Trajectories & Experience](#experience) · [🛠️ Workflows & Skills](#skills) · [👤 User Preferences & Task Information](#personalization) · [🔄 Maintenance & Memory Safety](#maintenance) · [🧪 Benchmarks & Evaluation](#benchmarks) · [📖 Related Surveys](#surveys)

<a id="state"></a>

### 🖥️ Task State & Visual History

Keeping the information needed for the next action.

**ATMem** · 2026<br>
[What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States](https://arxiv.org/abs/2606.31612v2)<br>
Organizes task data as execution state, separating data applicability, workflow progress and remaining operations.<br>

**PAL-UI** · 2025<br>
[PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents](https://arxiv.org/abs/2510.00413v2)<br>
Retrieves a previous screenshot by step index when the agent needs to look back.<br>

**Chain-of-Memory** · 2025<br>
[Chain-of-Memory: Enhancing GUI Agents for Cross-Application Navigation](https://arxiv.org/abs/2506.18158v1)<br>
Bounds recent action results in short-term memory; task-relevant screen information is selected into long-term memory.<br>

**MementoGUI** · 2026<br>
[MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652v1)<br>
Keeps selected events as text summaries and image regions for later action decisions.<br>

**CausalCache** · 2026<br>
[CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](https://arxiv.org/abs/2608.22577v2)<br>
Restores selected summarized events to text-and-image form within a fixed active-image budget.<br>

**Mem-W** · 2026<br>
[Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1)<br>
Compresses past experience and aging context prefixes into latent memory blocks for a frozen GUI policy.<br>

**UI-TARS** · 2025<br>
[UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326v1)<br>
Retains a recent screenshot window alongside complete action and thought histories as inputs to later decisions.<br>

**OpenCUA** · 2025<br>
[OpenCUA: Open Foundations for Computer-Use Agents](https://arxiv.org/abs/2508.09123v1)<br>
Represents history with concise action-level text and multiple screenshots; compares history representations in its evaluation.<br>

**UFO2** · 2025<br>
[UFO2: The Desktop AgentOS](https://arxiv.org/abs/2504.14603v1)<br>
Combines private agent state with a shared blackboard of intermediate results and execution information in a GUI/API hybrid framework.<br>

**GUI-KV** · 2025<br>
[GUI-KV: Efficient GUI Agents via KV Cache with Spatio-Temporal Awareness](https://arxiv.org/html/2510.00536v1)<br>
Retains historical visual-token KV states for subsequent GUI actions and prunes the cache using spatial saliency and temporal redundancy cues.<br>
[Source: §§3.2–3.3, Eqs. (8)–(9)](https://arxiv.org/html/2510.00536v1)

**GUI-Rise** · 2025<br>
[GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](https://arxiv.org/abs/2510.27210v1)<br>
Updates a compact history summary from the current screenshot and previous summary, then uses it with structured reasoning to guide later GUI actions.<br>
[Source: §§3.2–3.3, pp. 4–5](https://arxiv.org/abs/2510.27210v1)

**MapAgent** · 2025<br>
[MapAgent: Trajectory-Constructed Memory-Augmented Planning for Mobile Task Automation](https://arxiv.org/abs/2507.21953v1)<br>
Builds page memory from exploration trajectories and retrieves task-relevant pages to guide mobile planning and execution.<br>
[Source: Method, Trajectory-based Memory Mechanism and Memory-Augmented Task Planning](https://arxiv.org/abs/2507.21953v1)

[↑ Back to shelves](#shelves)

<a id="experience"></a>

### 🧭 Trajectories & Experience

Learning reusable guidance from previous interactions.

**Synapse** · 2023<br>
[Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863v3)<br>
Retrieves exemplar trajectories through task metadata; its Mind2Web exemplar pool uses the training split.<br>
[Code](https://github.com/ltzheng/Synapse)

**Agent S** · 2024<br>
[Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164v1)<br>
Retrieves successful subtask experience and writes strategy summaries back after completion.<br>
[Code](https://github.com/simular-ai/Agent-S)

**ReasoningBank** · 2025<br>
[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2)<br>
Stores structured lessons extracted from successful and failed experiences.<br>

**WebCoach** · 2025<br>
[WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997v2)<br>
Stores complete trajectory summaries after termination and retrieves experience from partial trajectories during execution.<br>

[↑ Back to shelves](#shelves)

<a id="skills"></a>

### 🛠️ Workflows & Skills

Turning interaction history into reusable procedures.

**Agent Workflow Memory** · 2024<br>
[Agent Workflow Memory](https://arxiv.org/abs/2409.07429v1)<br>
Abstracts subtask workflows from experience, replacing instance values with parameters to guide action generation.<br>
[Code](https://github.com/zorazrw/agent-workflow-memory)

**ActionEngine** · 2026<br>
[ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502v1)<br>
Records UI state transitions and retains selector-based access patterns for dynamic content.<br>

**State-Grounded Dynamic Retrieval** · 2026<br>
[Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1)<br>
Extracts local skills from trajectory windows and verifies them by substitution and re-execution.<br>

**AppAgent** · 2023<br>
[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771v3)<br>
Builds and updates UI-element documentation from exploration, then supplies page-specific guidance during deployment.<br>
[Code](https://github.com/TencentQQGYLab/AppAgent)

**Mobile-Agent-E** · 2025<br>
[Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](https://arxiv.org/abs/2501.11733v2)<br>
Reflects on plans, progress and action/error histories to form Tips and executable Shortcuts for later planning and action.<br>

**MobileGPT** · 2023 preprint / 2024 MobiCom<br>
[MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation](https://arxiv.org/html/2312.03003v3)<br>
Stores application pages and reusable subtask procedures in an app memory graph, then recalls and adapts actions to current parameters and interfaces.<br>
[Source: §§2.1, 4.1–4.2, 5.1–5.2](https://arxiv.org/html/2312.03003v3) · [Published paper](https://doi.org/10.1145/3636534.3690682)

[↑ Back to shelves](#shelves)

<a id="personalization"></a>

### 👤 User Preferences & Task Information

Reusing user context with an explicit scope.

**PersonaTrail / PACMEM** · 2026<br>
[PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails](https://arxiv.org/abs/2607.20482v2)<br>
Separates factual and preference memory from browsing history, combining semantic and temporal retrieval cues.<br>

**PersonalAlign / HIM-Agent** · 2026<br>
[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://arxiv.org/abs/2601.09636v2)<br>
Aggregates GUI user records into prototypes and updates hierarchical preference and routine-intent memory daily.<br>

**MemAgent** · 2025<br>
[MemAgent: A cache-inspired framework for augmenting conversational Web Agents with task-specific information](https://ceur-ws.org/Vol-4028/paper8.pdf)<br>
Separates task-information collection from execution and gives cached task entities an expiration policy.<br>

[↑ Back to shelves](#shelves)

<a id="maintenance"></a>

### 🔄 Maintenance & Memory Safety

Updating useful memories and handling stale or harmful content.

**HYMEM** · 2026<br>
[Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291v1)<br>
Chooses ADD, MERGE or REPLACE after retrieving neighboring experience nodes and checking redundancy.<br>

**Darwinian Memory** · 2026<br>
[Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528v1)<br>
Uses utility, time decay and execution-verification penalties to regulate retention and pruning.<br>

**PANDO** · 2026<br>
[PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/abs/2605.24785v2)<br>
Retrieves rules and programmatic skills with keywords and persistently downgrades repeatedly failing skills.<br>

**VerificAgent** · 2025<br>
[VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents](https://arxiv.org/abs/2506.02539v3)<br>
Uses expert-checked trajectory lessons, with memory frozen during test inference.<br>

**SmartSnap** · 2025<br>
[SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/html/2512.22322v1)<br>
Collects task-completion evidence screenshots and checks their validity to support mobile-task self-verification.<br>
[Source: §§3.2–3.4, Evidence Validity Check, Eq. (3)](https://arxiv.org/html/2512.22322v1)

**Environment-injected memory poisoning** · 2026<br>
[Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents](https://arxiv.org/abs/2604.02623v2)<br>
Studies how webpage content can poison saved trajectories and influence later tasks through recall.<br>

[↑ Back to shelves](#shelves)

<a id="benchmarks"></a>

### 🧪 Benchmarks & Evaluation

Read the interaction protocol alongside the reported metric.

**MemGUI-Bench · online GUI execution** · 2026<br>
[MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075v3)<br>
Evaluates Android GUI interaction with resets after failure and experience transfer across mirrored task pairs.<br>

**AndroTMem · recorded trajectories** · 2026<br>
[AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents](https://arxiv.org/abs/2603.18429v1)<br>
Evaluates state anchors and dependencies on fixed screenshots and annotated actions from recorded trajectories.<br>

**LongMemEval-V2 · memory question answering** · 2026<br>
[LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493v1)<br>
Inserts trajectories sequentially, then evaluates a fixed reader using answer accuracy and query latency.<br>

**MemGym · long-horizon environment** · 2026<br>
[MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833v1)<br>
Measures memory gain with the same reasoner while recognizing that memory can change later action distributions.<br>

**Budget-constrained web-agent study** · 2026<br>
[Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/abs/2606.15017v2)<br>
Accounts for actor, induction, synthesis, memory, retrieval and verification calls in per-task token costs.<br>

[↑ Back to shelves](#shelves)

<a id="surveys"></a>

### 📖 Related Surveys

Broader perspectives for placing GUI memory in context.

**Memory mechanisms of LLM-based agents** · 2024<br>
[A Survey on the Memory Mechanism of Large Language Model based Agents](https://arxiv.org/abs/2404.13501v1)<br>
A general introduction organized around definitions, sources, forms, operations and evaluation.<br>

**Memory in the Age of AI Agents** · 2025<br>
[Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564v2)<br>
Organizes agent memory through forms, functions and dynamics.<br>

**LLM-Brained GUI Agents** · 2024<br>
[Large Language Model-Brained GUI Agents: A Survey](https://arxiv.org/abs/2411.18279v12)<br>
Maps GUI-agent components, frameworks, data, models, evaluation and applications.<br>

**OS Agents** · 2025<br>
[OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use](https://arxiv.org/abs/2508.04482v1)<br>
Places memory within OS-agent architectures, with a dedicated discussion of memory sources, management and retrieval.<br>

**Efficient GUI Agents** · 2026<br>
[Efficient GUI Agents: A Systems Survey of Observation, Memory, Action, and Runtime Optimization](https://arxiv.org/abs/2609.02309v1)<br>
Examines summary compression, selective look-back and runtime representation compression through a systems-efficiency lens.<br>

**Long-term memory security** · 2026<br>
[A Survey on Long-Term Memory Security in LLM Agents: Attacks, Defenses, and Governance Across the Memory Lifecycle](https://arxiv.org/abs/2604.16548v2)<br>
Organizes attacks, defenses and governance across the memory lifecycle, including eTAMP and VerificAgent.<br>

**Agentic skills: systems foundations** · 2026<br>
[Towards a Systems Foundation for Agentic Skills: Architecture, Lifecycle, and Security](https://arxiv.org/abs/2608.29596v1)<br>
Connects skill discovery, representation, storage, routing, execution/repair and governance, including GUI/OS navigation.<br>

[↑ Back to shelves](#shelves)

<a id="survey"></a>

## 📘 Our Survey

**The State of Memory in GUI Agents: A Lifecycle-Centric Survey**

**Paper — Coming soon.** A public paper link and formal citation will appear here when available.

The survey examines memory in language- and vision-language-model agents operating Web, desktop and mobile interfaces. Its **lifecycle–state framework** connects five kinds of retained objects—visual evidence, interface knowledge, task state and trajectories, reusable skills, and user and session context—to six operations: writing, representation, retrieval, use, verification/recovery and updating/forgetting. Object types describe what a record is about; text, graphs and latent representations describe how it is stored.

The current synthesis draws on the [289-work classification catalogue](CATALOGUE.md), with original-source checks of retained objects and subsequent GUI uses. The framework relates maintenance operations to their objects and evaluation endpoints; assignments indicate source-supported mechanisms, rather than comparable effect sizes or field-wide prevalence.

Lifecycle operations form the main axis for comparing mechanisms; the five object categories distinguish what each operation acts on and the conditions under which that information remains useful:

| State layer | Retained content | Conditions for use and maintenance |
|---|---|---|
| **L1 Visual evidence** | Screenshots, regions and visual descriptions | Observation time, location and relevance to the current decision |
| **L2 Interface knowledge** | Element functions and interface transitions | Continued validity of functions and bindings in the current interface |
| **L3 Task state and trajectories** | Actions, confirmed effects and pending work | Distinguishing completed, pending and unconfirmed work |
| **L4 Reusable skills** | Parameterized procedures | Matching preconditions, parameter bindings and execution environments |
| **L5 User and session context** | User information, preferences and account context | Authorization, user/account scope and withdrawal conditions |

The six operations distinguish admission, organization, selection, decision use, problem detection and recovery, and revision of content or availability. Components can combine operations, and execution can revisit them. The five object categories serve a different purpose from the catalogue’s seven reading themes; compound records can involve multiple objects.

Three design tensions guide the mechanism comparisons:

| Design tension | Reading focus |
|---|---|
| **Fidelity and abstraction** | Which details survive compression or summarization, and which can be recovered for a later decision? |
| **Reuse and applicability** | Which parts of a procedure transfer, and which variable bindings or conditions need checking in the current interface? |
| **Persistence and correction** | When a record changes, which derived knowledge and active contexts must change before later actions reflect the correction? |

Separating **procedures, variable bindings and applicability conditions** helps identify what needs repair while retaining useful knowledge. Cross-layer dependencies connect observations to task facts, trajectories to skills, and user information to later plans. A stored record and the context currently consumed by an agent can therefore require different updates.

Evaluation follows the path from retained information to action: **recall, action selection on recorded observations and online execution** measure different outcomes. Comparisons account for experience, reset conditions and resource budgets; security analysis also preserves attacker access and the path from retained content to later harm. The research agenda proposes **task-resumption and cross-layer correction tests** to measure whether revisions reach later decisions while useful, unaffected knowledge remains available.

### Challenges and future directions

The survey develops six research directions from existing mechanisms and their conditions of use:

- **Memory quality and effective use**: improve admission, compression, retrieval and decision use together, measuring task gains under matched experience and budgets.
- **Abstraction with validity conditions**: connect compact procedures to applicability conditions and recoverable source evidence.
- **Task continuity under incomplete feedback**: distinguish intended actions, observed effects and unresolved confirmations, and evaluate resumption after interruption.
- **Cross-layer correction**: identify dependencies and propagate revisions while preserving utility on unaffected knowledge.
- **Experience and computation over time**: account for initial construction, repeated use, verification and maintenance costs together.
- **Scoped and interoperable interfaces**: preserve object identity, provenance, applicability and correction dependencies when replacing or sharing components.

<a id="evidence"></a>

## 🔎 Evidence & Reproducibility

Version **`evidence-20261014-v2`** provides the companion data for *The State of Memory in GUI Agents: A Lifecycle-Centric Survey*, with publication coverage through **20 September 2026**.

| Content | Scope and counts |
|---|---|
| Literature catalogue | **289 works**: 250 direct-memory and 39 evaluation or security studies, with classifications, bilingual descriptions, adopted versions and source locations |
| Object–operation matrix | **1,119 work–cell assignments** for **246 mechanism studies** |
| Corpus statistics | Counts by publication year, theme, category, analytical role and matrix cell |
| Search and selection | **13 queries across five databases**, execution dates, hit counts and selection totals |
| Documentation and validation | English and Chinese readmes, a data dictionary, CC BY 4.0 license, file checksums and an offline validation script |

- [Download the data package](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/releases/download/evidence-20261014-v2/evidence-20261014-v2.zip) · [Package overview](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/README.md) · [Zenodo](https://doi.org/10.5281/zenodo.23366556)
- [Literature catalogue](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/catalogue.csv) · [Matrix assignments](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/matrix_assignments.csv)
- [Corpus statistics](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/corpus_counts.json) · [Search records](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/search_runs.csv) · [Selection totals](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/selection_summary.json)
- [Data dictionary](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/data_dictionary.md) · [License](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/LICENSE.md) · [File checksums](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/blob/evidence-20261014-v2/releases/evidence-20261014-v2/manifest.sha256)

Validate the files, record relationships and counts with Python 3.9 or later:

```sh
cd releases/evidence-20261014-v2
python3 validate.py
```

## 🤝 Contributing

Suggest a paper, correct a link or improve a reading note through an [issue](https://github.com/kqcoxn/Awesome-GUI-Agent-Memory/issues) or pull request. Include the original paper link, a suggested shelf and one or two sentences explaining its relevance to GUI memory; code links should point to author-released implementations. Update both language versions when editing an entry. For data corrections, include the work identifier and source passage.

## 🌐 Explore Further

- [GUI Agents Paper List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List)
- [LLM-Brained GUI Agents Survey](https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey)
- [From Storage to Experience](https://github.com/FeishuLuo/Evolving-LLM-Agent-Memory-Survey)

---

<div align="center">

**English** · [简体中文](README.zh-CN.md)

From discovering papers to tracing evidence.

</div>
