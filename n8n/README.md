# n8n workflow: visual prototype of the Session 1 agent

`agent-prototype.json` is an importable [n8n](https://n8n.io) workflow that reproduces, with zero code, the agent built by hand in `session-1-agent-fundamentals.ipynb`: a chat-triggered *AI Agent* with an Anthropic model, short-term memory and two tools (a calculator and a `fetch_paper` HTTP tool that reads the course corpus straight from this repository).

## Run it in 5 minutes

1. **Open an n8n instance.** Either:
   - [n8n Cloud](https://n8n.io) (free trial), or
   - locally with Docker:

     ```bash
     docker run -it --rm -p 5678:5678 n8nio/n8n
     ```

     then open http://localhost:5678.
2. **Import the workflow.** New workflow → menu (top right) → **Import from File...** → select `agent-prototype.json`.
3. **Add your Anthropic credential.** Open the *Anthropic Chat Model* node and create a credential with your `ANTHROPIC_API_KEY` (the same one used in the notebooks).
4. **Chat with it.** Click **Open chat** and try:

   > What does the paper on multi-agent coordination say about which pattern wins on quality? And what is 987654 * 123457?

   Open the execution view to watch the loop: the agent calls `fetch_paper`, reads the abstract, calls `Calculator`, and only then answers — the same ReAct cycle as `run_agent()` in the notebook.

## Node-to-code mapping

| n8n node | In the Session 1 notebook |
|---|---|
| *When chat message received* | the user `question` |
| *AI Agent* | the `run_agent()` loop |
| *Anthropic Chat Model* | `client.messages.create(...)` |
| *Simple Memory* | the `messages` list |
| *Calculator* / *fetch_paper* | `TOOLS` + `TOOL_FUNCTIONS` |

## When to use which

- **n8n**: validating an idea with non-technical stakeholders, internal automations, quick integrations (Gmail, Slack, Drive and 400+ connectors), webhook-triggered agents.
- **Code**: anything you must test, version, review and ship to production — typed outputs, guardrails, evaluation and traceability (Session 3) live in code.
