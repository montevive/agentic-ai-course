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
2. Get **at least one** API key (Anthropic, OpenAI or Google).
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
- Add your keys in the **Secrets** panel (🔑 icon in the sidebar) with the names `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` or `GOOGLE_API_KEY`, and enable "Notebook access".

## API keys

| Provider | Variable | Console | Notes |
|---|---|---|---|
| Anthropic (Claude) | `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/) | Recommended as the primary provider in the course |
| OpenAI | `OPENAI_API_KEY` | [platform.openai.com](https://platform.openai.com/) | Only needed for the OpenAI Agents SDK block |
| Google (Gemini) | `GOOGLE_API_KEY` | [aistudio.google.com](https://aistudio.google.com/apikey) | A valid alternative in almost every exercise |

One key is enough to follow the course. The exercises use low-cost models by default (Claude Haiku / Sonnet, GPT mini, Gemini Flash): the estimated spend across the three sessions is under 2-3 EUR. Access will be provided during the training to anyone who needs it.

## Repository structure

```
├── 00-environment-check.ipynb          Environment check (run before S1)
├── session-1-agent-fundamentals.ipynb  From LLM to agent · anatomy · Pydantic AI, smolagents, OpenAI Agents SDK
├── session-2-multi-agent-systems.ipynb Coordination · CrewAI vs LangGraph · context, memory and RAG
├── session-3-production-mcp.ipynb       MCP · guardrails and traceability · end-to-end pipeline · frontiers
├── data/                               Mini-corpus of abstracts (fictional) for RAG and MCP
├── assets/                             Figures, logos and banners used in the notebooks (SVG)
├── mcp_servers/
│   └── corpus_server.py                FastMCP server used in Session 3
├── requirements.txt                    Pinned and verified dependencies
└── .env.example                        Environment variables template
```

## Program

| Session | Date | Content |
|---|---|---|
| **S1 · Agentic AI Fundamentals** | Mon 13 Jul | From LLM to agent (ReAct, tool use) · anatomy of an agent · live implementation with Pydantic AI and smolagents · contrast with OpenAI Agents SDK |
| **S2 · Multi-Agent Systems** | Tue 14 Jul | Coordination patterns and A2A · CrewAI vs LangGraph vs Microsoft Agent Framework · multi-agent workshop · context engineering, memory (Mem0) and RAG (ChromaDB) |
| **S3 · Production and Frontiers** | Thu 16 Jul | Model Context Protocol (FastMCP) · guardrails, human-in-the-loop and traceability (Langfuse, NVIDIA NeMo Agent Toolkit) · end-to-end multi-agent pipeline · trends 2026-2027 |

## License and use

Training material produced by Montevive AI for Fundacion AI Granada. The abstracts in `data/` are synthetic (fictional papers and authors). You may reuse the exercise code in your research and teaching by citing the source.
