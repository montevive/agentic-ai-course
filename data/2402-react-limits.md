# On the Limits of ReAct-Style Reasoning in Long-Horizon Tasks

- **Authors:** Dubois, A.; Yamamoto, K.
- **Year:** 2024
- **Keywords:** ReAct, long-horizon tasks, context engineering, error compounding

## Abstract

The ReAct pattern interleaves chain-of-thought reasoning with environment actions, but its performance degrades on tasks requiring more than 20 sequential steps. We evaluate ReAct agents on 400 long-horizon tasks in scientific workflow automation and find a 43 percent failure rate attributable to context saturation and error compounding. Introducing periodic state summarization and explicit sub-goal decomposition reduces failures to 17 percent. Our results suggest that context engineering, including compaction and pruning of stale observations, is essential for long-running agents.
