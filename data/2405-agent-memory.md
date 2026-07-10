# Beyond the Context Window: Comparing Memory Layers for Conversational Agents

- **Authors:** Rossi, F.; Adeyemi, O.; Kaur, P.
- **Year:** 2024
- **Keywords:** agent memory, Mem0, vectorstore, personalization, token efficiency

## Abstract

Vector stores retrieve documents; memory layers remember users. We compare three agent memory systems (Mem0, Letta, Zep) against a plain vectorstore baseline on 5,000 multi-session dialogues. Memory layers that extract and consolidate salient facts outperform raw retrieval by 26 percent on personalization benchmarks while using 90 percent fewer tokens per query. However, fact extraction introduces latency at write time and occasional consolidation errors. We propose a hybrid design: episodic vectorstore for verbatim recall, semantic memory layer for user preferences and stable facts.
