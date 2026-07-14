![Agentic AI and Multi-Agent Systems - a Montevive AI course for Fundacion AI Granada](assets/banner-readme.svg)

# Agentic Artificial Intelligence and Multi-Agent Systems

**Hands-on course · Fundacion AI Granada Research & Innovation**
13, 14 and 16 July 2026 · 10:00-12:00 · Online (live sessions)

Taught by [Montevive AI](https://montevive.ai) · Chema Robles (chema@montevive.ai)

## Course notebooks

| Notebook | Session | Open in Colab |
|---|---|---|
| [00-environment-check.ipynb](00-environment-check.ipynb) | Before you start | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/montevive/agentic-ai-course/blob/main/00-environment-check.ipynb) |
| [session-1-agent-fundamentals.ipynb](session-1-agent-fundamentals.ipynb) | Mon 13 · Agentic AI Fundamentals | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/montevive/agentic-ai-course/blob/main/session-1-agent-fundamentals.ipynb) |
| [session-2-multi-agent-systems.ipynb](session-2-multi-agent-systems.ipynb) | Tue 14 · Multi-Agent Systems | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/montevive/agentic-ai-course/blob/main/session-2-multi-agent-systems.ipynb) |
| [session-3-production-mcp.ipynb](session-3-production-mcp.ipynb) | Thu 16 · Agents in Production and Frontiers | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/montevive/agentic-ai-course/blob/main/session-3-production-mcp.ipynb) |

## Before the first session

1. Set up the environment (local or Colab, see below).
2. Get an API key: the **course key** for the Montevive LLM proxy (given at the start of the training), or your own provider key (Anthropic, OpenAI or Google).
3. Run `00-environment-check.ipynb` end to end and check that it shows 🟢.

If anything fails: **chema@montevive.ai**.

## Option A · Local environment (recommended)

Requirements: Python 3.11+ (3.12 recommended), git.

```bash
git clone https://github.com/montevive/agentic-ai-course.git
cd agentic-ai-course

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env               # and fill in your API keys

jupyter lab                        # or open the folder in VS Code
```

With **conda**:

```bash
conda create -n agentic-course python=3.12 -y
conda activate agentic-course
pip install -r requirements.txt
```

## Option B · Google Colab

Use the badges in the table above. In Colab:

- The first cell of each notebook installs the dependencies automatically.
- Add your key in the **Secrets** panel (🔑 icon in the sidebar): `LITELLM_API_KEY` with the course key (recommended), or your own `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / `GOOGLE_API_KEY`. Enable "Notebook access".

## LLM access: the Montevive proxy (recommended)

The course runs on the **Montevive LLM proxy** (`llm.montevive.ai`). You get **one** key and set it as `LITELLM_API_KEY`; every notebook then routes all three providers through the proxy automatically — no other change needed, model strings like `anthropic:claude-sonnet-4-6` keep working.

Why a proxy: it only allows the course models, so you **can't accidentally run an expensive model**, and it shares one daily budget. This is also a real example of a governance guardrail — model allowlisting, per-key budget and rate limits — the same "secure & governed AI" lens the course applies to compliance in Session 3.

| Cheap (default in exercises) | Mid tier |
|---|---|
| `claude-haiku-4-5` | `claude-sonnet-4-6` |
| `gpt-5-mini` | `gpt-5` |
| `gemini-flash-latest` | `gemini-pro-latest` |

Any other model returns `403` (intentional). The key is shared by the class: ~20 USD/day budget, 300 req/min, and it expires **2026-07-18**. Prefer the cheap tier and avoid unbounded agent loops. A `429` means wait a few seconds and retry.

**Without the proxy:** leave `LITELLM_API_KEY` empty and set your own provider key instead (`ANTHROPIC_API_KEY` recommended, or `OPENAI_API_KEY` / `GOOGLE_API_KEY`) — the notebooks then call the providers directly. One key is enough; estimated spend across the three sessions is under 2-3 EUR with the default cheap models.

## Repository structure

```
├── 00-environment-check.ipynb          Environment check (run before S1)
├── 101-real-world-agent-systems.md     Field guide: 101 real agent systems across 13 domains, fact-checked
├── 101-open-source-agent-systems.md    Companion: 101 open-source agents you can clone and adapt, API-verified
├── session-1-agent-fundamentals.ipynb  From LLM to agent · anatomy · Pydantic AI, smolagents, OpenAI Agents SDK
├── session-2-multi-agent-systems.ipynb Coordination · CrewAI vs LangGraph · context, memory and RAG
├── session-3-production-mcp.ipynb       MCP · guardrails and traceability · end-to-end pipeline · frontiers
├── data/                               Mini-corpus of abstracts (fictional) for RAG and MCP
├── assets/                             Figures, logos and banners used in the notebooks (SVG)
├── mcp_servers/
│   └── corpus_server.py                FastMCP server used in Session 3
├── a2a_servers/
│   └── corpus_agent.py                 A2A server (Agent Card + JSON-RPC) used in Session 2
├── n8n/
│   ├── agent-prototype.json            Importable n8n workflow mirroring the Session 1 agent
│   ├── multi-agent-research.json       Supervisor + sub-agents as tools (Session 2)
│   └── README.md                       How to import and run them (n8n Cloud or Docker)
├── skills/
│   └── literature-review/              Example Agent Skill (SKILL.md) used in Session 3
├── requirements.txt                    Pinned and verified dependencies
└── .env.example                        Environment variables template
```

## Program

| Session | Date | Content |
|---|---|---|
| **S1 · Agentic AI Fundamentals** | Mon 13 Jul | From LLM to agent (ReAct, tool use) · visual prototyping with n8n (importable workflow in `n8n/`) · anatomy of an agent · live implementation with Pydantic AI and smolagents · contrast with OpenAI Agents SDK |
| **S2 · Multi-Agent Systems** | Tue 14 Jul | Coordination patterns and A2A (live demo) · supervisor pattern in n8n (agents as tools) · CrewAI vs LangGraph vs Microsoft Agent Framework · multi-agent workshop · context engineering, memory (Mem0) and RAG (ChromaDB, cosine, hybrid BM25) |
| **S3 · Production and Frontiers** | Thu 16 Jul | Model Context Protocol (FastMCP) · Agent Skills (SKILL.md) · guardrails, prompt injection, PII filtering (Presidio) and traceability (Langfuse, NVIDIA NeMo Agent Toolkit) · from guardrails to compliance (GDPR, AI Act, NIS2, ISO 27001) · end-to-end multi-agent pipeline · trends 2026-2027 |

Looking for real-world examples? [**101 real-world agent systems**](101-real-world-agent-systems.md) is a fact-checked field guide of production and research agents across 13 domains, mapped to the coordination patterns taught in Session 2. Its companion, [**101 open-source agent systems**](101-open-source-agent-systems.md), lists another 101 agents whose code you can clone and adapt, every repository verified live with stack and star snapshot.

## About Montevive AI

[Montevive AI](https://montevive.ai) is an AI engineering company based in Granada. Our mission is to help businesses apply AI **securely and aligned with compliance** — GDPR, NIS2, ISO 27001, AI Act — with data protection present from the design. That lens runs through the whole course: look for the *"Secure & governed AI"* asides in each session, the live prompt-injection demo ([Prompt Injection Indirecto: Robando API Keys de Agentes IA](https://www.youtube.com/watch?v=XBAiwo-pawg), Spanish), the PII/PFI/PHI filtering exercise and the guardrails-to-regulation map in Session 3.

## License and use

Training material produced by Montevive AI for Fundacion AI Granada. The abstracts in `data/` are synthetic (fictional papers and authors). You may reuse the exercise code in your research and teaching by citing the source.
