# Guardrails and Evaluation Pipelines for Production LLM Agents

- **Authors:** Bianchi, V.; Osei, K.; Larsen, M.
- **Year:** 2025
- **Keywords:** guardrails, evaluation, observability, human-in-the-loop, tracing

## Abstract

Deploying agents without output validation is deploying undefined behavior. We survey guardrail techniques, including schema-constrained generation, input sanitization against prompt injection, human-in-the-loop approval gates, and post-hoc verification, and measure their effect on a customer-facing research assistant over six months. Layered guardrails reduced harmful or off-policy outputs by 94 percent with a 7 percent increase in latency. We further show that trace-based evaluation with tools such as LangSmith, Langfuse and Arize Phoenix enables regression testing of agent behavior across model upgrades.
