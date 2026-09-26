---
name: risk-audit-skill
description: Autonomous risk and fraud detection skill for Snowflake CoCo CLI. Analyzes query telemetry, anomaly patterns, and exfiltration attempts against the Snowflake AI Data Cloud.
---

# Risk & Fraud Audit Skill for Snowflake CoCo CLI

This skill equips the Snowflake CoCo agent with automated intelligence to inspect access logs, detect data exfiltration attempts, and uncover anomalous query spikes.

## Activation Triggers
Activate this skill when:
- The user requests an audit of recent queries or warehouse activity.
- Unusual data volumes or unmasked PII access are flagged.
- An alert triggers on `EXFILTRATION` or `PRIVILEGE_ESCALATION`.

## Workflow
1. **Fetch Telemetry:** Query `SNOWSHIELD_DB.RISK_INTELLIGENCE.AUDIT_EVENT_LOGS` for anomalies where `ANOMALY_SCORE > 0.70` or `SEVERITY IN ('CRITICAL', 'HIGH')`.
2. **Contextualize with Cortex AI:** Call `SNOWFLAKE.CORTEX.COMPLETE('mistral-large2', ...)` to synthesize:
   - Behavioral deviation vs. 30-day baseline.
   - Identified blast radius (tables, rows, sensitive columns accessed).
   - Recommended immediate containment steps (e.g. `REVOKE ROLE`, `KILL QUERY`).
3. **Report:** Output an executive threat summary with actionable remediation commands.
