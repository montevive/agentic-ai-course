# Context Engineering: Token Budgets, Compaction and Pruning for Cost-Effective Agents

- **Authors:** Lindqvist, E.; Tanaka, R.; Obi, F.
- **Year:** 2025
- **Keywords:** context engineering, token budget, compaction, cost optimization

## Abstract

Context windows are a budget, not a warehouse. We study context engineering strategies for agents that run for hundreds of steps: sliding-window pruning of stale tool outputs, hierarchical summarization (compaction), and offloading to external memory. On three agentic benchmarks, aggressive compaction cut token spend by 68 percent with under 2 percent quality loss, while naive truncation lost 21 percent quality. We derive practical heuristics: prune tool results after consumption, compact at 70 percent window occupancy, and never summarize the system prompt or active task specification.
