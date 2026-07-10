# Reproducible Machine Learning Experimentation with Traceable Agent Pipelines

- **Authors:** Wagner, T.; Moreno-Díaz, A.
- **Year:** 2025
- **Keywords:** reproducibility, experimentation, time series, traceability, MLOps

## Abstract

Experiment automation with agents raises a reproducibility question: can an autonomous pipeline be audited? We instrument a multi-agent system for time-series model development, where distinct agents handle data preparation, hyperparameter search, training, and reporting, with complete trace capture of every prompt, tool call, and artifact hash. The result is a fully replayable experiment ledger. Across 120 forecasting experiments, traced pipelines caught 23 silent data leakage errors that untraced baselines missed. We argue traceability should be a first-class requirement in agent-assisted research.
