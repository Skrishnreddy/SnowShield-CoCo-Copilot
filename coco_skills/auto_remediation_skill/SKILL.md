---
name: auto-remediation-skill
description: Autonomous vulnerability remediation and GitHub PR generator for Snowflake pipelines and repository code. Generates syntax-checked patches with zero hallucinations.
---

# Autonomous DevSecOps Remediation Skill

Performs automated patch synthesis and verification for code and pipeline vulnerabilities discovered in the enterprise data ecosystem.

## Safety Guardrails
Before any fix is proposed or PR created, the CoCo CLI agent MUST enforce:
1. **Grounding Check:** The patch must only modify the vulnerable segment and strictly preserve existing business logic and query signatures.
2. **Structural Safety Check:** Validate using AST parsing that no syntax errors, unintended variable shadowings, or introduced dependencies occur.
3. **Audit Trail:** Log the generated patch in `SNOWSHIELD_DB.RISK_INTELLIGENCE.REMEDIATION_PATCHES` before raising a GitHub Pull Request.
