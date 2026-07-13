"""A2A server exposing the course corpus researcher (Session 2 demo).

Run:  python a2a_servers/corpus_agent.py [port]      (default port 9999)

Serves the Agent Card at /.well-known/agent-card.json and the A2A JSON-RPC
endpoint at /. The skill searches the local corpus of abstracts and answers
with citations using claude-haiku-4-5 (through the course router when
LITELLM_API_KEY is set, directly against Anthropic otherwise).
"""

import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

LITELLM_API_KEY = os.getenv("LITELLM_API_KEY")
if LITELLM_API_KEY:
    os.environ["ANTHROPIC_API_KEY"] = LITELLM_API_KEY
    os.environ["ANTHROPIC_BASE_URL"] = "https://llm.montevive.ai"

import anthropic
import uvicorn
from fastapi import FastAPI

from a2a.helpers import get_message_text, new_text_message
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.routes import (
    add_a2a_routes_to_fastapi,
    create_agent_card_routes,
    create_jsonrpc_routes,
)
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentInterface,
    AgentSkill,
    Role,
)

ROOT = Path(__file__).resolve().parent.parent
CORPUS = {p.stem: p.read_text(encoding="utf-8") for p in sorted((ROOT / "data").glob("2*.md"))}


def search_corpus(query: str) -> str:
    terms = [t for t in re.findall(r"\w+", query.lower()) if len(t) > 3]
    scored = sorted(
        ((sum(text.lower().count(t) for t in terms), name) for name, text in CORPUS.items()),
        reverse=True,
    )
    top = [(s, n) for s, n in scored[:3] if s > 0]
    if not top:
        return "No results for that query."
    return "\n\n".join(f"[{name}]\n{CORPUS[name][:900]}" for _, name in top)


class CorpusResearcher(AgentExecutor):
    """The agent behind the A2A endpoint: term search + one cheap LLM call."""

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        question = get_message_text(context.message)
        findings = search_corpus(question)
        client = anthropic.AsyncAnthropic()
        msg = await client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=400,
            messages=[{
                "role": "user",
                "content": (
                    f"Question: {question}\n\nCorpus findings:\n{findings}\n\n"
                    "Answer in at most 80 words, citing papers like [2405-agent-memory]. "
                    "If the findings don't cover the question, say so."
                ),
            }],
        )
        answer = next(b.text for b in msg.content if b.type == "text")
        await event_queue.enqueue_event(
            new_text_message(
                answer,
                role=Role.ROLE_AGENT,
                context_id=context.context_id,
                task_id=context.task_id,
            )
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise NotImplementedError("cancel is not supported")


def build_app(port: int) -> FastAPI:
    card = AgentCard(
        name="corpus-researcher",
        description="Literature research over the course corpus of agentic-AI abstracts",
        version="1.0.0",
        supported_interfaces=[
            AgentInterface(url=f"http://localhost:{port}/", protocol_binding="JSONRPC"),
        ],
        capabilities=AgentCapabilities(streaming=True),
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        skills=[
            AgentSkill(
                id="corpus_search",
                name="Corpus search with citations",
                description=(
                    "Answers questions about the 12-paper corpus of agentic-AI abstracts, "
                    "citing paper identifiers."
                ),
                tags=["research", "literature", "citations"],
                examples=["What does the corpus say about agent memory versus vectorstores?"],
            )
        ],
    )
    handler = DefaultRequestHandler(
        agent_executor=CorpusResearcher(),
        task_store=InMemoryTaskStore(),
        agent_card=card,
    )
    app = FastAPI()
    add_a2a_routes_to_fastapi(
        app,
        agent_card_routes=create_agent_card_routes(card),
        jsonrpc_routes=create_jsonrpc_routes(handler, rpc_url="/"),
    )
    return app


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
    uvicorn.run(build_app(port), host="127.0.0.1", port=port, log_level="warning")
