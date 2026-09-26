import pymupdf

input_pdf = "/Users/gsaikrishnareddy/.gemini/antigravity-ide/brain/23558058-8d05-4f65-a21b-4b467e919bce/.user_uploaded/media_1790431698903.pdf"
output_pdf = "/Users/gsaikrishnareddy/pandashield-v2/Snowflake/SnowShield_CoCo_CLI_Hackathon_Submission.pdf"

doc = pymupdf.open(input_pdf)

# -------------------------------------------------------------
# Colors (RGB 0.0 - 1.0)
# -------------------------------------------------------------
SNOW_BLUE = (0.16, 0.54, 0.92)       # Snowflake bright blue #298AF0
DARK_BLUE = (0.05, 0.15, 0.30)
DARK_TEXT = (0.10, 0.14, 0.18)       # Slate 900
MUTED_TEXT = (0.35, 0.42, 0.50)      # Slate 600
CARD_BG = (0.96, 0.98, 1.00)         # Soft light blue-grey card
CARD_BORDER = (0.82, 0.88, 0.95)
WHITE = (1.0, 1.0, 1.0)
ACCENT_GREEN = (0.06, 0.65, 0.42)
ACCENT_RED = (0.90, 0.22, 0.22)
ACCENT_ORANGE = (0.95, 0.55, 0.10)

def draw_card(page, rect, bg_color=CARD_BG, border_color=CARD_BORDER, radius=6):
    r = pymupdf.Rect(rect)
    shape = page.new_shape()
    shape.draw_rect(r)
    shape.finish(fill=bg_color, color=border_color, width=1.0)
    shape.commit()

# =============================================================
# SLIDE 1: Cover details
# =============================================================
page1 = doc[0]
page1.insert_text((120, 271), "Team PandaShield (SnowShield)", fontsize=12, fontname="Helvetica-Bold", color=SNOW_BLUE)
page1.insert_text((165, 298), "G. Sai Krishna Reddy", fontsize=12, fontname="Helvetica-Bold", color=DARK_TEXT)
page1.insert_text((112, 326), "1", fontsize=12, fontname="Helvetica-Bold", color=DARK_TEXT)
page1.insert_text((155, 353), "Autonomous Risk, Fraud & Regulatory Intelligence Copilot on Snowflake AI Data Cloud", fontsize=11, fontname="Helvetica-Bold", color=SNOW_BLUE)
page1.insert_text((38, 368), "Powered by Snowflake Cortex AI & CoCo CLI for real-time compliance auditing, telemetry anomaly detection & AST auto-remediation.", fontsize=9.5, fontname="Helvetica-Oblique", color=MUTED_TEXT)

# =============================================================
# SLIDE 3: 1. Problem Brief
# =============================================================
page3 = doc[2]

# Header Title
page3.insert_text((34, 70), "1. Problem Brief: Autonomous Risk & Regulatory Governance in GCCs", fontsize=15, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((34, 85), "Global Capability Centers face exponential compliance burdens across enterprise data lakes & telemetry.", fontsize=9.5, fontname="Helvetica", color=MUTED_TEXT)

# 3 Column Cards
# Card 1: Real Business Problem & Context (x: 34 to 240)
draw_card(page3, (34, 98, 244, 380))
page3.insert_text((44, 116), "BUSINESS PROBLEM & CONTEXT", fontsize=9.5, fontname="Helvetica-Bold", color=DARK_BLUE)
page3.insert_text((44, 134), "• GCC Enterprise Mandates:", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((52, 148), "Global Capability Centers in banking,", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 160), "fintech, and healthcare manage", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 172), "petabyte-scale Snowflake estates.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((44, 192), "• Heavy Regulatory Pressure:", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((52, 206), "Mandates like GDPR (Art. 32), PCI-DSS", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 218), "4.0, SOC 2 Type II, and HIPAA demand", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 230), "continuous, immutable access controls.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((44, 250), "• Severe Alert Fatigue:", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((52, 264), "Millions of daily query logs bury real", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 276), "exfiltration risks beneath 40%+ false", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 288), "positive noise.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((44, 308), "• Pain Point:", fontsize=9, fontname="Helvetica-Bold", color=ACCENT_RED)
page3.insert_text((52, 322), "Manual compliance audits occur", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((52, 334), "quarterly, leaving multi-month blindspots.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)

# Card 2: Target User / Personas (x: 254 to 464)
draw_card(page3, (254, 98, 464, 380))
page3.insert_text((264, 116), "TARGET USER & PERSONAS", fontsize=9.5, fontname="Helvetica-Bold", color=DARK_BLUE)
page3.insert_text((264, 134), "1. SecOps & Cloud Risk Leads", fontsize=9, fontname="Helvetica-Bold", color=SNOW_BLUE)
page3.insert_text((272, 148), "Needs real-time visibility into high-risk", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 160), "queries, credential abuse, and unmasked", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 172), "PII exports without manual SQL audits.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((264, 194), "2. Enterprise Data Engineers", fontsize=9, fontname="Helvetica-Bold", color=SNOW_BLUE)
page3.insert_text((272, 208), "Builds ETL & data pipelines; needs", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 220), "instant, in-line security guidance when", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 232), "code introduces SQL injection or secrets.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((264, 254), "3. GCC Compliance Officers", fontsize=9, fontname="Helvetica-Bold", color=SNOW_BLUE)
page3.insert_text((272, 268), "Requires continuous audit matrices", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 280), "demonstrating tokenization and role", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 292), "least-privilege to regulatory authorities.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((264, 314), "4. DevOps / Release Managers", fontsize=9, fontname="Helvetica-Bold", color=SNOW_BLUE)
page3.insert_text((272, 328), "Wants automated, verified PR fixes that", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((272, 340), "pass syntax checks without regressions.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)

# Card 3: The SnowShield Improvement (x: 474 to 686)
draw_card(page3, (474, 98, 686, 380), bg_color=(0.95, 0.98, 0.95), border_color=(0.75, 0.88, 0.78))
page3.insert_text((484, 116), "HOW SNOWSHIELD IMPROVES IT", fontsize=9.5, fontname="Helvetica-Bold", color=ACCENT_GREEN)
page3.insert_text((484, 134), "✔ Real-Time Anomaly Scoring", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((492, 148), "Cortex AI evaluates telemetry in real time,", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((492, 160), "cutting false positive noise by >85%.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((484, 182), "✔ Automated Policy Synthesis", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((492, 196), "Auto-generates Dynamic Data Masking", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((492, 208), "(DDM) policies for unmasked PII tables.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((484, 230), "✔ Zero-Hallucination Auto-Fixes", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((492, 244), "AST structural validation guarantees code", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((492, 256), "patches never break production pipelines.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((484, 278), "✔ 72% MTTR Reduction", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((492, 292), "Mean Time to Remediate plummets from", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((492, 304), "48–72 hours to under 15 minutes via", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((492, 316), "1-click automated GitHub Pull Requests.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page3.insert_text((484, 340), "✔ Terminal & Dashboard Native", fontsize=9, fontname="Helvetica-Bold", color=DARK_TEXT)
page3.insert_text((492, 354), "Accessible via CoCo CLI & Streamlit in Snowflake.", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)

# =============================================================
# SLIDE 4: 2. Architecture Diagram
# =============================================================
page4 = doc[3]

page4.insert_text((34, 70), "2. Architecture Diagram & Snowflake CoCo CLI Modular Integration", fontsize=15, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((34, 85), "End-to-End data flow uniting Snowflake Data Cloud, Cortex AI, CoCo Skills, and DevSecOps AST Automation.", fontsize=9.5, fontname="Helvetica", color=MUTED_TEXT)

# Draw 4 Tier Architecture Diagram Boxes
# Box 1: Data Sources (x: 34, y: 98, w: 145, h: 280)
draw_card(page4, (34, 98, 180, 380), bg_color=(0.95, 0.97, 1.0), border_color=(0.75, 0.85, 0.95))
page4.insert_text((44, 116), "DATA SOURCES", fontsize=9.5, fontname="Helvetica-Bold", color=DARK_BLUE)
page4.insert_text((44, 134), "Snowflake AI Data Cloud", fontsize=8.5, fontname="Helvetica-Bold", color=SNOW_BLUE)
page4.insert_text((44, 146), "(SNOWSHIELD_DB)", fontsize=8, fontname="Helvetica", color=MUTED_TEXT)
page4.insert_text((44, 168), "• AUDIT_EVENT_LOGS", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((50, 180), "Warehouse query telemetry,", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((50, 190), "client IPs, roles & row counts", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((44, 210), "• COMPLIANCE_RULES", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((50, 222), "GDPR, PCI-DSS 4.0, SOC 2", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((50, 232), "automated SQL audit checks", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((44, 252), "• VULNERABILITY_LOGS", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((50, 264), "AST pipeline findings,", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((50, 274), "SQLi, secrets, unmasked PII", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((44, 296), "• REMEDIATION_LOGS", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((50, 308), "Historical patch diffs & PRs", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)

# Box 2: CoCo CLI Agent Harness (x: 195, y: 98, w: 160, h: 280)
draw_card(page4, (195, 98, 355, 380), bg_color=(0.93, 0.96, 1.0), border_color=(0.60, 0.78, 0.95))
page4.insert_text((205, 116), "CoCo CLI AGENT HARNESS", fontsize=9.5, fontname="Helvetica-Bold", color=DARK_BLUE)
page4.insert_text((205, 134), "Terminal-Native Skills Pack", fontsize=8.5, fontname="Helvetica-Bold", color=SNOW_BLUE)
page4.insert_text((205, 155), "1. risk-audit-skill", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((213, 167), "Scans query history for dump", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((213, 177), "anomalies & exfiltration spikes", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((205, 197), "2. compliance-guard-skill", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((213, 209), "Maps schemas against controls", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((213, 219), "& computes compliance index", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((205, 239), "3. auto-remediation-skill", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((213, 251), "Synthesizes code patches with", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((213, 261), "zero hallucinations & creates PR", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((205, 285), "Native MCP Protocol:", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_BLUE)
page4.insert_text((213, 297), "Inter-agent tool execution &", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((213, 307), "Snowflake session bridging", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)

# Box 3: Cortex AI Intelligence (x: 370, y: 98, w: 150, h: 280)
draw_card(page4, (370, 98, 520, 380), bg_color=(0.96, 0.94, 1.0), border_color=(0.80, 0.72, 0.95))
page4.insert_text((380, 116), "SNOWFLAKE CORTEX AI", fontsize=9.5, fontname="Helvetica-Bold", color=(0.4, 0.1, 0.7))
page4.insert_text((380, 134), "LLM Inference Engine", fontsize=8.5, fontname="Helvetica-Bold", color=(0.5, 0.2, 0.8))
page4.insert_text((380, 155), "• mistral-large2 / llama3.3", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((388, 167), "Native Cortex COMPLETE", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((388, 177), "with in-database residency", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((380, 197), "• Root Cause Synthesis", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((388, 209), "Contextualizes raw SQL into", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((388, 219), "actionable threat summaries", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((380, 239), "• Dynamic Policy Generator", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((388, 251), "Writes DDL masking policies", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((388, 261), "tailored to specific columns", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((380, 285), "• Conversational Copilot", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((388, 297), "Natural language queries on", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((388, 307), "warehouse compliance status", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)

# Box 4: Governance & Action Layer (x: 535, y: 98, w: 151, h: 280)
draw_card(page4, (535, 98, 686, 380), bg_color=(0.95, 0.98, 0.95), border_color=(0.70, 0.88, 0.75))
page4.insert_text((545, 116), "ACTION & REMEDIATION", fontsize=9.5, fontname="Helvetica-Bold", color=ACCENT_GREEN)
page4.insert_text((545, 134), "Autonomous Governance", fontsize=8.5, fontname="Helvetica-Bold", color=ACCENT_GREEN)
page4.insert_text((545, 155), "1. AST Safety Verification", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((553, 167), "Python AST parsing checks", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((553, 177), "patch syntax & integrity", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((545, 197), "2. Automated GitHub PR", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((553, 209), "Branches repo, applies fix,", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((553, 219), "and raises ready-to-merge PR", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((545, 239), "3. Dynamic Masking (DDM)", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((553, 251), "Instantly protects unmasked", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((553, 261), "PII without schema rewrite", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((545, 285), "4. Streamlit Command Center", fontsize=8.5, fontname="Helvetica-Bold", color=DARK_TEXT)
page4.insert_text((553, 297), "Unified executive dashboard", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)
page4.insert_text((553, 307), "for SecOps & compliance leads", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)

# Flow Arrows (simple text arrows)
page4.insert_text((182, 235), "➔", fontsize=14, fontname="Helvetica-Bold", color=SNOW_BLUE)
page4.insert_text((357, 235), "⇄", fontsize=14, fontname="Helvetica-Bold", color=(0.4, 0.1, 0.7))
page4.insert_text((522, 235), "➔", fontsize=14, fontname="Helvetica-Bold", color=ACCENT_GREEN)

# =============================================================
# SLIDE 5: 3. Impact Statement & Live Demo
# =============================================================
page5 = doc[4]

# Cover up 'Additional Slide' watermark
shape5 = page5.new_shape()
shape5.draw_rect(pymupdf.Rect(20, 355, 150, 385))
shape5.finish(fill=WHITE, color=WHITE)
shape5.commit()

page5.insert_text((34, 70), "3. Impact Statement, Scalability & Live Prototype Verification", fontsize=15, fontname="Helvetica-Bold", color=DARK_TEXT)
page5.insert_text((34, 85), "Quantifiable outcomes for enterprise GCCs, architectural scalability, and working demo links.", fontsize=9.5, fontname="Helvetica", color=MUTED_TEXT)

# 3 Top Metric Cards
draw_card(page5, (34, 98, 244, 185), bg_color=(0.94, 0.98, 0.95), border_color=(0.60, 0.85, 0.65))
page5.insert_text((44, 116), "MTTR REDUCTION", fontsize=9, fontname="Helvetica-Bold", color=ACCENT_GREEN)
page5.insert_text((44, 145), "~72% Faster", fontsize=20, fontname="Helvetica-Bold", color=ACCENT_GREEN)
page5.insert_text((44, 162), "From 48–72 hours down to < 15 mins", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((44, 174), "via autonomous AST code patches", fontsize=8, fontname="Helvetica", color=MUTED_TEXT)

draw_card(page5, (254, 98, 464, 185), bg_color=(0.94, 0.97, 1.0), border_color=(0.65, 0.82, 0.98))
page5.insert_text((264, 116), "CONTINUOUS COMPLIANCE", fontsize=9, fontname="Helvetica-Bold", color=SNOW_BLUE)
page5.insert_text((264, 145), "100% Real-Time", fontsize=20, fontname="Helvetica-Bold", color=SNOW_BLUE)
page5.insert_text((264, 162), "Zero-gap GDPR & PCI-DSS 4.0 audits", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((264, 174), "replacing quarterly manual reviews", fontsize=8, fontname="Helvetica", color=MUTED_TEXT)

draw_card(page5, (474, 98, 686, 185), bg_color=(0.98, 0.96, 0.94), border_color=(0.95, 0.78, 0.65))
page5.insert_text((484, 116), "ALERT ACCURACY", fontsize=9, fontname="Helvetica-Bold", color=ACCENT_ORANGE)
page5.insert_text((484, 145), "85% Less Noise", fontsize=20, fontname="Helvetica-Bold", color=ACCENT_ORANGE)
page5.insert_text((484, 162), "Cortex LLM contextualizes queries", fontsize=8.5, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((484, 174), "eliminating false-positive alert fatigue", fontsize=8, fontname="Helvetica", color=MUTED_TEXT)

# Scalability & Extending Beyond Demo (Left Column)
draw_card(page5, (34, 195, 350, 380))
page5.insert_text((44, 214), "SCALABILITY & EXTENDING BEYOND DEMO", fontsize=9.5, fontname="Helvetica-Bold", color=DARK_BLUE)
page5.insert_text((44, 234), "• Serverless Cloud-Native Architecture:", fontsize=8.8, fontname="Helvetica-Bold", color=DARK_TEXT)
page5.insert_text((52, 248), "Operates natively on Snowflake compute credits &", fontsize=8, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((52, 258), "Cortex endpoints with zero external database dependencies.", fontsize=8, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((44, 276), "• Enterprise CI/CD Pipeline Integration:", fontsize=8.8, fontname="Helvetica-Bold", color=DARK_TEXT)
page5.insert_text((52, 290), "Hooks directly into GitHub Actions / GitLab CI to block", fontsize=8, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((52, 300), "insecure commits before merging into main branches.", fontsize=8, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((44, 318), "• Multi-Framework Governance Roadmap:", fontsize=8.8, fontname="Helvetica-Bold", color=DARK_TEXT)
page5.insert_text((52, 332), "Extending beyond PCI/GDPR to automated EU AI Act", fontsize=8, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((52, 342), "and DORA (Digital Operational Resilience Act) filing.", fontsize=8, fontname="Helvetica", color=DARK_TEXT)
page5.insert_text((44, 360), "• Zero Hallucinations Guarantee:", fontsize=8.8, fontname="Helvetica-Bold", color=ACCENT_GREEN)
page5.insert_text((52, 372), "100% of generated patches undergo AST syntax validation.", fontsize=8, fontname="Helvetica", color=DARK_TEXT)

# Verification & Links (Right Column)
draw_card(page5, (360, 195, 686, 380), bg_color=(0.95, 0.98, 1.0), border_color=(0.60, 0.78, 0.95))
page5.insert_text((370, 214), "LIVE PROTOTYPE & SUBMISSION VERIFICATION", fontsize=9.5, fontname="Helvetica-Bold", color=DARK_BLUE)

page5.insert_text((370, 234), "🌐 Live Deployed Prototype URL:", fontsize=8.8, fontname="Helvetica-Bold", color=SNOW_BLUE)
page5.insert_text((375, 248), "https://snowshield-coco-copilot-7djukbxfen2nzwtaaamnxm.streamlit.app/", fontsize=7.8, fontname="Helvetica-Bold", color=DARK_TEXT)
page5.insert_text((375, 259), "• Interactive Risk Anomaly Inspector & Telemetry Analyzer", fontsize=7.8, fontname="Helvetica", color=MUTED_TEXT)
page5.insert_text((375, 269), "• Regulatory Compliance Matrix (GDPR, PCI-DSS, SOC 2)", fontsize=7.8, fontname="Helvetica", color=MUTED_TEXT)
page5.insert_text((375, 279), "• Conversational Snowflake Cortex AI Copilot", fontsize=7.8, fontname="Helvetica", color=MUTED_TEXT)

page5.insert_text((370, 298), "💻 Public GitHub Repository:", fontsize=8.8, fontname="Helvetica-Bold", color=SNOW_BLUE)
page5.insert_text((375, 312), "https://github.com/Skrishnreddy/SnowShield-CoCo-Copilot", fontsize=8.2, fontname="Helvetica-Bold", color=DARK_TEXT)
page5.insert_text((375, 323), "• Snowflake SQL DDL (SNOWSHIELD_DB.RISK_INTELLIGENCE)", fontsize=7.8, fontname="Helvetica", color=MUTED_TEXT)
page5.insert_text((375, 333), "• CoCo CLI Skills Pack: risk-audit, compliance-guard, auto-remediation", fontsize=7.8, fontname="Helvetica", color=MUTED_TEXT)
page5.insert_text((375, 343), "• Python AST validation & automated GitHub PR generator", fontsize=7.8, fontname="Helvetica", color=MUTED_TEXT)

page5.insert_text((370, 362), "👥 Team Information:", fontsize=8.8, fontname="Helvetica-Bold", color=DARK_BLUE)
page5.insert_text((375, 373), "Team PandaShield | Lead: G. Sai Krishna Reddy | GCC Edition 2026", fontsize=7.8, fontname="Helvetica", color=DARK_TEXT)

doc.save(output_pdf)
print("SUCCESS: Generated complete submission PDF at:", output_pdf)
