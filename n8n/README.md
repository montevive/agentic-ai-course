# n8n workflows: the course agents, visually

Two importable [n8n](https://n8n.io) workflows that reproduce, with zero code, agents built in the notebooks:

| File | Session | What it shows |
|---|---|---|
| `agent-prototype.json` | 1 | A single agent: chat trigger, Anthropic model, memory, two tools (calculator + `fetch_paper`) |
| `multi-agent-research.json` | 2 | A multi-agent team: a supervisor agent that delegates to two sub-agents exposed as **AI Agent Tool** nodes |

## Run them in 5 minutes

1. **Open an n8n instance.** Either:
   - [n8n Cloud](https://n8n.io) (free trial), or
   - locally with Docker:

     ```bash
     docker run -it --rm -p 5678:5678 n8nio/n8n
     ```

     then open http://localhost:5678.
2. **Import the workflow.** New workflow → menu (top right) → **Import from File...** → select the `.json` file.
3. **Add your Anthropic credential.** Open any *Anthropic Chat Model* node and create a credential with your `ANTHROPIC_API_KEY`. With the **course key**, also set the credential's *Base URL* to `https://llm.montevive.ai` so calls go through the course router. The multi-agent workflow has three model nodes (supervisor, researcher, writer): assign the same credential to all three.
4. **Chat with it.** Click **Open chat**.

   For the Session 1 agent:

   > What does the paper on multi-agent coordination say about which pattern wins on quality? And what is 987654 * 123457?

   For the Session 2 team:

   > What does the corpus say about agent memory layers versus vectorstores?

   Open the execution view to watch the flow. In the multi-agent workflow you'll see the supervisor call `researcher_agent` (which loops on `fetch_paper` with its own model), then `writer_agent`, then return the synthesis - the *agent-as-tool* delegation pattern from Session 2, on one canvas.

## Node-to-code mapping

Session 1 (`agent-prototype.json`):

| n8n node | In the Session 1 notebook |
|---|---|
| *When chat message received* | the user `question` |
| *AI Agent* | the `run_agent()` loop |
| *Anthropic Chat Model* | `client.messages.create(...)` |
| *Simple Memory* | the `messages` list |
| *Calculator* / *fetch_paper* | `TOOLS` + `TOOL_FUNCTIONS` |

Session 2 (`multi-agent-research.json`):

| n8n node | In the Session 2 notebook |
|---|---|
| *Supervisor* (AI Agent) | the orchestrator agent (Session 3 pipeline uses the same pattern) |
| *researcher_agent* / *writer_agent* (AI Agent Tool) | specialists exposed as tools: `delegate_research(...)`, `delegate_writing(...)` |
| each sub-agent's own *Anthropic Chat Model* | one bounded context per specialist |
| *fetch_paper* inside the researcher | the researcher's `search_corpus` tool |

The **AI Agent Tool** node is what makes single-canvas multi-agent possible: the supervisor keeps control and receives each specialist's answer as a tool result (*agent-as-tool*), as opposed to a *handoff* where the conversation is transferred. Both mechanics are discussed in Session 2, Block 1.

## When to use which

- **n8n**: validating an idea with non-technical stakeholders, internal automations, quick integrations (Gmail, Slack, Drive and 400+ connectors), webhook-triggered agents.
- **Code**: anything you must test, version, review and ship to production — typed outputs, guardrails, evaluation and traceability (Session 3) live in code.
