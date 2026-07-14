# 101 real-world agent systems

**Course: Agentic AI and Multi-Agent Systems** - Fundacion AI Granada - July 2026

A field guide of 101 real agent systems, compiled and fact-checked for this course (July 2026). Use it to answer the question every project starts with: *has someone already built an agent for a problem like mine?* When the answer is yes and you want to read the code, jump to the companion catalog: [101 open-source agent systems](101-open-source-agent-systems.md).

**What counts as an agent here.** Software where a model autonomously decides and executes multi-step actions against tools or an environment (the Session 1 anatomy: reasoning, perception, memory, tools, environment). Plain chatbots and autocomplete tools are out; so are agent *frameworks* (LangGraph, CrewAI...), which are covered in the sessions themselves.

**How to read the Architecture column** (the Session 2 coordination patterns):

- **single agent**: one reasoning loop with tools (Session 1).
- **sequential**: a fixed pipeline of stages (workflow, Session 2 block 1).
- **hierarchical**: an orchestrator delegating to specialist subagents (the workshop supervisor).
- **consensual**: several agents vote, debate or verify each other.
- **swarm**: many peer agents interacting in a shared environment.

Entries were verified against live sources in July 2026. Links marked with vendors' sites may ask you to accept cookies or block automated access, but all resolved in a browser at publication time.

## Contents

- [Coding and software engineering](#coding-and-software-engineering) (1-9)
- [Deep research and knowledge work](#deep-research-and-knowledge-work) (10-18)
- [Computer and browser use](#computer-and-browser-use) (19-26)
- [Science and drug discovery](#science-and-drug-discovery) (27-34)
- [Customer support and CX](#customer-support-and-cx) (35-41)
- [Enterprise and business operations](#enterprise-and-business-operations) (42-49)
- [Finance and legal](#finance-and-legal) (50-57)
- [Healthcare](#healthcare) (58-64)
- [Security and IT operations](#security-and-it-operations) (65-72)
- [Robotics and embodied agents](#robotics-and-embodied-agents) (73-80)
- [Education and personal assistants](#education-and-personal-assistants) (81-87)
- [Creative and media](#creative-and-media) (88-94)
- [Landmark research systems](#landmark-research-systems) (95-101)

## Coding and software engineering

*From issue to tested pull request without a human driving the editor.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 1 | [Devin](https://devin.ai/) · Cognition, 2024 | Plans, writes, tests, and ships production code autonomously using its own shell, editor, and browser; handles migrations and bug-fix tickets. | single agent (one agent loop with shell, editor, browser tools) | product |
| 2 | [Claude Code](https://claude.com/product/claude-code) · Anthropic, 2025 | Terminal agent that explores codebases, edits files, runs tests and shell commands, and handles git workflows from natural-language instructions. | single agent (single loop with tools; can spawn subagents) | product |
| 3 | [OpenAI Codex](https://openai.com/codex/) · OpenAI, 2025 | Runs parallel software tasks in cloud sandboxes: writes features, fixes bugs, answers codebase questions, and proposes pull requests. | single agent (one agent per task in isolated cloud sandbox) | product |
| 4 | [Jules](https://jules.google/) · Google, 2025 | Clones your repo into a cloud VM, plans changes, then asynchronously writes tests, builds features, fixes bugs, and presents diffs. | single agent (plan-then-execute single agent in cloud VM) | product |
| 5 | [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) · GitHub (Microsoft), 2025 | Takes an assigned GitHub issue, plans a task checklist, writes code in an Actions sandbox, runs tests, and iterates on a PR. | single agent (one agent iterating inside GitHub Actions sandbox) | product |
| 6 | [Aider](https://aider.chat/) · Aider-AI (Paul Gauthier), 2023 | Terminal pair programmer that maps repos with tree-sitter, makes multi-file edits, runs lint/test repair loops, and auto-commits to git. | single agent (single terminal loop with edit, test, commit tools) | open source |
| 7 | [OpenHands](https://github.com/OpenHands/OpenHands) · All Hands AI, 2024 | Open-source development agent that plans tasks, writes and executes code, browses the web, and runs commands in a Docker sandbox. | single agent (CodeAct-style single loop with sandboxed execution) | open source |
| 8 | [SWE-agent](https://arxiv.org/abs/2405.15793) · Princeton University, 2024 | Takes a GitHub issue and autonomously produces a repository patch via a purpose-built agent-computer interface; NeurIPS 2024 paper. | single agent (one LM loop over agent-computer interface commands) | research |
| 9 | [Replit Agent](https://replit.com/products/agent) · Replit, 2024 | Builds full-stack apps from natural-language prompts, then tests them in a real browser and fixes issues in autonomous loops. | single agent (one loop with build, browser-test, fix tools) | product |

## Deep research and knowledge work

*Multi-step web and literature research with citations.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 10 | [OpenAI Deep Research](https://openai.com/index/introducing-deep-research/) · OpenAI, 2025 | Autonomously plans and executes multi-step web browsing, reading hundreds of sources and pivoting on findings to produce cited research reports. | single agent (one RL-trained o3 model browsing iteratively) | product |
| 11 | [Gemini Deep Research](https://gemini.google/overview/deep-research/) · Google, 2024 | Runs an autonomous loop of planning, searching, reading and reasoning over hundreds of websites, then writes multi-page cited reports. | single agent (single iterative plan-search-read-reason loop) | product |
| 12 | [Claude Research (multi-agent research system)](https://www.anthropic.com/engineering/multi-agent-research-system) · Anthropic, 2025 | Lead agent plans research, spawns parallel subagents that search the web and workspace tools, then compiles cited answers. | hierarchical (lead orchestrator spawns 3-5 parallel search subagents) | product |
| 13 | [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) · Perplexity AI, 2025 | Performs dozens of autonomous searches, reads hundreds of sources, iteratively refines its research plan, and delivers comprehensive cited reports. | single agent (iterative search-read-reason loop, no subagents) | product |
| 14 | [Elicit Systematic Review](https://elicit.com/) · Elicit, 2025 | Automates systematic literature reviews: suggests screening criteria, screens papers, extracts data fields with supporting quotes into structured tables. | sequential (fixed stages: question, gather, screen, extract, export) | product |
| 15 | [STORM](https://github.com/stanford-oval/storm) · Stanford OVAL, 2024 | Researches a topic via simulated multi-perspective writer-expert interviews, builds an outline, then writes a cited Wikipedia-style article. | sequential (fixed research-outline-write stages with role-played dialogues) | open source |
| 16 | [GPT Researcher](https://github.com/assafelovic/gpt-researcher) · Assaf Elovic / Tavily (open source), 2023 | Planner agent generates research questions; crawler execution agents scrape and summarize web sources; planner aggregates into multi-page reports. | hierarchical (planner delegates questions to parallel execution agents) | open source |
| 17 | [AI Co-Scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) · Google DeepMind / Google Research, 2025 | Generates scientific hypotheses, then specialized agents debate, rank them in tournaments, and evolve them into novel research proposals. | consensual (generation, reflection, ranking agents debate in tournaments) | research |
| 18 | [The AI Scientist](https://sakana.ai/ai-scientist/) · Sakana AI, 2024 | Autonomously generates research ideas, writes and runs ML experiments, drafts full papers, and performs automated peer review. | sequential (fixed ideation-experiment-writeup-review stage chain) | research |

## Computer and browser use

*Agents that operate screens, browsers and GUIs built for humans.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 19 | [Claude computer use](https://www.anthropic.com/news/3-5-models-and-computer-use) · Anthropic, 2024 | Views screenshots and moves the cursor, clicks, and types to operate desktop apps and browsers for multi-step tasks. | single agent (One loop: screenshot in, mouse/keyboard action out) | product |
| 20 | [ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/) · OpenAI, 2025 | Uses its own virtual computer with browser and terminal to fill forms, book reservations, shop, and complete web tasks end-to-end. | single agent (One unified agent loop with browser, terminal tools) | product |
| 21 | [Project Mariner](https://labs.google.com/mariner/) · Google DeepMind, 2024 | Gemini-powered prototype browsing websites in cloud VMs: clicking, typing, filling forms, running up to 10 tasks simultaneously. | single agent (Single observe-plan-act loop per task instance) | research |
| 22 | [Browser Use](https://github.com/browser-use/browser-use) · Browser Use (open source), 2024 | Python library agent that opens pages, clicks buttons, types, and fills forms to automate web tasks with any LLM. | single agent (One LLM loop driving browser via DOM plus vision) | open source |
| 23 | [Skyvern](https://github.com/skyvern-ai/skyvern) · Skyvern AI, 2024 | Automates browser workflows (form filling, logins, invoice downloads) using vision LLMs and Playwright, resilient to site layout changes. | hierarchical (Agent swarm: planner delegates comprehension and action agents) | open source |
| 24 | [Amazon Nova Act](https://github.com/aws/nova-act) · Amazon (AWS AGI), 2025 | SDK for reliable browser agents: Python chains natural-language act() steps for form filling, navigation, and structured data extraction. | sequential (Developer-scripted chain of atomic act() model calls) | product |
| 25 | [UI-TARS](https://github.com/bytedance/UI-TARS) · ByteDance, 2025 | Native vision-language model perceiving screenshots and emitting keyboard/mouse actions to automate desktop, web, and mobile GUIs. | single agent (End-to-end VLM policy: screenshot to action) | open source |
| 26 | [Comet](https://www.perplexity.ai/comet) · Perplexity, 2025 | Chromium AI browser whose assistant navigates sites, organizes tabs, compares products, books travel, and fills forms across sessions. | single agent (Single embedded assistant loop across browser tabs) | product |

## Science and drug discovery

*Agents that design experiments, run labs and mine scientific literature.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 27 | [Coscientist](https://www.nature.com/articles/s41586-023-06792-0) · Carnegie Mellon University, 2023 | Autonomously designs, plans, and executes chemistry experiments, driving robotic liquid handlers to optimize reactions like palladium-catalyzed Suzuki and Sonogashira cross-couplings. | hierarchical (GPT-4 Planner directs web, docs, code, robotics modules) | research |
| 28 | [ChemCrow](https://arxiv.org/abs/2304.05376) · EPFL, 2023 | LLM chemistry agent that plans and executes organic syntheses via 18 expert tools, driving IBM's RoboRXN robot to make DEET and organocatalysts. | single agent (One GPT-4 ReAct loop over 18 chemistry tools) | research |
| 29 | [Robin](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system) · FutureHouse, 2025 | Multi-agent system autonomously generating hypotheses, designing experiments, and analyzing data for drug repurposing; proposed ripasudil for dry macular degeneration. | hierarchical (Workflow orchestrates literature agents (Crow, Falcon) and data agent Finch) | research |
| 30 | [The Virtual Lab](https://github.com/zou-group/virtual-lab) · Stanford University, 2024 | Team of LLM agents led by a PI agent designed 92 SARS-CoV-2 nanobodies, experimentally validated, using ESM, AlphaFold-Multimer, and Rosetta. | hierarchical (PI agent leads specialist agents plus critic in meetings) | open source |
| 31 | [Biomni](https://github.com/snap-stanford/Biomni) · Stanford University, 2025 | General-purpose biomedical agent that autonomously plans and runs research tasks using 150+ tools and databases across genomics, cloning, and drug repurposing. | single agent (One agent retrieves and runs 150+ biomedical tools) | open source |
| 32 | [A-Lab](https://www.nature.com/articles/s41586-023-06734-w) · Lawrence Berkeley National Laboratory, 2023 | Autonomous robotic lab that synthesized 41 novel inorganic materials in 17 days, using ML and active learning to plan recipes. | sequential (Fixed loop: propose, synthesize, characterize, active-learning decide) | research |
| 33 | [SciAgents](https://arxiv.org/abs/2409.05556) · MIT, 2024 | Multi-agent system reasoning over a 33,000-node knowledge graph to autonomously generate and critique research hypotheses for bio-inspired materials. | hierarchical (Ontologist, scientist, and critic agents traverse ontological knowledge graph) | research |
| 34 | [STELLA](https://arxiv.org/abs/2507.02004) · Princeton University and Stanford University, 2025 | Self-evolving biomedical LLM agent that autonomously creates its own bioinformatics tools and reasoning templates, reaching state-of-the-art accuracy on biomedical benchmarks. | hierarchical (Manager directs Developer, Critic, and Tool-Creation agents) | research |

## Customer support and CX

*Autonomous resolution of customer conversations, tickets and calls.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 35 | [Fin AI Agent](https://fin.ai/) · Intercom, 2023 | Resolves support conversations end to end across channels, executing multi-step Tasks like cancellations and refunds through API-connected workflows. | single agent (one agent loop over RAG, custom models, tool actions) | product |
| 36 | [Sierra Agent Platform](https://sierra.ai/) · Sierra, 2024 | Enterprise customer agents converse over chat and voice, executing returns, subscription updates and cancellations in connected backend systems. | hierarchical (planner-executor design; supervisor agents route and validate) | product |
| 37 | [Decagon AI Agent Engine](https://decagon.ai/) · Decagon, 2024 | Core AI agent handles chat, email and voice tickets, executing refunds and subscription changes following Agent Operating Procedures. | single agent (unified core agent; separate routing and QA audit modules) | product |
| 38 | [Klarna AI Assistant](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · Klarna (with OpenAI), 2024 | Handled two-thirds of Klarna's service chats in month one, managing refunds, returns and payment issues in 35+ languages. | single agent (one OpenAI-powered assistant executing errands with tools) | product |
| 39 | [Zendesk AI Agents](https://www.zendesk.com/ai-agents/) · Zendesk (tech from Ultimate acquisition), 2024 | Autonomously resolves up to 80% of interactions across channels, executing multi-step workflows and coordinating actions across connected systems. | single agent (single generative agent with workflow and API actions) | product |
| 40 | [Ada AI Agent](https://www.ada.cx/) · Ada Support, 2023 | Authenticates customers, plans steps and executes workflows in connected systems, resolving inquiries across chat, email, voice and SMS. | single agent (Reasoning Engine plans, safety-checks, then executes actions) | product |
| 41 | [Gorgias AI Agent](https://www.gorgias.com/ai-agent) · Gorgias, 2024 | Resolves ecommerce tickets autonomously: order tracking, returns, refunds, address and subscription edits via Shopify and 100+ integrations. | single agent (one agent, cascading prompts, confirmation-gated tool actions) | product |

## Enterprise and business operations

*Workflow agents inside CRMs, ERPs, ITSM and the tools businesses already run.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 42 | [Salesforce Agentforce](https://www.salesforce.com/agentforce/) · Salesforce, 2024 | Autonomously resolves customer service cases, qualifies sales leads, and executes CRM actions on company data, escalating to humans when needed | single agent (Atlas Reasoning Engine loop plans and executes actions) | product |
| 43 | [ServiceNow AI Agents](https://www.servicenow.com/products/ai-agents.html) · ServiceNow, 2025 | Pre-built agents resolve IT, HR, and customer-service tickets end-to-end on the ServiceNow platform, coordinated across departments by AI Agent Orchestrator | hierarchical (AI Agent Orchestrator coordinates specialized agents across departments) | product |
| 44 | [Microsoft 365 Copilot Researcher and Analyst](https://www.microsoft.com/en-us/microsoft-365/blog/2025/03/25/introducing-researcher-and-analyst-in-microsoft-365-copilot/) · Microsoft, 2025 | Reasoning agents run multi-step research and data analysis over emails, files, meetings, and web, iterating until delivering report-quality answers | single agent (each is one deep-reasoning loop over enterprise data) | product |
| 45 | [UiPath Agentic Automation (Maestro)](https://www.uipath.com/platform/agentic-automation) · UiPath, 2025 | Maestro control plane orchestrates AI agents, RPA robots, and humans through long-running BPMN business processes like claims handling and onboarding | hierarchical (Maestro orchestrator delegates to agents, robots, and humans) | product |
| 46 | [Moveworks](https://www.moveworks.com/) · Moveworks (ServiceNow), 2019 | Employee-support agent in Slack/Teams autonomously resolves IT and HR requests: password resets, software provisioning, PTO, across 100+ enterprise systems | single agent (Reasoning Engine plans steps and executes plugin actions) | product |
| 47 | [IBM watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate) · IBM, 2025 | Builds and runs enterprise agents that automate HR, procurement, and sales tasks (time-off, invoicing, vendor management) across 700+ applications | hierarchical (supervisor agent routes requests to specialized agents) | product |
| 48 | [SAP Joule Agents](https://www.sap.com/products/artificial-intelligence/ai-agents.html) · SAP, 2025 | Specialized agents inside SAP ERP autonomously handle finance, supply-chain, and procurement work: dispute resolution, cash collection, bid analysis, reconciliations | hierarchical (Joule orchestrates agent teams; agents trigger other agents) | product |
| 49 | [Glean Agents](https://www.glean.com/product/ai-agents) · Glean, 2025 | Employees build agents in natural language; agents plan multi-step workflows and execute actions across company systems using enterprise search context | single agent (reasoning engine plans multi-step actions from action library) | product |

## Finance and legal

*Contract work, diligence, financial analysis and trading research.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 50 | [Harvey Workflow Agents](https://www.harvey.ai/platform/workflow-agents) · Harvey AI, 2025 | Plans and executes multi-step legal work: drafting, diligence, and document analysis across transactional and litigation matters with human checkpoints. | sequential (multi-step workflows chain agents with conditionals and checkpoints) | product |
| 51 | [Hebbia Matrix](https://www.hebbia.com/product) · Hebbia, 2024 | Answers complex finance and legal questions over huge document sets by decomposing them into subtasks run by specialist agents. | hierarchical (orchestrator dispatches text objectives to specialized subagents) | product |
| 52 | [Rogo Felix](https://rogo.ai/felix) · Rogo, 2026 | Autonomous banking-analyst agent; bankers delegate work by email and it produces deal screening, comparables, models, memos, and decks. | single agent (one personalized agent executes multi-step finance workflows) | product |
| 53 | [AlphaSense Deep Research](https://www.alpha-sense.com/) · AlphaSense, 2025 | Runs 10-30 minute autonomous research over 500M+ financial documents, producing company primers, M&A screens, and investment briefings. | single agent (one long-running research loop over premium content corpus) | product |
| 54 | [Luminance Autonomous Negotiation](https://www.luminance.com/autonomous-negotiation/) · Luminance, 2023 | Negotiates contracts end-to-end: reviews agreements, redlines to legal standards, sends revisions, tracks and reacts to counterparty AI changes. | single agent (one agent negotiates end-to-end, even against counterparty AI) | product |
| 55 | [Spellbook Associate](https://spellbook.com/associate) · Spellbook, 2024 | Plans and executes transactional legal projects: drafts financing documents from term sheets, reviews document sets, revises many documents at once. | single agent (plans tasks, executes, checks own work, adapts) | product |
| 56 | [TradingAgents](https://arxiv.org/abs/2412.20138) · Tauric Research (UCLA/MIT), 2024 | Simulates a trading firm: analyst, bull and bear researcher, trader, and risk agents debate to make stock trading decisions. | consensual (bull/bear debate and risk team gate trader decisions) | research |
| 57 | [Basis](https://www.getbasis.ai/) · Basis, 2023 | Accounting agents generate journal entries, resolve reconciliations, draft technical memos, and completed an end-to-end Form 1065 tax return. | single agent (task agents execute ledger workflows with human oversight) | product |

## Healthcare

*Clinical documentation, patient outreach, prior authorization and care research.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 58 | [Abridge](https://www.abridge.com/ai) · Abridge, 2018 | Listens to patient-clinician conversations, drafts structured billable notes, captures orders, and surfaces clinical evidence using EHR context. | sequential (fixed ASR, contextual reasoning, note, coding stages) | product |
| 59 | [Polaris](https://hippocraticai.com/polaris/) · Hippocratic AI, 2024 | Conducts multi-turn voice calls with patients for chronic-care check-ins, medication guidance, and pre/post-procedure follow-up. | hierarchical (primary agent backed by specialist supervisor safety models) | product |
| 60 | [Infinitus voice AI agents](https://www.infinitus.ai/) · Infinitus Systems, 2021 | Voice agents phone insurance payors and PBMs to verify benefits, check prior-authorization status, and chase claims, navigating IVRs. | single agent (one call loop constrained by knowledge graph) | product |
| 61 | [Anterior (Florence)](https://www.anterior.com/prior-authorization-solution) · Anterior, 2024 | Reviews payer prior-authorization requests end-to-end: matches faxes, verifies eligibility, checks medical necessity against policy, approves or escalates to clinicians. | sequential (fixed gather-verify-prepare-reason-summarize stages with escalation) | product |
| 62 | [Dragon Copilot](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot) · Microsoft, 2025 | Ambient clinical assistant drafts notes, surfaces information, and automates tasks like orders, referrals, and after-visit summaries in EHR workflows. | hierarchical (assistant orchestrates embedded partner and task agents) | product |
| 63 | [AMIE](https://arxiv.org/abs/2401.05654) · Google Research / DeepMind, 2024 | Conducts text-based diagnostic dialogues: gathers history, asks questions, produces differential diagnoses; outperformed primary-care physicians in OSCE-style evaluations. | single agent (state-aware dialogue loop; self-play simulated training) | research |
| 64 | [Agent Hospital](https://arxiv.org/abs/2405.02957) · Tsinghua University, 2024 | Simulated hospital where LLM patient, nurse, and doctor agents interact; doctor agents evolve by treating thousands of simulated patients. | swarm (many peer agents in evolving hospital simulacrum) | research |

## Security and IT operations

*SOC triage, pentesting, vulnerability discovery and incident response.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 65 | [Microsoft Security Copilot Phishing Triage Agent](https://learn.microsoft.com/en-us/defender-xdr/phishing-triage-agent) · Microsoft, 2025 | Autonomously investigates user-reported phishing emails in Defender, classifying each as real threat or false alarm with evidence-backed verdict explanations. | single agent (Purpose-built autonomous triage loop, refined by analyst feedback) | product |
| 66 | [XBOW](https://xbow.com/) · XBOW, 2024 | Autonomously pentests web apps and APIs, chaining vulnerabilities into validated exploits; first AI to top HackerOne's US leaderboard. | single agent (Parallel autonomous attack loops with automated exploit validators) | product |
| 67 | [Dropzone AI](https://www.dropzone.ai/) · Dropzone AI, 2024 | Autonomously investigates SIEM, EDR and cloud alerts end-to-end, querying connected tools and producing decision-ready triage reports around the clock. | single agent (One investigation loop mimicking expert analyst reasoning across tools) | product |
| 68 | [Big Sleep](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html) · Google (Project Zero + DeepMind), 2024 | Navigates real codebases, runs sandboxed fuzzing scripts and debuggers to find exploitable bugs; discovered a SQLite zero-day, an AI first. | single agent (LLM loop with code browser, fuzzer, debugger tools) | research |
| 69 | [Charlotte AI Detection Triage](https://www.crowdstrike.com/en-us/platform/charlotte-ai/) · CrowdStrike, 2025 | Autonomously triages every endpoint detection, classifying true or false positives with 98%+ accuracy and recommending actions under bounded autonomy. | single agent (Bounded-autonomy triage loop trained on human triage decisions) | product |
| 70 | [Resolve AI (AI SRE)](https://resolve.ai/) · Resolve AI, 2024 | Investigates production incidents autonomously, correlating logs, metrics, deployments and code changes to deliver root-cause analysis and remediation steps in minutes. | hierarchical (Multi-agent system spanning code, infrastructure, observability tools) | product |
| 71 | [Aardvark (now Codex Security)](https://openai.com/index/introducing-aardvark/) · OpenAI, 2025 | Continuously scans repositories and commits, builds threat models, validates exploitability in sandboxes, and proposes Codex-generated patches for confirmed vulnerabilities. | sequential (Fixed stages: threat-model, commit scan, sandbox-validate, patch) | product |
| 72 | [PentestGPT](https://github.com/GreyDGL/PentestGPT) · Nanyang Technological University (GreyDGL), 2023 | Plans and drives penetration tests via a Pentesting Task Tree, solving CTF and real-world targets; USENIX Security 2024 paper. | hierarchical (Reasoning module directs generation and parsing LLM sessions) | open source |

## Robotics and embodied agents

*The agent loop with motors: vision-language-action models and world agents.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 73 | [Helix](https://www.figure.ai/news/helix) · Figure AI, 2025 | Controls humanoid robots' full upper body to grasp novel household objects and collaborate on multi-step tasks from voice commands. | hierarchical (slow System-2 VLM directs 200Hz motor policy) | product |
| 74 | [Gemini Robotics 1.5](https://deepmind.google/models/gemini-robotics/) · Google DeepMind, 2025 | Plans and executes multi-step manipulation on robot arms and humanoids: folding laundry, packing lunchboxes, sorting waste using web lookups. | hierarchical (ER reasoner plans and calls tools, VLA executes) | product |
| 75 | [pi-0 (π0)](https://www.pi.website/blog/pi0) · Physical Intelligence, 2024 | Generalist vision-language-action policy folds laundry, buses tables, bags groceries and assembles boxes, trained across eight robot platforms. | single agent (one flow-matching VLA policy loop) | open source |
| 76 | [Voyager](https://voyager.minedojo.org/) · NVIDIA / MineDojo, 2023 | GPT-4 agent explores Minecraft autonomously, writing code skills to mine, craft and fight, building a lifelong skill library. | single agent (one GPT-4 loop: curriculum, skills, self-verification) | research |
| 77 | [Optimus](https://www.tesla.com/optimus) · Tesla, 2022 | Bipedal humanoid in development performs object sorting and factory material handling; demos combine FSD-derived neural policies with human teleoperation. | single agent (end-to-end vision-to-action neural policy, partly teleoperated) | product |
| 78 | [Isaac GR00T N1](https://developer.nvidia.com/isaac/gr00t) · NVIDIA, 2025 | Open humanoid foundation model: grasps, moves objects bimanually and chains multistep manipulation on Fourier GR-1 and 1X robots. | single agent (dual-system VLA co-trained end-to-end, one policy) | open source |
| 79 | [PaLM-SayCan](https://say-can.github.io/) · Google Research / Everyday Robots, 2022 | Mobile kitchen robot decomposes requests like 'bring a snack' into skill sequences, LLM plans scored by affordance values. | single agent (LLM proposes steps, value functions ground execution) | research |
| 80 | [NEO (Redwood AI)](https://www.1x.tech/neo) · 1X Technologies, 2025 | Home humanoid does chores: retrieves objects, opens doors, handles laundry via onboard Redwood VLA with teleoperation fallback. | single agent (one 160M whole-body VLA on embedded GPU) | product |

## Education and personal assistants

*Tutors that teach and assistants that actually do things.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 81 | [Khanmigo](https://www.khanmigo.ai/) · Khan Academy, 2023 | Socratic AI tutor guides students through Khan Academy exercises; a background math agent verifies calculations in real time | sequential (background math agent verifies tutor responses before delivery) | product |
| 82 | [Alexa+](https://www.aboutamazon.com/news/devices/new-alexa-generative-artificial-intelligence) · Amazon, 2025 | Voice assistant that books reservations, orders groceries, and controls the home by navigating services and websites end to end | hierarchical (orchestrator routes tasks to expert agents/APIs) | product |
| 83 | [Gemini Spark](https://gemini.google/overview/agent/spark/) · Google, 2026 | Background personal agent that triages Gmail, tracks deadlines, drafts documents, and books services via Workspace apps and MCP connections | single agent (one cloud agent looping over app tools) | product |
| 84 | [Lindy](https://www.lindy.ai/) · Lindy.ai, 2023 | Executive-assistant agents triage inbox, draft replies in your voice, schedule meetings, join calls, and send follow-ups across integrations | single agent (each Lindy is a tool loop with memory) | product |
| 85 | [Zapier Agents](https://zapier.com/agents) · Zapier, 2025 | Goal-driven agents that browse the web, read live business data, and execute actions across 8,000+ integrated apps | single agent (tool loop; optional agent-to-agent delegation) | product |
| 86 | [Perplexity Assistant](https://www.perplexity.ai/help-center/en/articles/10450852-how-to-use-the-perplexity-android-assistant) · Perplexity, 2025 | Phone assistant that books tables, hails rides, drafts emails, and sets reminders by operating Android apps like OpenTable and Uber | single agent (reasoning loop invoking search and phone apps) | product |
| 87 | [Home Assistant Assist (LLM voice agent)](https://www.home-assistant.io/voice_control/) · Open Home Foundation, 2025 | Local voice assistant where an LLM agent calls device, script, and MCP tools to control the smart home | single agent (LLM conversation agent with home-control tools) | open source |

## Creative and media

*Agents that write, film, edit, animate and populate virtual worlds.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 88 | [Showrunner Agents (SHOW-1)](https://fablestudio.github.io/showrunner-agents/) · Fable Studio / The Simulation, 2023 | Character simulation plus GPT-4 prompt-chaining and diffusion models write, voice and render complete animated TV episodes from short prompts | swarm (Sims-like multi-agent character simulation drives scene generation) | research |
| 89 | [HeyGen Video Agent](https://www.heygen.com/agent) · HeyGen, 2025 | Turns one prompt into a finished video: writes script, picks visuals, generates avatar footage and voiceover, edits pacing and effects | sequential (Fixed scripting, visuals, voiceover, editing stages) | product |
| 90 | [Underlord](https://www.descript.com/underlord) · Descript, 2024 | Agentic co-editor that removes retakes, tightens pacing, fixes audio, generates clips and show notes from plain-language editing instructions | single agent (One co-editor loop with Descript editing tools) | product |
| 91 | [Inworld Character Engine](https://inworld.ai/) · Inworld AI, 2023 | Game NPCs with memory, emotions and personality that perceive game state and autonomously initiate goals, actions and dialogue | single agent (Per-NPC brain loop: goals, memory, actions) | product |
| 92 | [Jasper Agents](https://www.jasper.ai/agents) · Jasper, 2025 | 100+ specialized marketing agents autonomously plan, research, create, personalize and optimize campaign content through end-to-end content pipelines | sequential (Agents mapped to five-stage content pipeline) | product |
| 93 | [FilmAgent](https://filmagent.github.io/) · Harbin Institute of Technology (Shenzhen) & Tsinghua University, 2025 | LLM crew agents (director, screenwriter, actors, cinematographer) develop ideas, script, stage and shoot short films inside virtual 3D spaces | consensual (Critique-Correct-Verify and Debate-Judge among crew agents) | research |
| 94 | [PUBG Ally (NVIDIA ACE)](https://www.nvidia.com/en-us/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/) · KRAFTON / NVIDIA, 2025 | Co-playable AI teammate in PUBG that chats in game lingo, plans strategy, finds loot, drives vehicles and fights alongside players | single agent (On-device SLM cognition, behavior tree executes actions) | product |

## Landmark research systems

*The systems that defined the field. Dated, but every idea in this course traces back to one of them.*

| # | System | What it does | Architecture | Type |
|---|--------|--------------|--------------|------|
| 95 | [ChatDev](https://arxiv.org/abs/2307.07924) · Tsinghua University / OpenBMB, 2023 | Simulated software company where role-playing LLM agents (CEO, programmer, tester) design, code, and test applications through chat dialogues. | sequential (waterfall chat-chain of paired role-playing agents) | research |
| 96 | [Generative Agents (Smallville)](https://arxiv.org/abs/2304.03442) · Stanford University & Google Research, 2023 | 25 LLM agents inhabit a virtual town, remembering, reflecting and planning daily life, spontaneously organizing social events like a party | swarm (25 peer agents with memory, reflection, planning) | research |
| 97 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) · Significant Gravitas, 2023 | Autonomously decomposes a user goal into tasks and executes them with web search, file, and code tools until completion. | single agent (One GPT-4 loop planning and invoking tools) | open source |
| 98 | [BabyAGI](https://github.com/yoheinakajima/babyagi) · Yohei Nakajima, 2023 | Runs a continuous loop that creates, prioritizes, and executes tasks toward an objective using LLM calls and vector memory. | single agent (Single task creation, prioritization, execution loop) | open source |
| 99 | [MetaGPT](https://arxiv.org/abs/2308.00352) · DeepWisdom et al., 2023 | Turns a one-line requirement into a software project via role agents (PM, architect, engineer) following standardized operating procedures. | sequential (Assembly-line SOP stages across specialized roles) | open source |
| 100 | [CAMEL](https://arxiv.org/abs/2303.17760) · KAUST, 2023 | Two role-playing agents (user and assistant) cooperatively solve tasks through inception-prompted dialogue, generating data on agent societies. | consensual (Cooperative dialogue between role-playing agents) | research |
| 101 | [WebGPT](https://arxiv.org/abs/2112.09332) · OpenAI, 2021 | Fine-tuned GPT-3 browses a text-based web environment, searches, collects references, and answers long-form questions with citations. | single agent (One model acting in browsing environment) | research |

## Reading the catalog with the course lens

Three observations worth making in class:

1. **Most production systems are single agents or sequential pipelines.** The market agrees with Session 1's advice: if you know the steps, build a workflow; agents earn their cost when the path is decided at runtime. Hierarchical systems appear exactly where the task is open-ended (deep research, science, complex support).
2. **The same anatomy repeats everywhere.** A coding agent, a SOC triage agent and a lab robot are the same loop (reasoning + tools + memory + environment) pointed at different tools. Once you see it, framework choice becomes secondary.
3. **Verticals win on tools and guardrails, not on models.** Harvey, Abridge or XBOW mostly use the same frontier models you used in the exercises; their moat is domain tools, data access, evaluation and compliance (Session 3).

*Compiled with a multi-agent research pipeline (13 parallel domain researchers + independent fact-checkers), the same hierarchical pattern as entry #12. Corrections welcome: chema@montevive.ai*
