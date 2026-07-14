# 101 open-source agent systems

**Course: Agentic AI and Multi-Agent Systems** - Fundacion AI Granada - July 2026

The companion to [101 real-world agent systems](101-real-world-agent-systems.md). That catalog shows what the industry ships; this one lists 101 agents whose **code you can clone, read and adapt**. Every repository was verified live through the GitHub API in July 2026: it exists, it is not archived, and the star count below is a real snapshot.

**The bar for inclusion.** A public repository containing a genuine agent system (a model autonomously deciding and executing multi-step actions with tools), with real adoption (hundreds to tens of thousands of stars) or a peer-reviewed paper behind it. Excluded: frameworks and SDKs (LangGraph, CrewAI...), awesome-lists, thin API wrappers, abandoned MVPs, and anything already listed in the companion catalog.

**Why the Stack column matters here.** These are the frameworks you used in the sessions, in production shape: when an entry says LangGraph or PydanticAI, you can open the repo and see how a real team structured what you built as an exercise.

Architecture labels are the Session 2 coordination patterns: **single agent** (one loop with tools), **sequential** (fixed pipeline), **hierarchical** (orchestrator delegating to subagents), **consensual** (agents voting, debating or verifying each other), **swarm** (many peers in a shared environment).

## Contents

- [Coding and software engineering](#coding-and-software-engineering) (1-9)
- [Research and knowledge work](#research-and-knowledge-work) (10-18)
- [Browser and computer use](#browser-and-computer-use) (19-26)
- [Data analysis, SQL and BI](#data-analysis-sql-and-bi) (27-34)
- [Documents and agentic RAG](#documents-and-agentic-rag) (35-42)
- [DevOps, SRE and security](#devops-sre-and-security) (43-50)
- [Science and biomedicine](#science-and-biomedicine) (51-58)
- [Finance and trading](#finance-and-trading) (59-66)
- [Workflow and business automation](#workflow-and-business-automation) (67-73)
- [Personal assistants and automation](#personal-assistants-and-automation) (74-80)
- [Voice and conversational](#voice-and-conversational) (81-87)
- [Gaming, simulation and embodied](#gaming-simulation-and-embodied) (88-94)
- [Research-paper implementations](#research-paper-implementations) (95-101)

## Coding and software engineering

*Agents you can read to learn how Claude Code and Devin work inside.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 1 | [OpenCode](https://github.com/anomalyco/opencode) · Anomaly (formerly SST), 2025 | Terminal-native coding agent that autonomously explores repos, edits files and runs commands; supports 75+ model providers. | single agent (build/plan agents, each one tool-use loop) | TypeScript, custom loop | 186k |
| 2 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) · Google, 2025 | Open-source terminal agent using Gemini to understand codebases, generate changes, run commands and automate workflows via MCP tools. | single agent (ReAct loop with built-in and MCP tools) | TypeScript, custom loop | 106k |
| 3 | [Cline](https://github.com/cline/cline) · Cline (cline org, ex Claude Dev), 2024 | IDE/CLI coding agent that creates files, runs terminal commands and browses to finish tasks, with optional human-in-the-loop approvals. | single agent (plan/act modes in one tool-use loop) | TypeScript, custom loop | 65k |
| 4 | [Goose](https://github.com/block/goose) · Block (Agentic AI Foundation / Linux Foundation), 2024 | Local AI agent (CLI and desktop) that installs, executes, edits and tests code autonomously with any LLM and MCP extensions. | single agent (one agent loop, tools via MCP extensions) | Rust, custom loop, MCP | 51k |
| 5 | [Crush](https://github.com/charmbracelet/crush) · Charm (charmbracelet), 2025 | Terminal TUI coding agent that reads, writes and executes code with LSP context, MCP tools and multi-model sessions. | single agent (TUI agent loop with LSP and MCP tools) | Go, custom loop | 27k |
| 6 | [Kilo Code](https://github.com/Kilo-Org/kilocode) · Kilo Org (kilo.ai), 2025 | VS Code/JetBrains/CLI agent that plans, builds, debugs and reviews code across files, delegating to specialized subagents over 500+ models. | hierarchical (primary agent delegates subtasks to specialized subagents) | TypeScript, custom loop | 26k |
| 7 | [Plandex](https://github.com/plandex-ai/plandex) · Plandex AI (Dane Schneider), 2024 | Terminal agent that plans and executes large multi-file coding tasks in a cumulative diff sandbox, auto-debugging failed commands. | single agent (plans, edits, executes, debugs in one loop) | Go, custom loop | 16k |
| 8 | [Trae Agent](https://github.com/bytedance/trae-agent) · ByteDance, 2025 | CLI agent for general software engineering: turns natural-language instructions into file edits and bash runs; top SWE-bench Verified scores. | single agent (single ReAct loop with file/bash tools) | Python, custom loop | 12k |
| 9 | [AutoCodeRover](https://github.com/AutoCodeRoverSG/auto-code-rover) · National University of Singapore (AutoCodeRoverSG), 2024 | Resolves GitHub issues autonomously using AST-aware code search then patch generation; 46.2% pass@1 on SWE-bench Verified. | sequential (context retrieval stage then patch generation stage) | Python, custom loop | 3k |

## Research and knowledge work

*Deep research over the web and your own knowledge bases, self-hosted.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 10 | [DeerFlow](https://github.com/bytedance/deer-flow) · ByteDance, 2025 | Long-horizon super-agent that plans, researches the web, codes in sandboxes, and produces reports, slide decks and web pages. | hierarchical (lead agent spawns sandboxed subagents with skills) | Python, LangGraph | 77k |
| 11 | [Khoj](https://github.com/khoj-ai/khoj) · Khoj AI, 2021 | Self-hostable AI second brain: answers from your docs and web, deep research mode, custom agents, scheduled automations. | single agent (iterative /research tool loop over knowledge sources) | Python, Django, custom loop | 36k |
| 12 | [Onyx](https://github.com/onyx-dot-app/onyx) · Onyx (formerly Danswer), 2023 | Enterprise knowledge assistant: agentic RAG over 40+ workplace connectors, multi-step deep research reports, custom agents with actions. | hierarchical (deep research decomposes queries into sub-searches) | Python, FastAPI, custom agents | 31k |
| 13 | [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) · Alibaba Tongyi Lab, 2025 | Open 30B-A3B agentic LLM with inference code for long-horizon web research; tops open deep-research benchmarks. | single agent (ReAct loop; IterResearch heavy test-time mode) | Python, custom loop | 20k |
| 14 | [SurfSense](https://github.com/MODSetter/SurfSense) · MODSetter (open-source project), 2024 | Open-source NotebookLM alternative: research agent over personal knowledge bases and many connectors, scheduled monitoring briefs, podcast generation. | hierarchical (DeepAgents planning with subagents and filesystem) | Python, FastAPI, LangChain DeepAgents | 15k |
| 15 | [Open Deep Research](https://github.com/langchain-ai/open_deep_research) · LangChain, 2024 | Configurable deep-research agent: clarifies scope, delegates sub-topics to parallel researcher subagents, compresses findings into cited reports. | hierarchical (supervisor delegates topics to parallel researchers) | Python, LangGraph | 12k |
| 16 | [Local Deep Researcher](https://github.com/langchain-ai/local-deep-researcher) · LangChain, 2024 | Fully local web research assistant: iteratively generates queries, searches, reflects on knowledge gaps, outputs cited markdown summary. | single agent (reflective loop: search, summarize, find gaps) | Python, LangGraph, Ollama | 9k |
| 17 | [PaperQA2](https://github.com/Future-House/paper-qa) · FutureHouse, 2023 | Agentic RAG over scientific literature: agent iteratively searches papers, gathers evidence, reranks, answers with in-text citations. | single agent (agent iterates search, gather-evidence, answer tools) | Python, custom agent loop | 9k |
| 18 | [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) · Samuel Schmidgall (JHU/AMD), 2025 | Autonomous ML research workflow: specialized agents do literature review, run experiments, and write papers with human feedback checkpoints. | sequential (fixed phases: literature, experiments, report writing) | Python, custom loop | 6k |

## Browser and computer use

*Open implementations of the computer-use pattern: screenshots in, clicks out.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 19 | [Nanobrowser](https://github.com/nanobrowser/nanobrowser) · Nanobrowser community (open-source team), 2025 | Chrome extension that runs multi-step web automation tasks from natural-language commands using your own LLM API keys, fully in-browser. | hierarchical (Planner directs and self-corrects Navigator's web actions) | TypeScript, custom multi-agent loop | 13k |
| 20 | [Agent S (S2/S3)](https://github.com/simular-ai/Agent-S) · Simular AI, 2024 | GUI agent that operates desktop computers from screenshots, learning from experience; Agent S3 surpasses human accuracy on OSWorld benchmark. | single agent (S3 flat agent; Behavior Best-of-N picks best rollout) | Python, custom gui-agents package | 12k |
| 21 | [self-operating-computer](https://github.com/OthersideAI/self-operating-computer) · OthersideAI (HyperWrite), 2023 | Multimodal models view the screen and issue mouse and keyboard actions to operate a computer toward a stated objective. | single agent (One screenshot, decide, act loop) | Python, custom loop, PyAutoGUI | 10k |
| 22 | [Magentic-UI](https://github.com/microsoft/magentic-ui) · Microsoft Research, 2025 | Human-in-the-loop agent automating browser and file tasks: orchestrator model plans while a browser-use model acts inside a sandbox. | hierarchical (Orchestrator delegates to specialized browser-use model) | Python, TypeScript, custom orchestrator | 10k |
| 23 | [UFO (UFO2/UFO3)](https://github.com/microsoft/UFO) · Microsoft, 2024 | Windows desktop AgentOS whose agents operate applications via hybrid GUI and API actions; UFO3 orchestrates tasks across devices. | hierarchical (HostAgent orchestrates per-application AppAgents) | Python, custom framework, MCP | 9k |
| 24 | [Mobile-Agent (v3.5 / GUI-Owl)](https://github.com/X-PLUG/MobileAgent) · Alibaba Tongyi Lab (X-PLUG), 2024 | GUI agent family automating phone, desktop and browser tasks with planning, reflection and memory, powered by GUI-Owl models. | hierarchical (Planner manages operator, reflector and memory agents) | Python, custom multi-agent loop | 9k |
| 25 | [Agent-E](https://github.com/EmergenceAI/Agent-E) · Emergence AI, 2024 | Automates browser tasks (forms, search, media, e-commerce) from natural language, using DOM distillation for compact page representations. | hierarchical (Planner agent drives browser navigation agent) | Python, AutoGen (AG2) | 1k |
| 26 | [WebVoyager](https://github.com/MinorJerry/WebVoyager) · Zhejiang University / Tencent (He et al.), 2024 | Multimodal web agent completing tasks end-to-end on live websites using screenshots with Set-of-Mark annotations and Selenium actions. | single agent (One LMM observe-act loop over screenshots) | Python, Selenium, custom loop | 1k |

## Data analysis, SQL and BI

*Natural language to queries, charts and analyses, with planning loops.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 27 | [PandasAI](https://github.com/sinaptik-ai/pandas-ai) · Sinaptik AI, 2023 | Conversational data analysis over dataframes, CSVs, SQL and datalakes: generates and executes code to answer questions and plot charts. | single agent (generates pandas/SQL code, executes, self-corrects errors) | Python, custom loop, LiteLLM | 24k |
| 28 | [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) · eosphoros AI community (Ant Group roots), 2023 | Agentic AI data assistant: chats with databases, text-to-SQL, generative BI dashboards and multi-agent data workflows, supporting local models. | hierarchical (AWEL workflows orchestrate collaborating data agents) | Python, custom AWEL framework | 19k |
| 29 | [SuperSonic](https://github.com/tencentmusic/supersonic) · Tencent Music Entertainment, 2023 | Chat BI platform: maps questions onto a governed semantic layer, LLM parses and corrects queries, executes SQL, visualizes results. | sequential (mapper, parser, corrector, translator, executor LLM stages) | Java, custom pipeline | 5k |
| 30 | [DeepBI](https://github.com/DeepInsight-AI/DeepBI) · DeepInsight-AI, 2023 | LLM data-scientist BI platform: agents plan analysis, generate and execute SQL and Python on live databases, then build dashboards. | hierarchical (AutoGen-style group chat: planner, executor, checker, chart agents) | Python, AutoGen fork, JavaScript frontend | 2k |
| 31 | [DataLine](https://github.com/RamiAwar/dataline) · Rami Awar (independent), 2024 | Self-hosted, privacy-first chat with CSVs and SQL databases: writes queries, runs them, returns tables, charts and exportable reports. | single agent (LangGraph agent loop over SQL and chart tools) | Python, LangGraph | 2k |
| 32 | [Data-Copilot](https://github.com/zwq2018/Data-Copilot) · Zhejiang University, 2023 | Autonomous financial-data agent: self-designs interface tools, then plans and dispatches workflows to query, analyze, predict and visualize market data. | single agent (LLM self-designs interfaces, then plans workflow dispatch) | Python, custom loop | 2k |
| 33 | [TableGPT Agent](https://github.com/tablegpt/tablegpt-agent) · Zhejiang University TableGPT team, 2024 | Pre-built agent for TableGPT2 that inspects uploaded tables, then writes and executes Python in a sandbox to answer questions. | single agent (LangGraph loop with sandboxed Python execution) | Python, LangGraph | 638 |
| 34 | [LAMBDA](https://github.com/AMA-CMFAI/LAMBDA) · Hong Kong Polytechnic University (CMFAI lab), 2024 | Turns natural-language questions into reproducible analyses: autonomously explores datasets, writes and runs code, visualizes, exports reports and notebooks. | single agent (code-writing loop with persistent workspace and tools) | Python, FastAPI, custom loop | 585 |

## Documents and agentic RAG

*Beyond retrieve-and-stuff: agents that plan multi-step work over document collections.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 35 | [RAGFlow](https://github.com/infiniflow/ragflow) · InfiniFlow, 2024 | RAG engine with agent capabilities: builds document knowledge bases, then runs multi-step agent workflows with tools, code execution, MCP, memory. | hierarchical (canvas agent workflows; lead agents delegate to sub-agents) | Python/Go backend, React frontend | 85k |
| 36 | [PageIndex](https://github.com/VectifyAI/PageIndex) · Vectify AI, 2025 | Vectorless RAG: an LLM agent reasons over hierarchical document tree indexes, navigating sections step by step to locate answers. | single agent (multi-step LLM tree search, no vector database) | Python, LiteLLM multi-provider | 34k |
| 37 | [kotaemon](https://github.com/Cinnamon/kotaemon) · Cinnamon AI, 2024 | Chat-with-your-documents app whose ReAct/ReWOO agents decompose complex multi-hop questions and drive multimodal retrieval over private document collections. | single agent (one ReAct/ReWOO loop over retrieval tools) | Python, Gradio, LlamaIndex | 26k |
| 38 | [DocsGPT](https://github.com/arc53/DocsGPT) · Arc53, 2023 | Builds document-grounded assistants; agents call APIs and tools, run deep research, and return cited answers from ingested files. | single agent (single tool-calling agent with connected actions) | Python, Flask, custom agents | 18k |
| 39 | [KAG](https://github.com/OpenSPG/KAG) · OpenSPG (Ant Group), 2024 | Builds knowledge graphs from domain documents, then a solver plans logical forms and executes multi-step reasoning and retrieval operators. | single agent (kg-solver runs planning, reasoning, retrieval operators iteratively) | Python, OpenSPG graph engine | 9k |
| 40 | [DeepSearcher](https://github.com/zilliztech/deep-searcher) · Zilliz, 2025 | Deep-research agent over private documents: decomposes queries, iteratively searches vector databases, evaluates results, reflects, and writes cited reports. | single agent (iterative sub-query decomposition, retrieval, reflection loop) | Python, FastAPI, Milvus | 8k |
| 41 | [R2R](https://github.com/SciPhi-AI/R2R) · SciPhi AI, 2024 | Retrieval system whose reasoning agent decides when and what to retrieve, chaining hybrid search, knowledge-graph and web tools into reports. | single agent (one retrieval-reasoning loop with pluggable tools) | Python, FastAPI, LiteLLM | 8k |
| 42 | [DocETL](https://github.com/ucbepic/docetl) · UC Berkeley EPIC Lab, 2024 | Declarative document processing where agents execute and rewrite multi-step LLM pipelines, optimizing accuracy and cost over complex document collections. | sequential (LLM operator pipelines with agentic query rewriting/optimization) | Python, YAML pipelines, TypeScript UI | 4k |

## DevOps, SRE and security

*Kubernetes triage, incident investigation, pentesting and vulnerability hunting.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 43 | [Strix](https://github.com/usestrix/strix) · Strix (usestrix), 2025 | Autonomous AI hacker agents that dynamically run target apps, discover, validate and exploit vulnerabilities, producing real proof-of-concepts and fix reports. | hierarchical (Orchestrator deploys specialized red-team agents) | Python, custom agent runtime | 41k |
| 44 | [PentAGI](https://github.com/vxcontrol/pentagi) · VXControl, 2025 | Fully autonomous multi-agent system that plans and performs penetration tests, running 20+ security tools (nmap, metasploit, sqlmap) inside isolated Docker. | hierarchical (Orchestrator delegates to researcher, developer, executor agents) | Go, custom multi-agent orchestration | 20k |
| 45 | [kubectl-ai](https://github.com/GoogleCloudPlatform/kubectl-ai) · Google Cloud, 2025 | Terminal Kubernetes agent turning natural-language intent into multi-step kubectl and bash operations, running tools in a loop to manage clusters. | single agent (One agent loop using kubectl/bash tools) | Go, custom agent loop | 8k |
| 46 | [HolmesGPT](https://github.com/HolmesGPT/holmesgpt) · Robusta.dev (CNCF Sandbox), 2024 | SRE agent investigating production incidents, autonomously pulling logs, metrics and Kubernetes data via toolsets to find root cause and suggest fixes. | single agent (One agent loop calling observability toolsets) | Python, custom agent loop | 3k |
| 47 | [Vulnhuntr](https://github.com/protectai/vulnhuntr) · Protect AI, 2024 | Analyzes a codebase with an LLM that iteratively requests code context to trace user-input-to-sink call chains and find remotely exploitable 0-days. | single agent (LLM iteratively fetches code context, static analysis) | Python, custom LLM loop | 3k |
| 48 | [Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) · Armur AI, 2025 | Autonomous pentest swarm where recon, classification, exploitation and reporting agents coordinate via a shared blackboard, running ProjectDiscovery and nmap tools. | swarm (Decentralized agents coordinate via stigmergic blackboard) | Go, raw Claude API | 2k |
| 49 | [Stakpak Agent](https://github.com/stakpak/agent) · Stakpak, 2024 | Terminal DevOps autopilot generating IaC (Terraform, Kubernetes, Dockerfiles), running builds/deploys and debugging infrastructure 24/7 with guardrails and sandboxed subagents. | single agent (Single agent loop, optional research subagents) | Rust, custom agent loop | 2k |
| 50 | [hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) · TU Wien IPA-Lab, 2023 | Research agents letting LLMs autonomously hack test systems, e.g. iterating SSH commands to achieve Linux privilege escalation; ships reusable benchmarks. | single agent (One LLM loop issuing shell/SSH commands) | Python, custom agent loop | 1k |

## Science and biomedicine

*Research-grade agents for genes, molecules, experiments and clinical questions.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 51 | [TxAgent](https://github.com/mims-harvard/TxAgent) · Harvard (Zitnik Lab / MIMS), 2025 | Therapeutic-reasoning agent analyzing drug interactions, contraindications and patient-specific treatment strategies via 211 biomedical tools and real-time knowledge retrieval. | single agent (one reasoning loop selecting from 211 biomedical tools) | Python, custom loop, fine-tuned Llama | 640 |
| 52 | [GeneGPT](https://github.com/ncbi/GeneGPT) · NCBI / NLM (NIH), 2023 | Tool-augmented LLM answering genomics questions by autonomously calling NCBI Web APIs (E-utils, BLAST) through in-context learning and a custom decoding loop. | single agent (single loop calling NCBI Web APIs) | Python, custom loop (in-context) | 428 |
| 53 | [Curie](https://github.com/Just-Curieous/Curie) · Just-Curieous (Univ. of Michigan), 2025 | Agent framework automating rigorous scientific experimentation end-to-end (hypothesis formulation, experiment implementation, execution, result analysis) with reproducibility controls, including ML engineering tasks. | hierarchical (architect agent supervises technician worker agents) | Python, custom multi-agent framework | 364 |
| 54 | [MDAgents](https://github.com/mitmedialab/MDAgents) · MIT Media Lab, 2024 | Medical decision-making system that adaptively recruits a solo LLM or multi-agent clinician team to answer diagnostic and multimodal questions. | consensual (adaptive solo-or-team; specialists debate to consensus) | Python, custom multi-agent loop | 285 |
| 55 | [MDCrow](https://github.com/ur-whitelab/MDCrow) · White Lab (ur-whitelab), 2025 | Molecular-dynamics agent that sets up, runs and analyzes OpenMM simulations using 40+ expert tools via chain-of-thought reasoning. | single agent (one CoT loop over 40+ MD tools) | Python, LangChain | 244 |
| 56 | [CRISPR-GPT](https://github.com/cong-lab/crispr-gpt-pub) · Cong Lab, Stanford, 2024 | LLM agent automating gene-editing experiment design: selects CRISPR system, designs guide RNAs, drafts protocols and analyzes data across 22 tasks. | hierarchical (LLM planner decomposes tasks; executor runs tools) | Python, custom loop | 173 |
| 57 | [GeneAgent](https://github.com/ncbi-nlp/GeneAgent) · NCBI / NLM (NIH), 2024 | Self-verification agent annotating gene-set biological functions, fact-checking each claim against expert-curated databases via Web APIs to reduce hallucination. | single agent (self-verifies annotations against curated gene databases) | Python, raw OpenAI SDK (GPT-4) | 116 |
| 58 | [BioDiscoveryAgent](https://github.com/snap-stanford/BioDiscoveryAgent) · Stanford SNAP (Leskovec Lab), 2024 | Closed-loop agent designing genetic perturbation (CRISPR) experiments, choosing which genes to test each round using literature search and AI critique. | single agent (closed-loop agent with tools and AI self-critique) | Python, custom loop (Claude) | 113 |

## Finance and trading

*Multi-agent analyst teams and trading research (educational, not investment advice).*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 59 | [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) · virattt (Virat Singh), 2024 | Educational hedge-fund team: 13 investor-persona and 4 specialist analyst agents generate stock signals; risk and portfolio managers make trading decisions. | consensual (parallel analyst signals aggregated by portfolio manager) | Python, LangGraph | 62k |
| 60 | [Dexter](https://github.com/virattt/dexter) · Virat Singh (virattt), 2025 | CLI agent that decomposes financial research questions into tasks, pulls live market data and SEC filings, and self-validates its answers. | single agent (plans tasks, executes tools, self-validates until confident) | TypeScript, Bun, LangChain | 27k |
| 61 | [AI-Trader](https://github.com/HKUDS/AI-Trader) · HKU Data Intelligence Lab (HKUDS), 2025 | Live arena where LLM agents autonomously search, analyze, and execute trades across US stocks, A-shares, and crypto without human intervention. | swarm (independent LLM traders compete autonomously in live-market arena) | Python, FastAPI, React | 21k |
| 62 | [RD-Agent (Quant)](https://github.com/microsoft/RD-Agent) · Microsoft Research, 2024 | Automates quant strategy R&D: proposes factors and models, writes code, backtests on market data, evolves via feedback loops. | hierarchical (research and development agents coordinated in evolving loop) | Python, LiteLLM, custom loop | 14k |
| 63 | [NOFX](https://github.com/NoFxAiOS/nofx) · NoFxAiOS community, 2025 | Trading OS where LLM agents autonomously trade crypto, equities, and forex on real exchanges under hard-coded risk guardrails. | single agent (agent proposes trades; Go runtime enforces risk guardrails) | Go, TypeScript, React | 13k |
| 64 | [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) · AI4Finance Foundation, 2024 | Generates equity research reports: lead agent runs data, valuation, modeling, debate and reporting sub-agents into investment-committee style output. | hierarchical (lead agent orchestrates role sub-agents plus debate) | Python, PydanticAI | 8k |
| 65 | [QuantAgent](https://github.com/Y-Research-SBU/QuantAgent) · Y-Research Group, Stony Brook University, 2025 | Four vision-LLM agents (indicator, pattern, trend, decision) analyze candlestick charts and emit high-frequency long/short trade directives. | sequential (three analysis agents feed final decision agent) | Python, LangGraph | 3k |
| 66 | [FinMem](https://github.com/pipiku915/FinMem-LLM-StockTrading) · Yu et al., Stevens Institute of Technology, 2023 | LLM trading agent with profiling and layered long-term memory that backtests single-stock buy/sell decisions from news and prices. | single agent (one agent loop with layered memory retrieval) | Python, custom loop | 925 |

## Workflow and business automation

*Email, leads, content and ERP flows run by agents you can self-host.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 67 | [Activepieces](https://github.com/activepieces/activepieces) · Activepieces, 2022 | Self-hosted automation platform where AI agents qualify leads, route tickets and execute multi-step actions across 700+ app integrations. | single agent (agents reason and act inside flows, optional human approval) | TypeScript, Fastify, React | 23k |
| 68 | [Rowboat](https://github.com/rowboatlabs/rowboat) · Rowboat Labs (YC S24), 2025 | Desktop AI coworker that indexes email, meetings and Slack into a knowledge graph and runs background agents that draft and act. | single agent (independent background agents triggered by events or schedules) | TypeScript, Electron desktop app | 16k |
| 69 | [Inbox Zero](https://github.com/elie222/inbox-zero) · Elie Steinbock (Inbox Zero), 2023 | AI email assistant that autonomously triages inboxes: applies plain-English rules, drafts replies, archives, unsubscribes and blocks cold email. | single agent (LLM loop applies user rules via email tools) | TypeScript, Next.js | 12k |
| 70 | [Zero](https://github.com/Mail-0/Zero) · Mail-0, 2025 | Self-hostable Gmail alternative with a built-in AI agent that summarizes, labels, composes, sends and organizes email through tool calls. | single agent (tool orchestrator routes email tools and streaming sub-agents) | TypeScript, React Router, Vercel AI SDK | 11k |
| 71 | [Integuru](https://github.com/Integuru-AI/Integuru) · Integuru AI, 2024 | Agent reverse-engineers a platform's internal API from recorded browser traffic and generates permissionless Python integration code for business actions. | single agent (builds request dependency graph, then emits runnable code) | Python, OpenAI API | 5k |
| 72 | [Social Media Agent](https://github.com/langchain-ai/social-media-agent) · LangChain, 2024 | Sources and curates content from URLs, generates Twitter and LinkedIn posts, and schedules them with human-in-the-loop approval. | sequential (LangGraph ingest-generate-review-schedule flow with human interrupts) | TypeScript, LangGraph | 3k |
| 73 | [OpenAdapt](https://github.com/OpenAdaptAI/OpenAdapt) · OpenAdapt.AI, 2023 | Generative RPA: records GUI workflow demonstrations, then replays or generalizes them with multimodal models executing desktop and web actions. | single agent (demo-conditioned VLM loop replaying GUI actions) | Python, custom loop | 2k |

## Personal assistants and automation

*General-purpose agents that run on your machine and act on your behalf.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 74 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) · Open Interpreter, 2023 | Terminal coding agent, a Codex fork optimized for open models, that writes and executes code and shell commands locally, sandboxed. | single agent (one loop generating and executing code locally) | Rust, Codex fork | 65k |
| 75 | [OpenManus](https://github.com/FoundationAgents/OpenManus) · FoundationAgents (MetaGPT community), 2025 | Open Manus replica: general-purpose agent that plans tasks and executes them via browser automation (Playwright), code execution and MCP tools. | single agent (ReAct tool loop; optional multi-agent flow variant) | Python, custom loop, Playwright | 57k |
| 76 | [AgenticSeek](https://github.com/Fosowl/agenticSeek) · Fosowl (Martin Legrand), 2025 | Fully local Manus alternative: voice-enabled assistant that autonomously browses the web, writes and runs code, and plans multi-step tasks. | hierarchical (router and planner delegate to browser, coder, file agents) | Python, custom loop, FastAPI | 27k |
| 77 | [Kortix (formerly Suna)](https://github.com/kortix-ai/suna) · Kortix AI, 2025 | Company AI command center: parallel sandboxed agent sessions complete real tasks via 3,000+ connectors and reviewed change requests. Elastic License 2.0. | single agent (independent single-agent sessions in parallel sandboxes) | TypeScript, OpenCode agent runtime | 20k |
| 78 | [Agent Zero](https://github.com/agent0ai/agent-zero) · agent0ai (Jan Tomasek / frdel), 2024 | General-purpose personal agent in a Dockerized Linux desktop: browses, codes, runs terminal commands, and learns persistent skills and memories. | hierarchical (superior agents spawn subordinate agents for subtasks) | Python, custom loop, Dockerized | 18k |
| 79 | [Leon](https://github.com/leon-ai/leon) · Leon AI (Louis Grenard), 2019 | Self-hosted personal assistant whose LLM agent mode plans step by step and executes native and agent skills as tools, privacy-first. | single agent (one planner loop executing skills as tools) | TypeScript, Python, custom loop | 17k |
| 80 | [Eigent](https://github.com/eigent-ai/eigent) · Eigent AI (CAMEL-AI team), 2025 | Local desktop AI workforce: parallel developer, browser, document and multimodal agents complete multi-step productivity tasks with human-in-the-loop. | hierarchical (coordinator delegates subtasks to parallel specialized workers) | Python, CAMEL framework, Electron | 15k |

## Voice and conversational

*Talking agents: phone lines, embedded devices, avatars and companions.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 81 | [AIRI](https://github.com/moeru-ai/airi) · Moeru AI, 2024 | Self-hosted Neuro-sama-style companion: real-time voice chat, animates Live2D/VRM avatar, autonomously plays Minecraft and Factorio, chats on Discord/Telegram. | hierarchical (core LLM brain coordinates game-playing sub-agents) | TypeScript, Vue, Electron, WebGPU | 42k |
| 82 | [XiaoZhi ESP32](https://github.com/78/xiaozhi-esp32) · 78 (Xiage) and community, 2024 | ESP32 voice chatbot device: converses via Qwen/DeepSeek and controls smart home, PC desktop, search and email through MCP tools. | single agent (device chat loop invoking MCP tool servers) | C++, ESP-IDF, MCP protocol | 28k |
| 83 | [Fay](https://github.com/xszyou/Fay) · xszyou (Fay community), 2022 | Voice-interactive digital-human assistant linking LLMs to business systems; agent autonomously invokes MCP tools, holds proactive scheduled conversations, drives avatars. | single agent (LLM agent selects MCP tools; proactive dialogue scheduler) | Python, WebSockets, MCP, OpenAI-compatible LLMs | 13k |
| 84 | [Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) · Open-LLM-VTuber (community), 2023 | Offline-capable voice companion with Live2D avatar; sees camera/screen and autonomously calls MCP tools like web search and browser use. | single agent (Companion agent with MCP tool loop and vision) | Python backend, Electron/web Live2D frontend | 13k |
| 85 | [OpenAI Realtime Agents](https://github.com/openai/openai-realtime-agents) · OpenAI, 2025 | Voice customer-service agents over the Realtime API: authentication, returns and escalation flows with supervisor delegation, tool calls and guardrails. | hierarchical (chat-supervisor delegation plus sequential agent handoffs) | TypeScript, Next.js, OpenAI Agents SDK | 7k |
| 86 | [Call Center AI](https://github.com/microsoft/call-center-ai) · Microsoft (Clemence Lesne), 2024 | Runs inbound/outbound phone calls for insurance and support: gathers claim data, updates records, sends SMS, RAG lookups, human handoff. | single agent (one call loop, LLM streams multi-tool actions) | Python, raw OpenAI SDK, Azure | 7k |
| 87 | [GLaDOS](https://github.com/dnhkng/GLaDOS) · David Ng (dnhkng), 2023 | Local low-latency Portal-style voice assistant: streaming ASR/TTS, vision, persistent memory, and system actions through native and MCP tools. | hierarchical (async subagents (memory, emotion, observer) feed main loop) | Python, custom loop, ONNX, Ollama | 6k |

## Gaming, simulation and embodied

*Agents in game worlds, social simulations and robot policies.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 88 | [AI Town](https://github.com/a16z-infra/ai-town) · a16z-infra, 2023 | Deployable virtual town where LLM characters live, plan, converse and form memories; humans can join and interact in real time. | swarm (many peer NPC agents in shared world) | TypeScript, Convex engine | 10k |
| 89 | [Pokemon Red Experiments](https://github.com/PWhiddy/PokemonRedExperiments) · Peter Whidden, 2023 | Trains PPO agents that play Pokemon Red end-to-end from pixels in an emulator: exploring, catching Pokemon, beating gym leaders. | single agent (learned PPO policy maps pixels to buttons) | Python, Stable-Baselines3, PyBoy | 8k |
| 90 | [OpenVLA](https://github.com/openvla/openvla) · Stanford, Berkeley, TRI et al., 2024 | 7B vision-language-action model controls robot arms: maps camera images plus language instructions directly to manipulation actions; fine-tunable to new robots. | single agent (end-to-end learned policy, no explicit planner) | Python, PyTorch, Prismatic VLM | 7k |
| 91 | [Mindcraft](https://github.com/mindcraft-bots/mindcraft) · mindcraft-bots (Kolby Nottingham et al.), 2023 | LLM-driven bots play Minecraft: gather, craft, build and fight via Mineflayer commands, chatting and collaborating with players and other bots. | single agent (per-bot LLM loop with tools; multi-bot optional) | JavaScript, Mineflayer, custom loop | 5k |
| 92 | [OASIS](https://github.com/camel-ai/oasis) · CAMEL-AI.org, 2024 | Simulates social media (Twitter, Reddit) with up to one million LLM agents posting, following and reposting to study information spread. | swarm (up to a million peer agents interacting) | Python, CAMEL framework | 5k |
| 93 | [Eureka](https://github.com/eureka-research/Eureka) · NVIDIA Research + UPenn, 2023 | GPT-4 writes and evolves reward functions, evaluated by RL in Isaac Gym, teaching simulated robots skills like pen spinning. | single agent (LLM evolutionary loop over reward code) | Python, Isaac Gym, custom loop | 3k |
| 94 | [Cradle](https://github.com/BAAI-Agents/Cradle) · BAAI-Agents (Beijing Academy of AI), 2024 | Plays commercial games (RDR2, Stardew Valley) and desktop apps from raw screenshots, emitting keyboard-mouse actions with self-reflection and skill curation. | single agent (iterative loop: reflect, plan, curate skills, act) | Python, custom loop | 3k |

## Research-paper implementations

*Runnable code of the papers behind the patterns taught in this course.*

| # | Project | What it does | Architecture | Stack | ~Stars |
|---|---------|--------------|--------------|-------|--------|
| 95 | [AppAgent](https://github.com/TencentQQGYLab/AppAgent) · Tencent QQGYLab, 2023 | Multimodal agent learns Android apps through autonomous exploration or demonstrations, then executes tasks by tapping and swiping like humans (CHI 2025). | single agent (multimodal LLM loop over Android UI actions) | Python, raw GPT-4V API, ADB | 7k |
| 96 | [Tree of Thoughts](https://github.com/princeton-nlp/tree-of-thought-llm) · Princeton NLP (Shunyu Yao et al.), 2023 | LLM generates, evaluates and backtracks over branching thought trees with BFS/DFS to solve Game of 24, writing, crosswords. | single agent (one LLM, tree search over thoughts) | Python, custom search loop | 6k |
| 97 | [ReAct (original repo)](https://github.com/ysymyth/ReAct) · Shunyu Yao, Princeton NLP, 2022 | Official ReAct paper code: LLM interleaves reasoning traces with actions on HotpotQA, FEVER, AlfWorld and WebShop environments. | single agent (one thought-action-observation loop) | Python notebooks, raw OpenAI API | 4k |
| 98 | [Reflexion](https://github.com/noahshinn/reflexion) · Noah Shinn, Northeastern University, 2023 | Agent retries failed tasks using verbal self-reflection memory, improving on programming, AlfWorld decision-making and HotpotQA reasoning (NeurIPS 2023). | single agent (actor plus evaluator and self-reflection memory) | Python, raw OpenAI API | 3k |
| 99 | [OS-Copilot (FRIDAY)](https://github.com/OS-Copilot/OS-Copilot) · Shanghai AI Laboratory et al., 2024 | FRIDAY agent automates OS tasks across terminal, files, web, multimedia and third-party apps, self-generating new tools as it learns. | single agent (plan-configure-act loop generating own tools) | Python, custom loop | 2k |
| 100 | [Agent-as-a-Judge](https://github.com/metauto-ai/agent-as-a-judge) · metauto-ai (Meta AI / KAUST), 2024 | Judge agent inspects other agents' code workspaces with locate/read/search tools to evaluate requirements on the DevAI benchmark (ICML 2025). | single agent (judge agent with code-inspection tools) | Python, LiteLLM | 798 |
| 101 | [AFlow](https://github.com/FoundationAgents/AFlow) · FoundationAgents (DeepWisdom / MetaGPT team), 2024 | Monte Carlo tree search automatically generates, executes and refines code-represented agentic workflows across math, QA and coding benchmarks (ICLR 2025 oral). | hierarchical (MCTS optimizer evolves and executes LLM workflows) | Python, MetaGPT components | 551 |

## Before you adopt one of these

Three checks, straight from Session 3, before an open-source agent touches anything real:

1. **Activity and community.** Stars measure popularity, not health. Check the commit log, open issues and release cadence; an agent that cannot keep up with model API changes rots in months.
2. **Evaluation.** Does the repo ship evals or benchmarks? An agent without regression tests for its behavior is a demo, whatever its star count.
3. **Blast radius.** Most of these execute code, browse or spend money. Read what the tools can touch, run it sandboxed first (containers, restricted keys, spending caps), and add your own guardrails before production.

*Companion catalog: [101 real-world agent systems](101-real-world-agent-systems.md). Compiled with the same multi-agent research pipeline (domain researchers + independent fact-checkers + GitHub API validation of every repository). Star counts: July 2026. Corrections welcome: chema@montevive.ai*
