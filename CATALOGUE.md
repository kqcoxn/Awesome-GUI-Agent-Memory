# GUI Agent Memory Catalogue

**English** · [简体中文](CATALOGUE.zh-CN.md) · [Curated readings](README.md#shelves) · [CSV data](catalogue.csv)

Publication cutoff: **2026-09-20**. Catalogue prepared: **2026-10-14**. **289 distinct works**: 250 direct-memory studies and 39 related evaluation/security studies.

The scope covers research in which an LLM/VLM participates in GUI decisions, actions or memory processing. Selection uses original-source evidence of retained information and its subsequent GUI use, organized by contribution to the framework; coverage may be incomplete. Every entry has a source basis for classification. Classification checks do not establish that all effect sizes or mechanism details have undergone claim-level auditing.

Themes below are reading routes, with each work listed once; they are separate from the direct-memory versus evaluation/security categories. Retained objects and uses are reviewer syntheses. Years indicate first public availability and may precede formal publication. The CSV retains stable identifiers, categories, consulted versions, bilingual descriptions and source passages; passage locators preserve the language of the verification record.

The [companion data](README.md#evidence) provide this catalogue, explicit matrix assignments, corpus statistics, executed queries and selection totals. Curated readings also include background surveys outside the catalogue scope.

[Visual history (17)](#visual) | [Interface structure and navigation (48)](#interface) | [Task state and experience (90)](#state) | [Workflows and skills (83)](#skill) | [User context and personalization (14)](#user) | [Benchmarks and evaluation (22)](#evaluation) | [Safety and reliability (15)](#security)

## Annual distribution

| First public year | Works |
|---|---:|
| 2023 | 12 |
| 2024 | 40 |
| 2025 | 103 |
| 2026* | 134 |

*2026 covers publications through 20 September. Counts describe the selected catalogue, with each work counted once; they do not estimate field-wide growth.

<a id="visual"></a>

## Visual history · 17

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2026 | <a id="mem_fc9f615907"></a>[AnchorGUI: Asymmetric Memory for Dual-Scale Learning in GUI Navigation](https://arxiv.org/abs/2609.15457v1) | Anomalous-transition screenshots and prediction errors | Guide later mobile navigation |
| 2026 | <a id="mem_fdf6f62b8b"></a>[AQuaUI: Visual Token Reduction for GUI Agents with Adaptive Quadtrees](https://arxiv.org/html/2605.19260v1) | Prior screenshots and compressed signatures | GUI grounding and subsequent actions |
| 2024 | <a id="mem_8eff266b2d"></a>[Aria-UI: Visual Grounding for GUI Instructions](https://arxiv.org/html/2412.16256v2) | Historical screenshots and actions | Ground web and mobile controls |
| 2025 | <a id="comem"></a>[Auto-scaling Continuous Memory for GUI Agent](https://arxiv.org/abs/2510.09038v1) | Screenshot and action history | Long-horizon tasks on unfamiliar interfaces |
| 2026 | <a id="mem_5dc012329c"></a>[Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction](https://arxiv.org/html/2606.29445v1) | Tutorial keyframes | Guide subsequent GUI actions |
| 2026 | <a id="gui_wf_0333"></a>[CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](https://arxiv.org/abs/2608.22577v2) | Archived high-fidelity observations | Restore visual evidence for later GUI decisions |
| 2025 | <a id="mem_b8a7ad37fe"></a>[GUI-KV: Efficient GUI Agents via KV Cache with Spatio-Temporal Awareness](https://arxiv.org/html/2510.00536v1) | Historical visual-token KV cache | Predict subsequent GUI actions |
| 2026 | <a id="gui_wf_0235"></a>[MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652v1) | Task-relevant screen events and histories | Guide long-horizon GUI actions |
| 2025 | <a id="gui_wf_0078"></a>[PAL-UI: Planning with Active Look-back for Vision-Based GUI Agents](https://arxiv.org/abs/2510.00413v2) | Historical screenshots, clues and action outcomes | Guide mobile and web navigation |
| 2026 | <a id="mem_c1851f8f2f"></a>[Rethinking Token Pruning for Historical Screenshots in GUI Visual Agents: Semantic, Spatial, and Temporal Perspectives](https://arxiv.org/html/2603.26041v1) | Historical screenshots and visual embeddings | Support subsequent navigation reasoning |
| 2024 | <a id="mem_721a3ba219"></a>[Seeing is Believing: Vision-Driven Non-Crash Functional Bug Detection for Mobile Apps](https://arxiv.org/html/2407.03037) | Sequential screenshots and testing progress | Detect non-crash errors across transitions |
| 2025 | <a id="mem_37bd08fb78"></a>[SmartSnap: Proactive Evidence Seeking for Self-Verifying Agents](https://arxiv.org/html/2512.22322v1) | Task-completion evidence screenshots | Verify mobile task completion |
| 2026 | <a id="mem_99368811d3"></a>[STaR-KV: Spatio-Temporal Adaptive Re-weighting for KV Cache Compression in GUI Vision-Language Models](https://arxiv.org/html/2606.01790v1) | Visual-token cache from prior screenshots | Support subsequent GUI-action reasoning |
| 2026 | <a id="mem_29f8342932"></a>[Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory](https://arxiv.org/abs/2604.07863v1) | Graph of screenshots, Hypertext Markup Language (HTML) and structural signals | Retrieve history for subsequent web tasks |
| 2024 | <a id="mem_e971245432"></a>[Training a Vision Language Model as Smartphone Assistant](https://arxiv.org/html/2404.08755v1) | Historical screens and actions | Guide subsequent mobile control |
| 2025 | <a id="mem_891f9b6c38"></a>[UI-Hawk: Unleashing the Screen Stream Understanding for Mobile GUI Agents](https://aclanthology.org/2025.emnlp-main.920.pdf) | Screen sequences and action histories | Choose subsequent mobile actions |
| 2026 | <a id="mem_2fb8583d04"></a>[ViBR: Automated Bug Replay from Video-Based Reports using Vision-Language Models](https://arxiv.org/html/2604.19905v1) | Historical GUI-action videos | Reproduce Android bugs |

<a id="interface"></a>

## Interface structure and navigation · 48

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2025 | <a id="mem_db766e2179"></a>[A Multimodal GUI Architecture for Interfacing with LLM-Based Conversational Assistants](https://arxiv.org/html/2510.06223v2) | Navigation tree and capability semantics | Voice-request interpretation and GUI navigation |
| 2026 | <a id="gui_wf_0156"></a>[ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory](https://arxiv.org/abs/2602.20502v1) | Page states, action templates and transitions | Online GUI execution and repair |
| 2026 | <a id="mem_5be5a7fdd4"></a>[Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution](https://arxiv.org/html/2605.28607v1) | Knowledge graph, trajectories and state differences | Execute subsequent workflow actions |
| 2025 | <a id="mem_8c1405dbc1"></a>[Agent-SAMA: State-Aware Mobile Assistant](https://ojs.aaai.org/index.php/AAAI/article/view/40187) | Screen states and action-transition machine | Mobile planning, checking and recovery |
| 2026 | <a id="mem_e606dad11b"></a>[An LLM-Driven Visual Automation Script Generation Framework for Mixed-State Testing in Industrial Applications](https://journals.sagepub.com/doi/10.3233/ATDE260391) | Interface/backend relations, assertion history and label cache | Generate visual assertions and select test actions |
| 2024 | <a id="appagentv2"></a>[AppAgent v2: Advanced Agent for Flexible Mobile Interactions](https://arxiv.org/html/2408.11824v4) | Element documentation and execution summary | Guide later mobile actions |
| 2024 | <a id="mem_e74f43e107"></a>[AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation](https://arxiv.org/html/2412.18116v3) | Interface documentation and transition dependencies | Guide subsequent mobile operations |
| 2023 | <a id="gui_add_autodroid"></a>[AutoDroid: LLM-powered Task Automation in Android](https://arxiv.org/abs/2308.15272v4) | Application functions and navigation knowledge | Execute subsequent Android tasks |
| 2024 | <a id="mem_222e458f60"></a>[AUTONODE: A Neuro-Graphic Self-Learnable Engine for Cognitive GUI Automation](https://arxiv.org/pdf/2403.10171v2) | Website structure graph | Guide later web navigation |
| 2026 | <a id="mem_1c4d93aa53"></a>[Avenir-Web: Human-Experience-Imitating Multimodal Web Agents with Mixture of Grounding Experts](https://arxiv.org/html/2602.02468v1) | Procedural web knowledge and execution reflections | Guide subsequent web actions |
| 2026 | <a id="mem_34938daf29"></a>[Breaking the Illusion: Automated Reasoning of GDPR Consent Violations](https://arxiv.org/pdf/2512.22789v1) | Consent purposes and related page information | Navigate and collect relevant web forms |
| 2026 | <a id="mem_e7f4f362da"></a>[BugRepro: enhancing android bug reproduction with domain-specific knowledge integration](https://arxiv.org/pdf/2505.14528v2) | Annotated bug steps and interface transition graph | Extract reproduction steps and navigate the app |
| 2025 | <a id="mem_8bd245235d"></a>[Building a Stable Planner: An Extended Finite State Machine Based Planning Module for Mobile GUI Agent](https://arxiv.org/html/2505.14141v1) | Application states and transitions | Execute later mobile paths |
| 2026 | <a id="mem_3cd49de261"></a>[ColorBrowserAgent: Complex Long-Horizon Browser Agent with Adaptive Knowledge Evolution](https://arxiv.org/html/2601.07262v3) | Web expertise and evolving experience | Guide subsequent browser actions |
| 2026 | <a id="mem_a1874e29bf"></a>[Curiosity Driven Knowledge Retrieval for Mobile Agents](https://arxiv.org/pdf/2601.19306v1) | AppCards: functions, parameters and interface mappings | Guide multistep mobile operations |
| 2026 | <a id="mem_6acef98d3f"></a>[From GUI Tests to Conversational Interaction: A New Perspective on App-Specific Voice Assistants](https://arxiv.org/pdf/2607.11387v1) | Test-derived capabilities, intents and plans | Map voice requests to application actions |
| 2025 | <a id="mem_c0036ba3fe"></a>[From Redundancy to Efficiency: Exploiting Shared UI Interactions towards Efficient LLM-Based Testing](https://tskghs17.github.io/papers/wang2025testweaver.pdf) | Annotated transition graph and cached actions | Reuse shared interactions across mobile tests |
| 2025 | <a id="mem_2d7d77d00e"></a>[From User Interface to Agent Interface: Efficiency Optimization of UI Representations for LLM Agents](https://arxiv.org/html/2512.13438v1) | Interface transformation programs | Prepare later web-decision inputs |
| 2025 | <a id="mem_6167a7446c"></a>[Go-Browse: Training Web Agents with Structured Exploration](https://arxiv.org/html/2506.03533v2) | Web graph, exploration frontier and action history | Guide subsequent browser exploration |
| 2026 | <a id="gui_wf_0373"></a>[Graph-Structured Persistent Memory for Efficient LLM-Based Computer Use Agents](https://doi.org/10.3390/axioms15060415) | GUI states and executable paths | Reuse desktop subtasks |
| 2026 | <a id="graphdroid"></a>[GraphDroid: Asynchronous LLM-Based Mobile App GUI Testing via History-Aware Exploration and Hybrid Intent Fulfillment](https://arxiv.org/html/2609.10031v1) | Transition graph and functional clusters | Guide subsequent mobile testing |
| 2026 | <a id="mem_86cae9112f"></a>[GraphPilot: GUI Task Automation with One-Step LLM Reasoning Powered by Knowledge Graph](https://arxiv.org/html/2601.17418v1) | Page functions and transition graph | Guide subsequent mobile tasks |
| 2025 | <a id="mem_f0e871bcdb"></a>[Grounded Test-Time Adaptation for LLM Agents](https://arxiv.org/html/2511.04847v1) | Web-environment transition knowledge | Execute tasks on new WebArena sites |
| 2025 | <a id="mem_80ec58d665"></a>[GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/) | State-action-outcome knowledge | Guide navigation in target mobile apps |
| 2025 | <a id="mem_aceb660bb5"></a>[Improving Language Agents through BREW: Bootstrapping expeRientially-learned Environmental knoWledge](https://arxiv.org/html/2511.20297v2) | Documents of experiential environment knowledge | Guide later desktop actions |
| 2024 | <a id="mem_655ee4e4a6"></a>[Improving Web Element Localization by Using a Large Language Model](https://arxiv.org/pdf/2310.02046v1) | Element attributes from an earlier website version | Locate corresponding elements after changes |
| 2025 | <a id="mem_35d568c4f4"></a>[InfraMind: A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management](https://arxiv.org/html/2509.13704v1) | Industrial GUI elements and successful workflows | Guide later industrial automation |
| 2025 | <a id="mem_a6fb9e1b79"></a>[KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.274/) | Interface transition graph | Plan mobile navigation paths |
| 2025 | <a id="mem_9d976f07bc"></a>[KuiTest: Leveraging Knowledge in the Wild as GUI Testing Oracle for Mobile Apps](https://tskghs17.github.io/papers/hu2025kuitest.pdf) | Icon library and functional descriptions | Predict element functions and verify responses |
| 2024 | <a id="mem_b51478fe80"></a>[Large Language User Interfaces: Voice Interactive User Interfaces Powered by LLMs](https://arxiv.org/html/2402.07938v2) | Interface metadata, states and annotated trees | Guide later voice-driven GUI operations |
| 2026 | <a id="mem_a80fc6b0ea"></a>[Learning to Adapt: Self-Improving Web Agent via Cognitive-Aware Exploration](https://arxiv.org/abs/2605.31365v1) | Explored states, URLs, transitions and coverage | Plan uncovered exploration and backtracking |
| 2025 | <a id="mem_4c210c8eab"></a>[LLM-Explorer: Towards Efficient and Affordable LLM-based Exploration for Mobile Apps](https://arxiv.org/html/2505.10593v1) | Application-exploration knowledge | Guide subsequent mobile exploration |
| 2025 | <a id="mem_26e88d6b7a"></a>[LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance](https://tmliu06.github.io/pdfs/llmdroid-fse2025.pdf) | Visited pages and functional summaries | Guide subsequent mobile testing |
| 2023 | <a id="mem_7e656ec648"></a>[Make LLM a Testing Expert: Bringing Human-Like Interaction to Mobile GUI Testing via Functionality-Aware Decisions](https://arxiv.org/html/2310.15780v1) | Functional knowledge from testing | Guide subsequent mobile exploration |
| 2025 | <a id="mem_9c79ad23f3"></a>[MapAgent: Trajectory-Constructed Memory-Augmented Planning for Mobile Task Automation](https://arxiv.org/abs/2507.21953v1) | Page-layout and function snapshots | Plan and execute mobile tasks |
| 2025 | <a id="mem_cc179f2ee3"></a>[PG-Agent: An Agent Powered by Page Graph](https://arxiv.org/html/2509.03536v1) | Page-transition graph and interface guides | Plan navigation in unseen GUI scenarios |
| 2025 | <a id="mem_a7d48888e2"></a>[ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps](https://tingsu.github.io/files/fse2025-ProphetAgent.pdf) | Semantic interface transition graph | Generate executable mobile testing paths |
| 2026 | <a id="mem_fb8a22e354"></a>[Region4Web: Rethinking Observation Space Granularity for Web Agents](https://arxiv.org/html/2605.07134v1) | Page-region function summaries | Guide subsequent web actions |
| 2026 | <a id="mem_8d2b4314ae"></a>[Reproducing UI contexts described in app reviews with large language models](https://tmliu06.github.io/pdfs/ui-contexts-asej2026.pdf) | Pre-explored interface state library | Reach mobile screens described in reviews |
| 2026 | <a id="mem_ce89d4f027"></a>[Social-Annotate: Self-Healing Browser Extension to Annotate and Collect Social Media Data](https://arxiv.org/html/2607.01460v1) | Target selectors and structural changes | Maintain later browser-extension operations |
| 2025 | <a id="mem_96957a7efd"></a>[Temac: Multi-Agent Collaboration for Automated Web GUI Testing](https://arxiv.org/html/2506.00520v1) | Transition graph and coverage records | Guide targeted web testing |
| 2026 | <a id="mem_b49a013559"></a>[Testing Text Input Components of Web Applications Based on Large Language Models; &#91;基于大语言模型的 Web 文本输入组件测试方法&#93;](https://www.ejournal.org.cn/rc-pub/front/front-article/download/153611942/lowqualitypdf/Testing%20Text%20Input%20Components%20of%20Web%20Applications%20Based%20on%20Large%20Language%20Models.pdf) | Element context and testing results | Guide web-form input testing |
| 2026 | <a id="mem_f1e4fb7771"></a>[UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided GUI Agents](https://arxiv.org/html/2605.29534v1) | Application states and transition graph | Guide subsequent mobile tasks |
| 2025 | <a id="mem_7fbe083c3a"></a>[UICOMPASS: UI Map Guided Mobile Task Automation via Adaptive Action Generation](https://aclanthology.org/2025.emnlp-main.1346.pdf) | Interface graph and action history | Navigate and revise mobile paths |
| 2025 | <a id="mem_9c52f9d28f"></a>[WebATLAS: An LLM Agent with Experience-Driven Memory and Action Simulation](https://arxiv.org/abs/2510.22732v2) | Website map and interaction outcomes | Navigate unfamiliar websites |
| 2026 | <a id="mem_bbe1ea2894"></a>[WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/html/2606.10423v1) | Page hierarchy and element-behavior map | Guide subsequent web tasks |
| 2024 | <a id="mem_e17bac36bb"></a>[WebMap: Improving LLM Web Agents with Semantic Search for Relevant Web Pages](https://nlp.fi.muni.cz/raslan/2024/paper5.pdf) | Preprocessed web-navigation resources | Locate resources for later web tasks |
| 2026 | <a id="mem_5e44ec43ce"></a>[WebTestPilot: Agentic End-to-End Web Testing against Natural Language Specification by Inferring Oracles with Symbolized GUI Elements](https://arxiv.org/html/2602.11724v1) | Element symbols and cross-state dependencies | Verify web-interface behavior |

<a id="state"></a>

## Task state and experience · 90

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2026 | <a id="mem_cf78c6ae73"></a>[A Subgoal-driven Framework for Improving Long-Horizon LLM Agents](https://arxiv.org/html/2603.19685v1) | Interaction history and subgoals | Web navigation and progress assessment |
| 2023 | <a id="mem_93a681a63e"></a>[A Zero-Shot Language Agent for Computer Control with Structured Reflection](https://arxiv.org/html/2310.08740v3) | Action errors and structured reflections | Subsequent MiniWoB actions |
| 2025 | <a id="gui_wf_0027"></a>[Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906v1) | Shared context and specialist execution state | Coordinate desktop and mobile actions |
| 2026 | <a id="mem_aa54ce666c"></a>[AgentExplorer: Parallel Online Exploration for Enhancing On-Device Mobile GUI Agents](https://doi.org/10.1109/fmsys72110.2026.00011) | Exploration branches, history and outcomes | Guide subsequent mobile decisions |
| 2025 | <a id="mem_38af3cf8ff"></a>[Aime: Towards Fully-Autonomous Multi-Agent Framework](https://arxiv.org/html/2507.11988v2) | Task hierarchy, completion and feedback | Replan web tasks |
| 2023 | <a id="mem_4832b985b4"></a>[AllTogether: Investigating the Efficacy of Spliced Prompt for Web Navigation using Large Language Models](https://arxiv.org/html/2310.18331v1) | Web action history | Select later HTML element actions |
| 2024 | <a id="mem_4dbf6df898"></a>[Android in the Zoo: Chain-of-Action-Thought for GUI Agents](https://arxiv.org/html/2403.02713v2) | Action descriptions and previous outcomes | Choose subsequent mobile actions |
| 2026 | <a id="gui_wf_0179"></a>[AndroTMem: From Interaction Trajectories to Anchored Memory in Long-Horizon GUI Agents](https://arxiv.org/abs/2603.18429v1) | State anchors and dependencies | Predict actions and maintain mobile task state |
| 2025 | <a id="mem_5c25220256"></a>[AppCopilot: Toward General, Accurate, Long-Horizon, and Efficient Mobile Agent](https://arxiv.org/abs/2509.02444v2) | Queries, screenshots, action sequences and shared data | Match and replay tasks; supply cross-app inputs |
| 2023 | <a id="mem_4aff73538a"></a>[Autonomous Large Language Model Agents Enabling Intent-Driven Mobile GUI Testing](https://arxiv.org/html/2311.08649v1) | Testing history and spatial memory | Guide subsequent mobile testing |
| 2026 | <a id="mem_cc84562bba"></a>[AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling](https://arxiv.org/html/2604.27253v1) | Exploration queue, visited pages and paths | Avoid repeated exploration and reconstruct navigation prefixes |
| 2025 | <a id="gui_chain_r1_wf_0269"></a>[BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://aclanthology.org/2025.emnlp-main.212/) | Prior action states and error evidence | Backtrack and recover mobile execution |
| 2026 | <a id="mem_0041b9067c"></a>[BEAP-Agent: Backtrackable Execution and Adaptive Planning for GUI Agents](https://doi.org/10.1109/icassp55912.2026.11464343) | Failed branches, trajectories and subtask state | Backtrack and replan desktop execution |
| 2025 | <a id="gui_wf_0346"></a>[Beyond Static GUI Agent: Evolving LLM-based GUI Testing via Dynamic Memory](https://doi.org/10.1109/ase63991.2025.00135) | Functional traces, reflections and exploration strategies | Guide testing away from ineffective paths |
| 2025 | <a id="mem_07db8f0fb4"></a>[Branch-and-Browse: Efficient and Controllable Web Exploration with Tree-Structured Reasoning and Action Memory](https://arxiv.org/html/2510.19838v2) | Exploration tree and page-action history | Guide subsequent web navigation |
| 2025 | <a id="mem_936b23119b"></a>[BrowserAgent: Building Web Agents with Human-Inspired Web Browsing Actions](https://arxiv.org/html/2510.10666v2) | Browsing history and key findings | Guide subsequent browsing |
| 2026 | <a id="mem_52b7dc4ee0"></a>[CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/html/2603.24157v1) | Clinical GUI history and correction feedback | Guide healthcare software operations |
| 2025 | <a id="gui_wf_0046"></a>[Chain-of-Memory: Enhancing GUI Agents for Cross-Application Navigation](https://arxiv.org/abs/2506.18158v1) | Action descriptions and salient screen information | Navigate across applications |
| 2024 | <a id="mem_fbc3b0000a"></a>[CoCo-Agent: A Comprehensive Cognitive MLLM Agent for Smartphone GUI Automation](https://arxiv.org/html/2402.11941v3) | Mobile interaction records | Choose subsequent mobile actions |
| 2025 | <a id="mem_e50500ac57"></a>[COLA: Collaborative Multi-Agent Framework with Dynamic Task Scheduling for GUI Automation](https://aclanthology.org/2025.emnlp-main.227.pdf) | Execution state and rollback points | Recover GUI task execution |
| 2025 | <a id="mem_1837b0096d"></a>[CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs](https://arxiv.org/html/2510.15455v1) | Mobile decision history | Choose subsequent clicks and text input |
| 2025 | <a id="mem_a8771ae780"></a>[D-Artemis: A Deliberative Cognitive Framework for Mobile GUI Multi-Agents](https://arxiv.org/html/2509.21799v3) | Task hints and working memory | Guide subsequent mobile operations |
| 2026 | <a id="mem_33b716376d"></a>[Does The Way You Plan Matter? An Empirical Study of Planning Representations for LLM Web Agents](https://arxiv.org/html/2605.29927v1) | Subgoal lists and pseudocode plans | Guide subsequent WebArena actions |
| 2026 | <a id="mem_37c7b428f4"></a>[Don't Act Blindly: Robust GUI Automation via Action-Effect Verification and Self-Correction](https://arxiv.org/html/2604.05477v1) | Actions, expected effects and verification feedback | Correct subsequent GUI execution |
| 2024 | <a id="mem_9f0255f977"></a>[Dynamic Planning for LLM-based Graphical User Interface Automation](https://arxiv.org/html/2410.00467v3) | Execution history and dynamic plans | Guide subsequent GUI actions |
| 2026 | <a id="mem_627406dbf7"></a>[Falsifiable Commitment Planning for Self-Correcting Web Agents](https://arxiv.org/html/2607.24167v1) | Plan commitments, skills and repair experience | Guide subsequent WebArena actions |
| 2026 | <a id="mem_5dbe38d0ef"></a>[Fixpad++: Automated Bug Fix Verification using LLM Agents](https://www.researchgate.net/publication/403258864_Fixpad_Automated_Bug_Fix_Verification_Using_LLM_Agents) | Reproduction trajectories and reflection feedback | Choose desktop reproduction actions; replay patch checks |
| 2026 | <a id="gui_wf_0317"></a>[FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory](https://arxiv.org/abs/2608.04530v1) | Factorized latent content and trust signal | Read memory for subsequent web actions |
| 2026 | <a id="mem_0e23d7fb68"></a>[From Bug Reports to Browser-Executable Procedures: An LLM-Driven Agent for Web GUI Bug Reproduction](https://arxiv.org/html/2608.03598v1) | Bug plans, resource inventories and execution traces | Guide browser reproduction steps |
| 2024 | <a id="mem_075cbf2661"></a>[From Context to Action: Analysis of the Impact of State Representation and Context on the Generalization of Multi-Turn Web Navigation Agents](https://arxiv.org/html/2410.23555v1) | Web interaction history | Select subsequent web elements |
| 2025 | <a id="mem_6ee83388ce"></a>[General Agentic Planning Through Simulative Reasoning with World Models](https://arxiv.org/html/2507.23773v3) | World model and simulated trajectories | Plan subsequent browser actions |
| 2024 | <a id="mem_11da797c0d"></a>[GUARDIAN: A Runtime Framework for LLM-Based UI Exploration](https://dezhi-ran.com/publication/issta24-guardian/issta24-guardian.pdf) | Visited states, actions and blocked-action sets | Choose testing actions and backtrack after failure |
| 2025 | <a id="mem_c506ef96b2"></a>[GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](https://arxiv.org/abs/2510.27210v1) | Task progress and action summaries | Guide subsequent GUI navigation |
| 2024 | <a id="mem_d3ec2da938"></a>[GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451v2) | Historical screenshots, actions and summaries | Guide cross-app mobile navigation |
| 2026 | <a id="mem_9bbb29905d"></a>[GUITester: Enabling GUI Agents for Exploratory Defect Discovery](https://arxiv.org/html/2601.04500v1) | Testing subtasks and execution history | Guide later defect exploration |
| 2025 | <a id="mem_85b940ac68"></a>[History-Aware Reasoning for GUI Agents](https://ojs.aaai.org/index.php/AAAI/article/view/40966) | Interaction history and correction rules | Guide decisions and error recovery |
| 2026 | <a id="mem_2e790649cf"></a>[HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents](https://arxiv.org/html/2607.14548v1) | Mobile step history | Choose subsequent mobile actions |
| 2023 | <a id="mem_bc9314e21c"></a>[LASER: LLM Agent with State-Space Exploration for Web Navigation](https://arxiv.org/html/2309.08172v2) | Web states and exploration history | Guide subsequent web navigation |
| 2024 | <a id="mem_29565e9bba"></a>[LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing](https://arxiv.org/pdf/2402.10294v1) | Dialogue, video summaries and frame descriptions | Guide later GUI timeline editing |
| 2026 | <a id="mem_27213371dd"></a>[LDMDroid: Leveraging LLMs for Detecting Data Manipulation Errors in Android Apps](https://arxiv.org/pdf/2604.00458v2) | Action history, change summaries and testing progress | Explore Android data-manipulation defects |
| 2025 | <a id="mem_37b8090ed4"></a>[Learning GUI Grounding with Spatial Reasoning from Visual Feedback](https://arxiv.org/html/2509.21552v1) | Cursor history and spatial relations | Choose subsequent cursor movements |
| 2025 | <a id="mem_358154d3a0"></a>[LegalWebAgent: Empowering Access to Justice via LLM-Based Web Agents](https://arxiv.org/html/2512.04105v1) | Task information gathered from earlier pages | Operate legal forms and schedules |
| 2025 | <a id="mem_ee67b1add7"></a>[Less is More: Empowering GUI Agent with Context-Aware Simplification](https://arxiv.org/html/2507.03730v1) | Prior screens and interaction context | Guide web and mobile navigation |
| 2025 | <a id="mem_132daa5f0a"></a>[LightAgent: Mobile Agentic Foundation Models](https://arxiv.org/html/2510.22009v1) | Mobile interaction history | Guide subsequent mobile actions |
| 2026 | <a id="mem_8fc549d94a"></a>[LLM-as-Code: Agentic Programming for Agent Harness](https://arxiv.org/html/2606.15874v1) | Call-tree execution history | Guide subsequent computer actions |
| 2025 | <a id="mem_47ed45cdbb"></a>[LLM-Empowered Scriptless Functional Testing](https://doi.org/10.1109/qrs65678.2025.00012) | Recent actions, achieved goals and transition model | Choose later web test actions and check goals |
| 2025 | <a id="mem_0e7c9a6a76"></a>[LLM-Guided Scenario-based GUI Testing](https://arxiv.org/html/2506.05079v1) | GUI operations and testing history | Choose subsequent scenario-based mobile tests |
| 2026 | <a id="gui_wf_0337"></a>[LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents](https://arxiv.org/abs/2608.25777v1) | Subgoals, evidence and runtime feedback | Guide subsequent desktop actions |
| 2026 | <a id="mem_f2bc990ed3"></a>[M$^2$: Dual-Memory Augmentation for Long-Horizon Web Agents via Trajectory Summarization and Insight Retrieval](https://arxiv.org/abs/2603.00503v1) | Trajectory summaries and retrieved insights | Guide long-horizon web navigation |
| 2026 | <a id="mem_970c5d5d71"></a>[Mango: Multi-Agent Web Navigation via Global-View Optimization](https://arxiv.org/html/2604.18779v1) | Historical navigation attempts | Guide subsequent web navigation |
| 2026 | <a id="gui_wf_0222"></a>[Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1) | Latent persistent interaction state | Condition later web and mobile decisions |
| 2026 | <a id="mem_c72a11d0bd"></a>[MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management](https://arxiv.org/abs/2606.19926v1) | Folded action history and interface states | Guide subsequent cross-app mobile actions |
| 2025 | <a id="mga"></a>[MGA: Memory-Driven GUI Agent for Observation-Centric Interaction](https://arxiv.org/html/2510.24168v1) | Screen-state differences and transition chains | Guide long-horizon desktop tasks |
| 2025 | <a id="mem_11cdbbfd00"></a>[MobA: Multifaceted Memory-Enhanced Adaptive Planning for Efficient Mobile Task Automation](https://aclanthology.org/2025.naacl-demo.43/) | Task outcomes, page interactions and preferences | Retrieve and adapt mobile plans |
| 2026 | <a id="mem_b53aef7406"></a>[MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration](https://arxiv.org/html/2605.26546v1) | Exploration traces and interface hints | Choose subsequent mobile actions |
| 2025 | <a id="mem_e66cca9ab5"></a>[MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation](https://papers.neurips.cc/paper_files/paper/2025/file/3994410d63ec68ce9a66011a34c9a2c4-Paper-Conference.pdf) | Execution errors and exploration findings | Recover long-horizon mobile execution |
| 2026 | <a id="mem_ddb97803ba"></a>[Navigating the Infinite Dynamic Web Space: Effective In-Context Exploration via Cognitive Multi-Agent Collaboration](https://aclanthology.org/2026.eacl-long.384.pdf) | Observation histories and action trajectories | Navigate and backtrack on dynamic websites |
| 2024 | <a id="mem_e070b3ae22"></a>[On the Multi-turn Instruction Following for Conversational Web Agents](https://aclanthology.org/2024.acl-long.477/) | Multiturn dialogue and web interactions | Guide subsequent conversational navigation |
| 2026 | <a id="mem_483b6e1939"></a>[OpAgent: Operator Agent for Web Navigation](https://arxiv.org/abs/2602.13559v2) | Reasoning/action history, checklists, hints and notes | Plan later browser navigation from feedback |
| 2026 | <a id="gui_wf_0124"></a>[OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent](https://arxiv.org/abs/2601.07779v1) | Milestones and application tutorials | Guide long-horizon desktop tasks |
| 2024 | <a id="mem_6f8e302e89"></a>[OSCAR: Operating System Control via State-Aware Reasoning and Re-Planning](https://arxiv.org/html/2410.18963v1) | Workflow state and execution plans | Guide desktop and mobile actions |
| 2025 | <a id="mem_9a999b5414"></a>[PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC](https://arxiv.org/html/2502.14282v1) | Subtask progress and error feedback | Coordinate cross-application desktop tasks |
| 2025 | <a id="mem_b964a8de67"></a>[PLAN-AND-ACT: Improving Planning of Agents for Long-Horizon Tasks](https://arxiv.org/html/2503.09572v1) | Structured high-level task plans | Guide long-horizon web actions |
| 2026 | <a id="mem_2cc9e86940"></a>[Plan-MCTS: Plan Exploration for Action Exploitation in Web Navigation](https://arxiv.org/html/2602.14083v1) | Abstract semantic history | Plan subsequent web navigation |
| 2026 | <a id="mem_9341bec452"></a>[Planner Matters! An Efficient and Unbalanced Multi-agent Collaboration Framework for Long-horizon Planning](https://arxiv.org/html/2605.02168v1) | Long-term task context | Guide later web and desktop actions |
| 2026 | <a id="mem_4eadbdd6f9"></a>[Read More, Think More: Revisiting Observation Reduction for Web Agents](https://arxiv.org/html/2604.01535v1) | Historical web observations and interface differences | Guide subsequent web actions |
| 2026 | <a id="mem_56411d8457"></a>[SecAgent: Efficient Mobile GUI Agent with Semantic Context](https://arxiv.org/html/2603.08533v1) | Semantic interface and action summaries | Guide subsequent mobile navigation |
| 2026 | <a id="mem_a6a464584a"></a>[See and Remember: A Multimodal Agent for Web Traversal](https://arxiv.org/html/2603.02626v1) | Structured traversal paths | Navigate and backtrack on websites |
| 2025 | <a id="mem_cc0284e6e2"></a>[See, Think, Act: Online Shopper Behavior Simulation with VLM Agents](https://arxiv.org/html/2510.19245v1) | Web observations and action history | Predict subsequent GUI actions |
| 2026 | <a id="mem_96bab57611"></a>[Speech-visual integration multimodal multi-agents framework for mobile operation](https://link.springer.com/content/pdf/10.1007/s44443-026-00584-y.pdf) | Operation state, task templates and user habits | Resume and reuse mobile operations |
| 2026 | <a id="mem_eee7e82c40"></a>[Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/html/2604.27151v1) | Recent reasoning/actions and task milestones | Guide later computer actions |
| 2026 | <a id="mem_7611155082"></a>[StepReflect: Structured UI Transition Reflection for Mobile GUI Agents](https://arxiv.org/html/2608.05587v1) | Previous/current screens and expected transitions | Correct subsequent mobile execution |
| 2026 | <a id="mem_59bee19263"></a>[StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](https://arxiv.org/html/2607.11388v1) | Verifiable progress, modifications and failures | Guide subsequent computer tasks |
| 2026 | <a id="mem_f24837cee4"></a>[STRUCTUREDAGENT: Planning with AND/OR Trees for Long-Horizon Web Tasks](https://arxiv.org/html/2603.05294v1) | Plan trees, subgoals and execution state | Guide long-horizon web tasks |
| 2025 | <a id="mem_effc1923f1"></a>[Surfer 2: The Next Generation of Cross-Platform Computer Use Agents](https://arxiv.org/html/2510.19949v1) | Long-horizon task context | Guide web, desktop and mobile actions |
| 2025 | <a id="mem_37a149a962"></a>[Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/html/2511.22235v1) | Task progress and execution context | Schedule long-horizon GUI actions |
| 2024 | <a id="mem_2efe59c925"></a>[Tree Search for Language Model Agents](https://jykoh.com/search-agents/paper.pdf) | Search-tree states and trial outcomes | Plan real web interactions |
| 2025 | <a id="mem_dd64174a7b"></a>[TreeMind: Automatically Reproducing Android Bug Reports via LLM-empowered Monte Carlo Tree Search](https://arxiv.org/html/2509.22431v1) | Explored GUI action history | Navigate Android bug reproduction |
| 2025 | <a id="mem_ad5250d497"></a>[UFO3: Weaving the Digital Agent Galaxy](https://arxiv.org/abs/2511.11332v2) | Device-agent progress and execution results | Update context for later Windows GUI decisions |
| 2026 | <a id="mem_313d2389fe"></a>[UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/html/2604.13822v1) | Persistent observations and task context | Guide subsequent GUI tasks |
| 2026 | <a id="mem_16729366f4"></a>[VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/html/2606.24525v1) | Pre-action and post-action visual states | Correct subsequent GUI actions |
| 2026 | <a id="mem_cf6e59941f"></a>[VLAA-GUI: Knowing When to Stop, Recover, and Search, A Modular Framework for GUI Automation](https://arxiv.org/html/2604.21375v1) | Failed actions and repeated screen states | Recover subsequent desktop execution |
| 2024 | <a id="mem_d6240e522a"></a>[WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://arxiv.org/html/2402.05930v1) | Web actions and screen history | Guide conversational navigation |
| 2025 | <a id="mem_22cd31f6ad"></a>[WebOperator: Action-Aware Tree Search for Autonomous Agents in Web Environment](https://arxiv.org/html/2512.12692v1) | Browser paths and action candidates | Backtrack during web tasks |
| 2024 | <a id="mem_b621b90477"></a>[WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration](https://arxiv.org/html/2408.15978v1) | Task plans, progress and previous attempts | Guide subsequent web exploration |
| 2025 | <a id="mem_7bb832d88d"></a>[WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms](https://arxiv.org/html/2504.11788v1) | Navigation paths and previous states | Roll back and search web paths |
| 2025 | <a id="mem_6016a9ab72"></a>[WebRouter: Query-specific Router via Variational Information Bottleneck for Cost-sensitive Web Agent](https://arxiv.org/html/2510.11221v1) | Action history and page state | Route subsequent web operations to models |
| 2025 | <a id="mem_47f0d52734"></a>[WebSight: A Vision-First Architecture for Robust Web Agents](https://arxiv.org/html/2508.16987v1) | Task episodes | Navigate and verify web actions |
| 2026 | <a id="gui_wf_0298"></a>[What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States](https://arxiv.org/abs/2606.31612v2) | Active task-driving states | Guide subsequent mobile planning |
| 2023 | <a id="mem_3f85fad284"></a>[You Only Look at Screens: Multimodal Chain-of-Action Agents](https://arxiv.org/html/2309.11436v1) | Action history and pending plans | Choose subsequent mobile actions |

<a id="skill"></a>

## Workflows and skills · 83

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2024 | <a id="mem_bd2603acc5"></a>[AdaptAgent: Adapting Multimodal Web Agents with Few-Shot Learning from Human Demonstrations](https://arxiv.org/html/2411.13451v1) | Human web demonstrations | Adapt subsequent web task execution |
| 2024 | <a id="gui_wf_0469"></a>[AGENT S: AN OPEN AGENTIC FRAMEWORK THAT USES COMPUTERS LIKE A HUMAN](https://arxiv.org/abs/2410.08164v1) | Application knowledge and task experience | Desktop planning and execution |
| 2024 | <a id="gui_add_awm"></a>[Agent Workflow Memory](https://arxiv.org/abs/2409.07429v1) | Parameterized workflows from prior tasks | Guide subsequent web actions |
| 2024 | <a id="mem_e6c10c610b"></a>[AGENTTREK: AGENT TRAJECTORY SYNTHESIS VIA GUIDING REPLAY WITH WEB TUTORIALS](https://arxiv.org/html/2412.09605v2) | Web tutorials and guided trajectories | Guide GUI replay during training-data generation |
| 2025 | <a id="mem_aafd37bfbc"></a>[ALLOY: Generating Reusable Agent Workflows from User Demonstration](https://arxiv.org/html/2510.10049v1) | Workflow templates from user demonstrations | Reuse procedures across web tasks |
| 2023 | <a id="gui_add_appagent"></a>[AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771v3) | Application-operation knowledge | Select mobile operation sequences |
| 2025 | <a id="appagentx"></a>[AppAgentX: Evolving GUI Agents as Proficient Smartphone Users](https://arxiv.org/html/2503.02268v3) | Page transitions and action outcomes | Guide later mobile operations |
| 2024 | <a id="mem_377cdc507a"></a>[Auto-Intent: Automated Intent Discovery and Self-Exploration for Large Language Model Web Agents](https://arxiv.org/html/2410.22552v1) | Demonstrations and discovered action intents | Predict later web actions |
| 2024 | <a id="mem_9377e9276f"></a>[AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents](https://arxiv.org/abs/2403.08978v2) | Context-dependent navigation guidelines | Select applicable guidance for web actions |
| 2025 | <a id="mem_1b0c025efd"></a>[Automated Test Transfer across Android Apps using Large Language Models](https://seal.ics.uci.edu/publications/2025_ISSTA.pdf) | Source test events and semantic abstractions | Generate GUI events in a target Android app |
| 2023 | <a id="mem_33b60a25fc"></a>[Automatic Macro Mining from Interaction Traces at Scale](https://arxiv.org/html/2310.07023v2) | Interaction traces and replayable macros | Execute later mobile macros |
| 2026 | <a id="mem_8094943a75"></a>[AutoRPA: Efficient GUI Automation through LLM-Driven Code Synthesis from Interactions](https://arxiv.org/html/2605.21082v1) | GUI trajectory library | Generate and execute automation code |
| 2024 | <a id="mem_4773250d93"></a>[BAGEL: Bootstrapping Agents by Guiding Exploration with Language](https://arxiv.org/abs/2403.08140v2) | Synthetic instructions and demonstrations | Retrieve examples for MiniWoB++ actions |
| 2026 | <a id="mem_6f421e4af8"></a>[Beyond Browser Agents: Distilling Experience for Accessible Web Automation](https://doi.org/10.1145/3800424.3800431) | Successful trajectories, compiled scripts and repair fragments | Repeat web tasks and repair local failures |
| 2026 | <a id="mem_637c6dc8ce"></a>[Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns](https://arxiv.org/html/2606.17645v1) | Transferable interaction skills | Reuse actions across websites |
| 2026 | <a id="mem_62a54557e6"></a>[CAPTCHAs in the Agentic Era: Solvers That Learn from Every Encounter](https://arxiv.org/html/2609.02393v1) | Historical visual verification challenges and model labels | Guide visual solving and clicking |
| 2025 | <a id="mem_efe0271b79"></a>[CHOP: Mobile Operating Assistant with Constrained High-frequency Optimized Subtask Planning](https://arxiv.org/html/2503.03743v1) | Frequent mobile subtask library | Plan later mobile actions |
| 2026 | <a id="mem_e5ebc58e38"></a>[CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications](https://arxiv.org/html/2608.11588v1) | Workflow steps, failures and recovery experience | Guide actions in unseen mobile apps |
| 2026 | <a id="mem_d63ba396ed"></a>[Context-Aware Functional Test Generation via Business Logic Extraction and Adaptation](https://arxiv.org/html/2602.24108v1) | Historical tests and business logic | Generate target-application GUI tests |
| 2025 | <a id="mem_e7fb5956b9"></a>[Contextual Experience Replay for Self-Improvement of Language Agents](https://arxiv.org/html/2506.06698v1) | Distilled experience and dynamic replay buffer | Guide subsequent web tasks |
| 2025 | <a id="mem_b190e0f2ed"></a>[Cracking the Code of Action: a Generative Approach to Affordances for Reinforcement Learning](https://arxiv.org/html/2504.17282v1) | Code describing feasible GUI actions | Constrain later MiniWoB++ actions |
| 2025 | <a id="mem_9179d638a4"></a>[Cybernaut: Towards Reliable Web Automation](https://arxiv.org/html/2508.16688v1) | Demonstrations and operating procedures | Execute later enterprise web tasks |
| 2026 | <a id="gui_wf_0134"></a>[Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528v1) | Reusable trajectory units | Guide later cross-application tasks |
| 2026 | <a id="mem_9de61577a9"></a>[Domain Adaptation of MLLM-Based GUI Agents in Documentation-Rich Environments with Standard Operating Procedures](https://doi.org/10.1007/978-981-92-2856-0_34) | Manual pages and task-specific screen sequences | Plan cockpit GUI operations |
| 2026 | <a id="gui_wf_0242"></a>[DRIVE: Modeling Skills at the Reasoning and Interaction Levels for Web Agents under Continual Learning](https://arxiv.org/abs/2605.23939v1) | Reasoning and interaction skills | Retrieve and update skills for web navigation |
| 2025 | <a id="mem_fb97493684"></a>[EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/html/2512.19396v3) | Exploration traces and consolidated memory | Guide subsequent GUI tasks |
| 2026 | <a id="mem_b8dede6c76"></a>[EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/html/2604.09815v1) | GUI and Model Context Protocol (MCP) trajectories and learned strategies | Guide later computer actions |
| 2024 | <a id="mem_f3dec444a3"></a>[Enabling Cost-Effective UI Automation Testing with Retrieval-Based LLMs: A Case Study in WeChat](https://researchmgt.monash.edu/ws/files/694588803/652457437.pdf) | Task descriptions and operation examples | Generate actions for new GUI tests |
| 2026 | <a id="mem_a9ac62b770"></a>[Enhancing Web Agents with a Hierarchical Memory Tree](https://arxiv.org/abs/2603.07024v1) | Hierarchical workflows and semantic action patterns | Guide cross-website actions |
| 2026 | <a id="gui_wf_0224"></a>[Executable Agentic Memory for GUI Agent](https://arxiv.org/abs/2605.12294v1) | GUI states, action groups and routines | Execute subsequent mobile tasks |
| 2026 | <a id="mem_1db918cc57"></a>[Expanding LLM Agent Boundaries with Strategy-Guided Exploration](https://arxiv.org/html/2603.02045v1) | Exploration trajectories and strategy hints | Guide later AndroidWorld actions |
| 2024 | <a id="mem_73c5c9fc62"></a>[Explainable Behavior Cloning: Teaching Large Language Model Agents through Learning by Demonstration](https://arxiv.org/html/2410.22916v1) | Mobile user demonstrations | Guide subsequent mobile tasks |
| 2026 | <a id="mem_2adf16983d"></a>[Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/html/2604.27996v3) | ParaView task experience | Reuse knowledge in visualization workflows |
| 2026 | <a id="gui_add_2609_04869"></a>[From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents](https://arxiv.org/abs/2609.04869v1) | Persistent executable skills from interaction traces | Reuse and revise skills in later desktop tasks |
| 2025 | <a id="mem_55534f231d"></a>[From Operation to Cognition: Automatic Modeling Cognitive Dependencies from User Demonstrations for GUI Task Automation](https://pi.cs.tsinghua.edu.cn/wp-content/uploads/2025/06/3706598.3713356.pdf) | Demonstration graphs and parameter dependencies | Generate new parameters for repeated GUI tasks |
| 2026 | <a id="mem_082ac25de3"></a>[GLOVE: Global Verifier for LLM Memory-Environment Realignment](https://arxiv.org/abs/2601.19249v1) | State-action-outcome experience and corrections | Guide WebShop actions and revise drifted experience |
| 2026 | <a id="mem_a3ce0a1bc9"></a>[GUIDE: Resolving Domain Bias in GUI Agents through Real-Time Web Video Retrieval and Plug-and-Play Annotation](https://arxiv.org/html/2603.26266v3) | Retrieved video-tutorial steps | Guide subsequent computer tasks |
| 2026 | <a id="mem_7bd1196719"></a>[GUITrans2Act: Understanding User Operational Behaviors from Mobile GUI Interactions with Vision-Language Models](https://arxiv.org/html/2606.12817v2) | Mobile demonstrations and operation descriptions | Replay subsequent mobile tasks |
| 2026 | <a id="gui_wf_0172"></a>[Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291v1) | Structured trajectories and symbolic nodes | Guide subsequent GUI tasks |
| 2026 | <a id="mem_44b75fe96f"></a>[IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/html/2602.17049v2) | Intent vectors, skills and planning memory | Guide subsequent computer tasks |
| 2025 | <a id="mem_2039589e4c"></a>[Intention-Based GUI Test Migration for Mobile Apps using Large Language Models](https://seg.nju.edu.cn/uploadPublication/copyright/1251771328477.pdf) | Test-derived intents and exploration history | Migrate tests to a target Android app |
| 2025 | <a id="mem_10448b01db"></a>[JEF-Hinter: Leveraging Offline Knowledge for Improving Web Agents Adaptation](https://arxiv.org/html/2510.04373v2) | Web experience and feedback hints | Guide subsequent web tasks |
| 2025 | <a id="mem_a04115503b"></a>[LEARN-BY-INTERACT: A DATA-CENTRIC FRAMEWORK FOR SELF-ADAPTIVE AGENTS IN REALISTIC ENVIRONMENTS](https://arxiv.org/html/2501.10893v1) | Interaction trajectories and training data | Improve subsequent web and computer actions |
| 2026 | <a id="mem_915a24bd29"></a>[Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents](https://arxiv.org/html/2606.31270v1) | Failed trajectories, repair strategies and code patches | Guide subsequent desktop tasks |
| 2025 | <a id="mem_0a87047f0a"></a>[Learning from Online Videos at Inference Time for Computer-Use Agents](https://arxiv.org/html/2511.04137v1) | Video-tutorial demonstrations | Guide subsequent computer actions |
| 2026 | <a id="mem_26f8a1013f"></a>[Learning Simple Test-Time Environments for LLM Web Agents](https://arxiv.org/html/2608.29305v1) | Experience from test-time subenvironments | Guide subsequent web automation |
| 2025 | <a id="mem_f645c3c0b6"></a>[LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://arxiv.org/html/2503.02950v1) | Agent workflows | Plan and operate browser tasks |
| 2025 | <a id="mem_15b08655ec"></a>[Log2Plan: An Adaptive GUI Automation Framework Integrated with Task Mining Approach](https://arxiv.org/html/2509.22137v1) | Behavior patterns and task dictionary | Plan and execute GUI operations |
| 2025 | <a id="mem_69df37e68d"></a>[Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358v1) | Completed-task plans and browser session state | Retrieve plans for later orchestrated web actions |
| 2025 | <a id="mem_319b45f66d"></a>[Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills](https://arxiv.org/abs/2506.10387v1) | Hierarchical multimodal skills | Guide cross-platform tasks |
| 2026 | <a id="mem_436a3bce45"></a>[MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?](https://arxiv.org/html/2606.01993v1) | Executable skills distilled from guides | Control later GUI tasks |
| 2025 | <a id="mem_adaa85b94f"></a>[Mobile-Agent-RAG: Driving Smart Multi-Agent Coordination with Contextual Knowledge Empowerment for Long-Horizon Mobile Automation](https://arxiv.org/html/2511.12254v1) | Verified plans and application-control guides | Guide later multi-app mobile execution |
| 2023 | <a id="mobilegpt"></a>[MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation](https://arxiv.org/abs/2312.03003v3) | Application subtasks and procedures | Complete later mobile tasks |
| 2026 | <a id="mem_6bd4636764"></a>[Motif: Discovering and Automating Personal Web Workflows](https://arxiv.org/html/2607.10531v1) | Repeated personal workflows and programs | Automate subsequent browsing tasks |
| 2025 | <a id="mem_43d635f955"></a>[NetGent: Agent-Based Automation of Network Application Workflows](https://arxiv.org/html/2509.00625v1) | Workflow state and execution code | Repeat web tasks |
| 2026 | <a id="mem_9bff151ee5"></a>[OmegaUse-SOP: SOP Engineering for Professional Computer Use from Human Demonstrations](https://arxiv.org/html/2609.02149v1) | Expert procedures and domain rules | Guide professional computer tasks |
| 2026 | <a id="gui_wf_0263"></a>[Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval](https://arxiv.org/abs/2606.04391v1) | Trajectory skills and action code | Guide subsequent web actions |
| 2024 | <a id="mem_7f315017a0"></a>[PAFFA: Premeditated Actions For Fast Agents](https://arxiv.org/html/2412.07958v1) | Browser interaction patterns and actions | Execute subsequent web tasks |
| 2026 | <a id="gui_wf_0243"></a>[PANDO: Efficient Multimodal AI Agents via Online Skill Distillation](https://arxiv.org/abs/2605.24785v2) | Distilled online interaction skills | Reuse skills in later multimodal web actions |
| 2026 | <a id="mem_50b7a11276"></a>[PCLLM: An Integrated LLM-Driven System for Automating Desktop Operations via Direct Mouse and Keyboard Control](https://mdpi-res.com/d_attachment/computers/computers-15-00351/article_deploy/computers-15-00351.pdf) | Software architecture and operation sequences | Control desktop mouse and keyboard actions |
| 2026 | <a id="mem_123c68649f"></a>[PlugMem: A Task-Agnostic Plugin Memory Module for LLM Agents](https://arxiv.org/html/2603.03296v1) | Propositional and prescriptive experience | Guide subsequent web tasks |
| 2023 | <a id="mem_ad3777085b"></a>[Prompting Is All You Need: Automated Android Bug Replay with Large Language Models](https://arxiv.org/html/2306.01987v1) | Bug-replay examples | Generate GUI sequences for new Android bugs |
| 2025 | <a id="mem_43c402feb9"></a>[R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/html/2510.11892v1) | External operation tutorials | Plan OSWorld and WebArena tasks |
| 2024 | <a id="mem_f9fb586f04"></a>[RaDA: Retrieval-augmentedWeb Agent Planning with LLMs](https://aclanthology.org/2024.findings-acl.802.pdf) | Action demonstrations and their contexts | Decompose web tasks and generate actions |
| 2025 | <a id="mem_323a806137"></a>[Real-Time Procedural Learning From Experience for AI Agents](https://arxiv.org/abs/2511.22074v2) | State-action-outcome experience | Guide subsequent browsing actions |
| 2025 | <a id="gui_add_reasoningbank"></a>[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140v2) | Reasoning experience and evolving strategies | Retrieve and refine subsequent web plans |
| 2025 | <a id="mem_2976bcd4b4"></a>[Retrieval-augmented GUI Agents with Generative Guidelines](https://arxiv.org/html/2509.24183v1) | Web tutorials and generated guidelines | Guide subsequent GUI operations |
| 2025 | <a id="mem_ed2d101659"></a>[ReuseDroid: A VLM-empowered Android UI Test Migrator Boosted by Active Feedback](https://arxiv.org/html/2504.02357v1) | Source-application testing logic | Guide target-application GUI tests |
| 2026 | <a id="mem_6f5908ef54"></a>[See, Record, Do: Automated Generation of UI Workflows from Tutorial Videos](https://openaccess.thecvf.com/content/WACV2026/papers/Beauchaine_See_Record_Do_Automated_Generation_of_UI_Workflows_from_Tutorial_WACV_2026_paper.pdf) | Video-derived workflows and task tables | Execute desktop workflows |
| 2024 | <a id="mem_6d3437948f"></a>[Skill-Adpative Imitation Learning for UI Test Reuse](https://arxiv.org/html/2409.13311v1) | Transferable skills from source tests | Generate target-app testing actions |
| 2026 | <a id="mem_fc8efb4733"></a>[SkillDroid: Compile Once, Reuse Forever](https://arxiv.org/html/2604.14872v1) | Action templates and element locators | Execute later mobile tasks |
| 2026 | <a id="mem_1884939353"></a>[SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation](https://arxiv.org/html/2608.10775v1) | Skills, visual evidence and verification signals | Guide subsequent GUI operations |
| 2025 | <a id="mem_ce2ba22ac8"></a>[Standing on the Shoulders of Giants: Bug-Aware Automated GUI Testing via Retrieval Augmentation](https://mediatum.ub.tum.de/doc/1832986/1832986.pdf) | Historical bug reports and structured knowledge | Plan bug-directed Android testing |
| 2023 | <a id="gui_wf_0488"></a>[SYNAPSE: TRAJECTORY-AS-EXEMPLAR PROMPTING WITH MEMORY FOR COMPUTER CONTROL](https://arxiv.org/abs/2306.07863v3) | Abstract state-action exemplars | Guide later web actions |
| 2024 | <a id="mem_0c31922846"></a>[TRAD: Enhancing LLM Agents with Step-Wise Thought Retrieval and Aligned Decision](https://arxiv.org/html/2403.06221v1) | Historical thoughts and demonstration steps | Guide subsequent web-action decisions |
| 2025 | <a id="ufo2"></a>[UFO2: The Desktop AgentOS](https://arxiv.org/html/2504.14603v1) | Application-domain knowledge | Execute Windows GUI/application programming interface (API) tasks |
| 2024 | <a id="mem_0408187a4f"></a>[VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://arxiv.org/abs/2406.14596v6) | Program abstractions of demonstrations and subgoals | Guide multimodal web decisions |
| 2025 | <a id="gui_wf_0106"></a>[WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997v2) | Browsing trajectories and task experience | Guide cross-session navigation |
| 2026 | <a id="mem_a695d565aa"></a>[WebGrader: Training LLMs for Web Development with Self-Evolving Programmatic Grader](https://arxiv.org/html/2608.06474v1) | Routable skills from GUI-verification failures | Plan, ground and assess later live-browser checks |
| 2025 | <a id="mem_8df7178cb0"></a>[WebLists: Extracting Structured Information From Complex Interactive Websites Using Executable LLM Agents](https://arxiv.org/html/2504.12682v1) | Web-operation programs and Cascading Style Sheets (CSS) selectors | Extract data from similar pages |
| 2025 | <a id="mem_85eb734c18"></a>[WebSurfer: Enhancing LLM Agents with Web-Wise Feedback for Web Navigation](https://doi.org/10.1109/icassp49660.2025.10889961) | Expert traces, insights and failed experience | Predict later navigation elements and actions |
| 2026 | <a id="mem_e58f01140b"></a>[WebXSkill: Skill Learning for Autonomous Web Agents](https://arxiv.org/html/2604.13318v1) | Parameterized action programs and step guidance | Execute subsequent web tasks |
| 2024 | <a id="wilbur"></a>[WILBUR: Adaptive In-Context Learning for Robust and Accurate Web Agents](https://arxiv.org/html/2404.05902v1) | Prior demonstrations and error paths | Guide web navigation and recovery |

<a id="user"></a>

## User context and personalization · 14

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2026 | <a id="mem_7f2655ac49"></a>[Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions](https://arxiv.org/html/2608.14132v1) | Mobile behavior descriptions and intent history | Predict and execute later mobile tasks |
| 2025 | <a id="mem_204f29eed1"></a>[Beyond Training: Enabling Self-Evolution of Agents with MOBIMEM](https://arxiv.org/html/2512.15784v1) | Profiles, task templates and action records | Guide subsequent mobile tasks |
| 2026 | <a id="mem_6dad5bd2d7"></a>[Exploring Recommender System Evaluation: A Multi-Modal User Agent Framework for A/B Testing](https://arxiv.org/pdf/2601.04554v1) | Cross-session interactions and visual/text preferences | Simulate recommendation-interface behavior |
| 2026 | <a id="mem_ba19f0a17f"></a>[KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/html/2607.12625v2) | Preferences, task memory and skills | Guide personalized GUI tasks |
| 2024 | <a id="gui_wf_0339"></a>[Large Language Models Empowered Personalized Web Agents](https://doi.org/10.1145/3696410.3714842) | Profiles and historical web behavior | Interpret personalized requests and execute actions |
| 2025 | <a id="gui_wf_0395"></a>[MemAgent: A cache-inspired framework for augmenting conversational Web Agents with task-specific information](https://ceur-ws.org/Vol-4028/paper8.pdf) | Task-specific user information | Complete repeated web tasks |
| 2026 | <a id="gui_wf_0125"></a>[PersonalAlign: Hierarchical Implicit Intent Alignment for Personalized GUI Agent with Long-Term User-Centric Records](https://arxiv.org/abs/2601.09636v2) | Preferences, habits and long-term records | Guide personalized mobile actions |
| 2025 | <a id="mem_234fdc406a"></a>[Quick on the Uptake: Eliciting Implicit Intents from Human Demonstrations for Personalized Mobile-Use Agents](https://arxiv.org/html/2508.08645v1) | Operating procedures and user habits | Execute personalized mobile tasks |
| 2026 | <a id="mem_efbc9702cc"></a>[Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227v1) | Cross-day events, profiles and shared device results | Form tasks, select GUI agents and replan |
| 2026 | <a id="mem_373c352731"></a>[SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents](https://arxiv.org/html/2602.01443v1) | Buyer profiles, intents and session experience | Simulate browser shopping interactions |
| 2026 | <a id="mem_584eda464a"></a>[SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents](https://arxiv.org/html/2605.14205v1) | Historical buyer-behavior types | Simulate buyer web actions |
| 2026 | <a id="mem_9e2b16e0a6"></a>[Towards Automated Crowdsourced Testing via Personified-LLM](https://arxiv.org/html/2603.24160v1) | Testing-persona habits and strategies | Generate diverse GUI testing events |
| 2026 | <a id="mem_9479f6783a"></a>[Towards Faithful Simulation of Human Shopping Behavior](https://arxiv.org/html/2608.20707v1) | Session trajectories and shopping preferences | Guide subsequent e-commerce actions |
| 2026 | <a id="mem_398ebf466a"></a>[TRACE: A Scalable and Extensible Framework for Auditing YouTube's Recommendation Algorithm](https://research.dial.uclouvain.be/bitstreams/b64910f1-bd40-413b-bd2e-7f7985ab8bc8/download) | User-role profiles | Simulate web-interface interactions |

<a id="evaluation"></a>

## Benchmarks and evaluation · 22

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2026 | <a id="gui_wf_0277"></a>[Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/abs/2606.15017v2) | Online workflows and skills | Compare web success and computation budgets |
| 2024 | <a id="mem_8a0c25bfd0"></a>[Autonomous Evaluation and Refinement of Digital Agents](https://arxiv.org/abs/2404.06474v3) | Execution traces and evaluator judgments | Evaluate and refine later agent actions |
| 2026 | <a id="mem_5d57f6aaad"></a>[Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World](https://arxiv.org/html/2605.26086v1) | Persistent state and cross-device events | Evaluate later mobile and desktop tasks |
| 2026 | <a id="mem_8a368533a6"></a>[DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments](https://arxiv.org/html/2607.13465v1) | Recent actions and feedback in baseline context | Evaluate cross-device execution |
| 2026 | <a id="mem_0d7de943af"></a>[DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents](https://arxiv.org/html/2605.17439v2) | Failed-trajectory summaries and branch evidence | Guide GUI re-exploration and diagnosis |
| 2025 | <a id="mem_0c787d498c"></a>[FingerTip 20K: A Benchmark for Proactive and Personalized Mobile LLM Agents](https://arxiv.org/html/2507.21071v2) | User profiles and intent history | Evaluate proactive task suggestions and execution |
| 2025 | <a id="mem_2b1f95c536"></a>[FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games](https://arxiv.org/html/2509.01052v2) | Game clues and task trajectories | Evaluate later game-interface actions |
| 2026 | <a id="mem_e50ada3c2a"></a>[GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/html/2604.07429v1) | Multiturn screenshots and actions | Evaluate later game-control actions |
| 2026 | <a id="mem_883eca9986"></a>[KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/html/2604.08455v1) | Profiles and historical mobile logs | Evaluate personalized mobile tasks |
| 2025 | <a id="mem_15a6944ee7"></a>[MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/html/2509.06477v1) | Preset and agent-generated shortcut workflows | Evaluate hybrid mobile and shortcut execution |
| 2026 | <a id="gui_wf_0140"></a>[MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075v3) | Cross-action and cross-session information | Evaluate dynamic mobile tasks |
| 2026 | <a id="gui_wf_0241"></a>[MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833v1) | Long-horizon agent experience | Evaluate later web tasks |
| 2025 | <a id="mem_067bd369ad"></a>[NatureGAIA: Pushing the Frontiers of GUI Agents with a Challenging Benchmark and High-Quality Trajectory Dataset](https://arxiv.org/html/2508.01330v1) | Task plans and evolving context | Evaluate long-horizon execution |
| 2025 | <a id="mem_a1448e1af0"></a>[OPeRA: A Dataset of Observation, Persona, Rationale, and Action for Evaluating LLMs on Human Online Shopping Behavior Simulation](https://arxiv.org/html/2506.05606v1) | Personas and shopping histories | Predict subsequent web actions |
| 2026 | <a id="mem_97b28f23ad"></a>[OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/html/2606.29537v1) | Cross-source task information and user profiles | Evaluate later computer tasks |
| 2026 | <a id="mem_2807793b6c"></a>[Persona2Web: Benchmarking Personalized Web Agents for Contextual Reasoning with User History](https://arxiv.org/abs/2602.17003v3) | User histories and implicit preferences | Evaluate personalized web actions |
| 2026 | <a id="gui_wf_0306"></a>[PersonaTrail: Benchmarking Personalized Web Agents through Browsing Trails](https://arxiv.org/abs/2607.20482v2) | Historical facts and preferences | Evaluate later personalized web actions |
| 2024 | <a id="mem_28a8173dfe"></a>[SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://arxiv.org/abs/2410.15164v2) | Cross-step context and retention | Evaluate interactive Android execution |
| 2025 | <a id="mem_e80d0330b9"></a>[WEB-SHEPHERD: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/html/2505.15277v1) | Web trajectories and step checks | Verify subsequent web steps |
| 2025 | <a id="mem_e9a3fe5356"></a>[WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks](https://arxiv.org/html/2506.01952v1) | Information across web observations | Evaluate complex web tasks |
| 2025 | <a id="mem_6b3ed2ddf7"></a>[WebMall - A Multi-Shop Benchmark for Evaluating Web Agents](https://arxiv.org/html/2508.13024v1) | Short-term agent task memory | Evaluate shopping across websites |
| 2026 | <a id="mem_e2b3c41f62"></a>[When Users Change Their Mind: Evaluating Interruptible Agents in Long-Horizon Web Navigation](https://arxiv.org/html/2604.00892v1) | Executed web state and changed user goals | Evaluate navigation after interruption |

<a id="security"></a>

## Safety and reliability · 15

| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |
|---|---|---|---|
| 2026 | <a id="mem_680ac02d1c"></a>[CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/abs/2609.21686v1) | Sensitive user records retrieved by a web agent | Measure action, process and output leakage |
| 2025 | <a id="mem_9077f1805d"></a>[Context manipulation attacks : Web agents are susceptible to corrupted memory](https://arxiv.org/html/2506.17318v1) | Injected knowledge, histories and plans | Evaluate later web-action safety |
| 2026 | <a id="gui_wf_0338"></a>[CURA: Certified Runtime Alarms for Computer-Use Agents](https://arxiv.org/abs/2608.27808v1) | Trajectory risk state | Monitor subsequent GUI execution |
| 2026 | <a id="mem_f0227aecf6"></a>[Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces](https://arxiv.org/html/2605.09497v1) | Experience of deceptive interfaces | Check subsequent web clicks |
| 2024 | <a id="gui_wf_0012"></a>[GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning](https://arxiv.org/abs/2406.09187v3) | Examples of prior tasks | Check web-agent actions against conditions |
| 2025 | <a id="mem_0ee3ad606e"></a>[HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization](https://arxiv.org/html/2508.04010v1) | Unified safety-policy database | Approve subsequent web actions |
| 2026 | <a id="gui_wf_0249"></a>[MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution](https://arxiv.org/abs/2605.28646v2) | Privacy policies and correction skills | Arbitrate subsequent screen exposure |
| 2026 | <a id="gui_wf_0271"></a>[MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/abs/2606.10742v1) | Poisoned graph memories and multimodal evidence | Influence later web tasks |
| 2026 | <a id="gui_add_2609_02057"></a>[Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision](https://arxiv.org/abs/2609.02057v1) | Observable trajectories and key-step signals | Monitor and intervene in later web actions |
| 2026 | <a id="mem_9d7e2d0d16"></a>[OpenAgentFlow: Enabling System-Wide Safety Boundaries for Heterogeneous AI Agent Fleets](https://arxiv.org/abs/2609.00015v2) | Session provenance, sensitive values and policy state | Check or block subsequent Android action submission |
| 2025 | <a id="mem_af47dbc20f"></a>[Permission Manifests for Web Agents](https://arxiv.org/html/2601.02371v1) | Website interaction permissions | Constrain subsequent web navigation |
| 2026 | <a id="gui_wf_0190"></a>[Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents](https://arxiv.org/abs/2604.02623v2) | Poisoned web-interaction traces | Influence cross-session web tasks |
| 2026 | <a id="mem_c7553f9bac"></a>[ProjGuard: Safety Monitoring for Computer-Use Agents via Low-Dimensional Projections](https://arxiv.org/html/2605.13631v1) | Accumulated trajectories and risk | Monitor and correct later computer actions |
| 2026 | <a id="mem_73d703b4a3"></a>[SynChain: Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains](https://arxiv.org/html/2608.06862v1) | Poisoned skills and memory records | Influence future computer workflows |
| 2025 | <a id="gui_wf_0040"></a>[VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents](https://arxiv.org/abs/2506.02539v3) | Domain-specific experiences and verification judgments | Verify memory before later desktop actions |

## Data maintenance

`catalogue.csv` is the data source for these views. After editing records, run `python scripts/build_catalogue.py`; use `python scripts/build_catalogue.py --check` to verify both language versions.
