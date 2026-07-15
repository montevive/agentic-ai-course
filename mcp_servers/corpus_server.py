"""MCP server for the course paper corpus.

Exposes the mini-corpus in data/ as MCP tools and resources.
Direct execution (stdio transport):

    python mcp_servers/corpus_server.py
"""

import re
from pathlib import Path

from fastmcp import FastMCP

mcp = FastMCP("corpus-papers")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CORPUS = {p.stem: p.read_text(encoding="utf-8") for p in sorted(DATA_DIR.glob("2*.md"))}


@mcp.tool
def search_papers(query: str) -> str:
    """Search papers by terms in the local corpus of abstracts on agentic AI.

    Returns the 3 most relevant papers with their identifier and the start of the text.
    """
    terms = [t for t in re.findall(r"\w+", query.lower()) if len(t) > 3]
    scored = sorted(
        ((sum(text.lower().count(t) for t in terms), name) for name, text in CORPUS.items()),
        reverse=True,
    )
    top = [(s, n) for s, n in scored[:3] if s > 0]
    if not top:
        return "No results for that query."
    return "\n\n".join(f"[{name}]\n{CORPUS[name][:900]}" for _, name in top)


@mcp.tool
def read_paper(paper_id: str) -> str:
    """Return the full text of a corpus paper given its identifier."""
    if paper_id not in CORPUS:
        available = ", ".join(sorted(CORPUS))
        return f"The paper '{paper_id}' does not exist. Available identifiers: {available}"
    return CORPUS[paper_id]


@mcp.resource("papers://list")
def list_papers() -> str:
    """List of paper identifiers available in the corpus."""
    return "\n".join(sorted(CORPUS))


@mcp.resource("papers://{paper_id}")
def paper_resource(paper_id: str) -> str:
    """Expose each paper as a readable resource (papers://2405-agent-memory)."""
    return CORPUS.get(paper_id, f"Unknown paper: {paper_id}")


@mcp.prompt
def literature_review(topic: str) -> str:
    """Reusable prompt template: a cited mini literature review on a topic."""
    return (
        f"Write a short literature review on '{topic}' using ONLY the corpus.\n"
        "1. Call search_papers to find the relevant papers.\n"
        "2. Call read_paper on the most relevant ones.\n"
        "3. Answer in under 150 words, citing every claim like [2405-agent-memory]."
    )


if __name__ == "__main__":
    mcp.run()
