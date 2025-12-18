## AutoLoop Runbook

Purpose:
Continuously ingest data, analyze, predict, plan, and execute.

Triggers:
- Container start
- Interval-based execution

Failure Handling:
- Exception → auto-heal
- Repeated failure → degraded state
- Emergency stop via manifest

No human input required.
