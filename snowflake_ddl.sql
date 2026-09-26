-- ==============================================================================
-- SnowShield: Enterprise Risk, Fraud & Regulatory Intelligence Schema
-- Snowflake AI Data Cloud DDL & Cortex Integration
-- ==============================================================================

CREATE DATABASE IF NOT EXISTS SNOWSHIELD_DB;
CREATE SCHEMA IF NOT EXISTS SNOWSHIELD_DB.RISK_INTELLIGENCE;

USE SCHEMA SNOWSHIELD_DB.RISK_INTELLIGENCE;

-- 1. Real-time Audit & Access Event Logs (Telemetry)
CREATE OR REPLACE TABLE AUDIT_EVENT_LOGS (
    EVENT_ID VARCHAR(64) PRIMARY KEY,
    TIMESTAMP TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    USER_IDENTITY VARCHAR(128),
    ROLE_USED VARCHAR(64),
    CLIENT_IP VARCHAR(45),
    QUERY_TEXT VARCHAR(4000),
    ROWS_ACCESSED NUMBER,
    DATASET_TARGET VARCHAR(256),
    ANOMALY_SCORE FLOAT,
    RISK_CATEGORY VARCHAR(64), -- 'EXFILTRATION', 'PRIVILEGE_ESCALATION', 'UNMASKED_PII_ACCESS', 'BENIGN'
    SEVERITY VARCHAR(32)       -- 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW'
);

-- 2. Regulatory Compliance Frameworks & Rules (SOC2, GDPR, PCI-DSS, HIPAA)
CREATE OR REPLACE TABLE COMPLIANCE_FRAMEWORKS (
    RULE_ID VARCHAR(32) PRIMARY KEY,
    FRAMEWORK VARCHAR(64),     -- 'GDPR', 'PCI-DSS', 'SOC2_TYPE_II', 'HIPAA'
    CONTROL_NAME VARCHAR(256),
    DESCRIPTION VARCHAR(1000),
    MANDATORY_ACTION VARCHAR(512),
    AUTOMATED_CHECK_SQL VARCHAR(2000)
);

-- 3. Pipeline & Code Vulnerability Findings
CREATE OR REPLACE TABLE VULNERABILITY_FINDINGS (
    FINDING_ID VARCHAR(64) PRIMARY KEY,
    DETECTED_AT TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    REPOSITORY VARCHAR(256),
    FILE_PATH VARCHAR(512),
    LINE_NUMBER NUMBER,
    VULNERABILITY_TYPE VARCHAR(128), -- 'SQL_INJECTION', 'HARDCODED_SECRET', 'PII_LEAK_IN_ETL', 'BROKEN_RBAC'
    SEVERITY VARCHAR(32),            -- 'CRITICAL', 'HIGH', 'MEDIUM'
    STATUS VARCHAR(32) DEFAULT 'OPEN', -- 'OPEN', 'REMEDIATING', 'RESOLVED'
    SNIPPET VARCHAR(2000),
    EXPLANATION VARCHAR(2000)
);

-- 4. Remediation Patches & Pull Request Audit Log
CREATE OR REPLACE TABLE REMEDIATION_PATCHES (
    PATCH_ID VARCHAR(64) PRIMARY KEY,
    FINDING_ID VARCHAR(64) REFERENCES VULNERABILITY_FINDINGS(FINDING_ID),
    CREATED_AT TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP(),
    PROPOSED_DIFF VARCHAR(4000),
    STRUCTURAL_SAFETY_PASSED BOOLEAN,
    GROUNDING_CHECK_PASSED BOOLEAN,
    GITHUB_PR_URL VARCHAR(512),
    STATUS VARCHAR(32) DEFAULT 'APPLIED' -- 'PENDING_REVIEW', 'APPLIED', 'REJECTED'
);

-- ==============================================================================
-- Sample Seed Data for Hackathon Demonstration
-- ==============================================================================

INSERT INTO COMPLIANCE_FRAMEWORKS VALUES 
('GDPR-Art32', 'GDPR', 'Encryption & Pseudonymization of Personal Data', 'All customer identifiers (email, SSN, phone) in warehouse staging must use Dynamic Data Masking.', 'SELECT COUNT(*) FROM SNOWSHIELD_DB.RISK_INTELLIGENCE.AUDIT_EVENT_LOGS WHERE DATASET_TARGET LIKE ''%CUSTOMER%'' AND RISK_CATEGORY = ''UNMASKED_PII_ACCESS'';'),
('PCI-Req3.4', 'PCI-DSS', 'Render Primary Account Numbers (PAN) Unreadable', 'Payment card numbers must be tokenized or masked with SHA-256 before ingestion.', 'SELECT COUNT(*) FROM SNOWSHIELD_DB.RISK_INTELLIGENCE.AUDIT_EVENT_LOGS WHERE QUERY_TEXT ILIKE ''%card_number%'' OR QUERY_TEXT ILIKE ''%cvv%'';'),
('SOC2-CC6.1', 'SOC2_TYPE_II', 'Logical Access Security & Segregation of Duties', 'Service accounts must not execute ad-hoc DDL or full table dumps exceeding 50,000 records without MFA.', 'SELECT COUNT(*) FROM SNOWSHIELD_DB.RISK_INTELLIGENCE.AUDIT_EVENT_LOGS WHERE ROWS_ACCESSED > 50000 AND ROLE_USED LIKE ''%SVC%'';');

INSERT INTO AUDIT_EVENT_LOGS VALUES
('EVT-9021', CURRENT_TIMESTAMP(), 'etl_service_acc', 'DATA_LOADER_ROLE', '10.240.12.8', 'SELECT card_number, cvv, billing_zip FROM RAW_STAGING.PAYMENTS WHERE status = ''PENDING'';', 84200, 'RAW_STAGING.PAYMENTS', 0.94, 'EXFILTRATION', 'CRITICAL'),
('EVT-9022', CURRENT_TIMESTAMP(), 'contractor_analyst', 'PUBLIC', '192.168.1.104', 'SELECT customer_id, ssn, email, phone FROM ANALYTICS.USERS LIMIT 1000;', 1000, 'ANALYTICS.USERS', 0.88, 'UNMASKED_PII_ACCESS', 'HIGH'),
('EVT-9023', CURRENT_TIMESTAMP(), 'admin_dev', 'ACCOUNTADMIN', '172.16.0.45', 'ALTER USER dev_bot SET PASSWORD = ''Pass12345!'';', 1, 'ACCOUNT_USERS', 0.76, 'PRIVILEGE_ESCALATION', 'HIGH'),
('EVT-9024', CURRENT_TIMESTAMP(), 'bi_dashboard_role', 'REPORTING_ROLE', '10.240.1.15', 'SELECT date, sum(revenue) FROM MARTS.FINANCE GROUP BY 1;', 365, 'MARTS.FINANCE', 0.05, 'BENIGN', 'LOW');

INSERT INTO VULNERABILITY_FINDINGS VALUES
('FIND-401', CURRENT_TIMESTAMP(), 'enterprise-data-pipeline', 'pipelines/ingest_transactions.py', 42, 'SQL_INJECTION', 'CRITICAL', 'OPEN', 'query = f"SELECT * FROM transactions WHERE user_id = ''{user_input}''"', 'Direct string formatting detected in Snowflake query execution. Exposes warehouse to arbitrary SQL injection.'),
('FIND-402', CURRENT_TIMESTAMP(), 'enterprise-data-pipeline', 'pipelines/customer_sync.py', 88, 'PII_LEAK_IN_ETL', 'HIGH', 'OPEN', 'df.to_csv("s3://unsecured-exports/customers.csv", columns=["ssn", "full_name"])', 'Writing unmasked personal identifiable data (SSN) to external storage without encryption or tokenization.'),
('FIND-403', CURRENT_TIMESTAMP(), 'snowflake-connectors', 'auth/warehouse_connector.py', 14, 'HARDCODED_SECRET', 'CRITICAL', 'OPEN', 'SNOWFLAKE_PASSWORD = "SnowSecret_2026_Live!"', 'Hardcoded credential discovered in repository source code.');
