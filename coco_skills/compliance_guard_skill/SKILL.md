---
name: compliance-guard-skill
description: Regulatory intelligence and compliance auditor for Snowflake CoCo CLI. Evaluates data pipelines and warehouse policies against GDPR, SOC 2, PCI-DSS, and HIPAA controls.
---

# Regulatory Compliance Guard Skill

Empowers the CoCo CLI agent to run compliance benchmark evaluations against active schemas and pipelines.

## Target Frameworks
- **GDPR (Articles 32, 25):** Ensures Dynamic Data Masking (DDM) on identifiers and PII in European GCC instances.
- **PCI-DSS 4.0 (Req 3.4 & 10):** Validates hashing/tokenization on Primary Account Numbers (PAN) and immutable audit trails.
- **SOC 2 Type II (CC6.1 - CC6.8):** Enforces least-privilege role segregation and flags cross-account admin elevation.

## Instructions
1. Map incoming pipeline definition or table schema against `SNOWSHIELD_DB.RISK_INTELLIGENCE.COMPLIANCE_FRAMEWORKS`.
2. Execute automated check queries to compute the compliance violation index.
3. Formulate an audit compliance matrix with control status: `COMPLIANT`, `AT RISK`, or `NON-COMPLIANT`.
