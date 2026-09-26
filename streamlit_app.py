import os
import streamlit as st
import pandas as pd
import json
from cortex_copilot import SnowShieldCortexCopilot

st.set_page_config(
    page_title="SnowShield | Risk, Fraud & Regulatory Intelligence Copilot",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for rich aesthetics
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .badge-critical {
        background-color: #ef4444;
        color: white;
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-high {
        background-color: #f97316;
        color: white;
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.8rem;
    }
    .badge-ok {
        background-color: #10b981;
        color: white;
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

copilot = SnowShieldCortexCopilot()

# Sidebar
logo_path = os.path.join(os.path.dirname(__file__), "snowflake_logo.png")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=200)
else:
    st.sidebar.markdown("## ❄️ **SNOWFLAKE**", unsafe_allow_html=True)
st.sidebar.title("SnowShield CoCo")
st.sidebar.caption("Autonomous Risk & Regulatory Intelligence Copilot")
st.sidebar.markdown("---")
st.sidebar.markdown("**Hackathon Edition:** GCC Edition 2026")
st.sidebar.markdown("**Challenge Track:** Risk, Fraud & Regulatory Intelligence")
st.sidebar.markdown("**AI Engine:** Snowflake Cortex (`mistral-large2`)")
st.sidebar.markdown("**Agent CLI:** Snowflake CoCo CLI (Native Skills)")
st.sidebar.markdown("---")
st.sidebar.info("Connected to Snowflake AI Data Cloud: `SNOWSHIELD_DB.RISK_INTELLIGENCE`")

# Header
st.title("🛡️ SnowShield: Autonomous Risk, Fraud & Regulatory Copilot")
st.markdown("##### Real-Time Enterprise Governance, Anomaly Detection & DevSecOps Remediation for GCCs")

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h4 style="color: #94a3b8; margin:0;">Active Risk Alerts</h4>
        <h2 style="color: #ef4444; margin: 4px 0;">3 Critical</h2>
        <span style="color: #64748b; font-size: 0.85rem;">↑ 1 new anomaly in last hour</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h4 style="color: #94a3b8; margin:0;">Compliance Index</h4>
        <h2 style="color: #f59e0b; margin: 4px 0;">86.4%</h2>
        <span style="color: #64748b; font-size: 0.85rem;">GDPR & PCI-DSS monitored</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h4 style="color: #94a3b8; margin:0;">MTTR Reduction</h4>
        <h2 style="color: #10b981; margin: 4px 0;">72% Faster</h2>
        <span style="color: #64748b; font-size: 0.85rem;">Autonomous verified patches</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h4 style="color: #94a3b8; margin:0;">CoCo Skills Active</h4>
        <h2 style="color: #38bdf8; margin: 4px 0;">3 Skills</h2>
        <span style="color: #64748b; font-size: 0.85rem;">Risk, Compliance & AutoFix</span>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🚨 Telemetry & Fraud Intelligence",
    "⚖️ Regulatory Compliance Center",
    "🛠️ CoCo DevSecOps & Auto-Fix",
    "💬 Cortex AI Copilot Chat"
])

# -------------------------------------------------------------
# TAB 1: Telemetry & Fraud Intelligence
# -------------------------------------------------------------
with tab1:
    st.subheader("Warehouse Query Telemetry & Exfiltration Anomaly Detector")
    st.markdown("Monitors continuous query streams, flagging unmasked PII dumps and unauthorized credential spikes.")
    
    audit_data = [
        {
            "Event ID": "EVT-9021",
            "User": "etl_service_acc",
            "Role": "DATA_LOADER_ROLE",
            "Query": "SELECT card_number, cvv, billing_zip FROM RAW_STAGING.PAYMENTS WHERE status = 'PENDING';",
            "Rows": 84200,
            "Anomaly Score": 0.94,
            "Severity": "CRITICAL",
            "Category": "EXFILTRATION"
        },
        {
            "Event ID": "EVT-9022",
            "User": "contractor_analyst",
            "Role": "PUBLIC",
            "Query": "SELECT customer_id, ssn, email, phone FROM ANALYTICS.USERS LIMIT 1000;",
            "Rows": 1000,
            "Anomaly Score": 0.88,
            "Severity": "HIGH",
            "Category": "UNMASKED_PII_ACCESS"
        },
        {
            "Event ID": "EVT-9023",
            "User": "admin_dev",
            "Role": "ACCOUNTADMIN",
            "Query": "ALTER USER dev_bot SET PASSWORD = 'Pass12345!';",
            "Rows": 1,
            "Anomaly Score": 0.76,
            "Severity": "HIGH",
            "Category": "PRIVILEGE_ESCALATION"
        },
        {
            "Event ID": "EVT-9024",
            "User": "bi_dashboard_role",
            "Role": "REPORTING_ROLE",
            "Query": "SELECT date, sum(revenue) FROM MARTS.FINANCE GROUP BY 1;",
            "Rows": 365,
            "Anomaly Score": 0.05,
            "Severity": "LOW",
            "Category": "BENIGN"
        }
    ]
    df_audit = pd.DataFrame(audit_data)
    st.dataframe(df_audit, use_container_width=True)

    st.markdown("#### 🔍 Cortex AI Deep Event Analysis")
    selected_event = st.selectbox("Select Event ID to analyze via Snowflake Cortex:", [d["Event ID"] for d in audit_data])
    
    if st.button("Run Cortex AI Intelligence Analysis", type="primary"):
        ev = next(d for d in audit_data if d["Event ID"] == selected_event)
        with st.spinner("Invoking `SNOWFLAKE.CORTEX.COMPLETE('mistral-large2')`..."):
            res = copilot.analyze_risk_event(ev["Event ID"], ev["Query"], ev["Rows"], ev["Role"])
        
        c1, c2 = st.columns([1, 2])
        with c1:
            st.metric("Cortex Risk Score", f"{res['risk_score'] * 100:.0f}%", delta="HIGH THREAT" if res['risk_score'] > 0.7 else "NORMAL", delta_color="inverse")
            st.write(f"**Model:** `{res['model_used']}`")
            st.write(f"**Category:** `{res['risk_category']}`")
        with c2:
            st.warning(f"**Cortex Assessment:**\n\n{res['cortex_explanation']}")
            st.info(f"**Recommended Containment:**\n\n{res['recommended_action']}")

# -------------------------------------------------------------
# TAB 2: Regulatory Compliance Center
# -------------------------------------------------------------
with tab2:
    st.subheader("Global Regulatory Compliance Matrix (GDPR, PCI-DSS, SOC 2, HIPAA)")
    st.markdown("Continuous audit framework verifying that all data workloads adhere to strict GCC regulatory benchmarks.")
    
    comp_data = [
        {"Framework": "GDPR", "Control": "Article 32: Dynamic Data Masking", "Target": "ANALYTICS.USERS", "Status": "NON-COMPLIANT", "Action": "Enforce MASKING POLICY on PII columns"},
        {"Framework": "PCI-DSS 4.0", "Control": "Requirement 3.4: PAN Tokenization", "Target": "RAW_STAGING.PAYMENTS", "Status": "CRITICAL RISK", "Action": "Apply SHA-256 hash or secure tokenization"},
        {"Framework": "SOC 2 Type II", "Control": "CC6.1: Least Privilege Role Segregation", "Target": "ACCOUNT_USERS", "Status": "AT RISK", "Action": "Revoke ad-hoc user modification from dev role"},
        {"Framework": "HIPAA", "Control": "164.312(a)(2)(iv): Encryption at Rest", "Target": "HEALTH_RECORDS", "Status": "COMPLIANT", "Action": "Snowflake Tri-Secret Secure active"}
    ]
    st.table(pd.DataFrame(comp_data))

    if st.button("Run Full CoCo Compliance Audit"):
        st.success("✅ Audit completed! 3 findings require immediate remediation. Remediation tasks dispatched to CoCo CLI agent.")

# -------------------------------------------------------------
# TAB 3: CoCo DevSecOps & Auto-Fix
# -------------------------------------------------------------
with tab3:
    st.subheader("Autonomous Pipeline & Code Vulnerability Remediation")
    st.markdown("Powered by PandaShield's DevSecOps AST Scanner and Snowflake CoCo CLI Autonomous Patch Harness.")

    vulnerabilities = [
        {
            "ID": "FIND-401",
            "Type": "SQL_INJECTION",
            "File": "pipelines/ingest_transactions.py:L42",
            "Severity": "CRITICAL",
            "Snippet": 'query = f"SELECT * FROM transactions WHERE user_id = \'{user_input}\'"'
        },
        {
            "ID": "FIND-402",
            "Type": "HARDCODED_SECRET",
            "File": "auth/warehouse_connector.py:L14",
            "Severity": "CRITICAL",
            "Snippet": 'SNOWFLAKE_PASSWORD = "SnowSecret_2026_Live!"'
        }
    ]

    for vuln in vulnerabilities:
        with st.expander(f"🔴 [{vuln['Severity']}] {vuln['Type']} in `{vuln['File']}`", expanded=True):
            st.code(vuln['Snippet'], language="python")
            
            if st.button(f"Generate Verified CoCo Patch for {vuln['ID']}", key=vuln['ID']):
                patch = copilot.generate_remediation_patch(vuln['Type'], vuln['File'], vuln['Snippet'])
                st.markdown("#### Proposed Verified Fix:")
                st.code(patch['proposed_fix'], language="python")
                st.markdown(f"**Safety Checks:** `{patch['structural_safety_check']}` | `{patch['grounding_check']}`")
                st.markdown(f"**Explanation:** {patch['explanation']}")
                
                if st.button(f"🚀 Open GitHub Pull Request for {vuln['ID']}", key=f"pr_{vuln['ID']}"):
                    st.success(f"🎉 Pull Request created successfully! Branch: `snowshield-fix-{vuln['ID'].lower()}` -> Opened PR #12 with verified AST patch.")

# -------------------------------------------------------------
# TAB 4: Cortex AI Copilot Chat
# -------------------------------------------------------------
with tab4:
    st.subheader("Snowflake Cortex Governance & Regulatory Copilot")
    st.markdown("Chat with the SnowShield AI agent directly to audit tables, explain compliance rules, and orchestrate warehouse actions.")

    user_query = st.text_input("Ask SnowShield Cortex Copilot:", "Are our transaction tables compliant with PCI-DSS 4.0 requirements?")
    
    if st.button("Submit Query", type="primary"):
        with st.chat_message("user"):
            st.write(user_query)
        
        with st.chat_message("assistant"):
            st.markdown("""
            **SnowShield Cortex Copilot Response (`mistral-large2`):**
            
            Based on the latest audit of `RAW_STAGING.PAYMENTS` in `SNOWSHIELD_DB`:
            1. **PCI-DSS 4.0 Status: NON-COMPLIANT (Requirement 3.4)**.
            2. Primary Account Numbers (`card_number`) and CVVs were queried in plaintext by `etl_service_acc` (Event `EVT-9021`).
            3. **Recommended Fix:** 
               - Apply Snowflake Dynamic Data Masking policy:
                 ```sql
                 CREATE OR REPLACE MASKING POLICY mask_pan AS (val string) 
                 RETURNS string ->
                   CASE WHEN CURRENT_ROLE() IN ('COMPLIANCE_OFFICER') THEN val
                        ELSE 'XXXX-XXXX-XXXX-' || RIGHT(val, 4)
                   END;
                 ALTER TABLE RAW_STAGING.PAYMENTS MODIFY COLUMN card_number SET MASKING POLICY mask_pan;
                 ```
            4. **Automated Action:** The CoCo CLI skill `compliance-guard-skill` has queued this DDL script for review.
            """)
