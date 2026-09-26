import snowflake.connector
import os

account = "cbc79236.us-east-1"
user = "SAIKRISHNA"
password = "S37uxB5LKABxFR3"
warehouse = "COMPUTE_WH"
database = "SNOWSHIELD_DB"
schema = "RISK_INTELLIGENCE"

print(f"Connecting to Snowflake {account}...")
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)
cs = conn.cursor()

# 1. Create a stage for Streamlit assets
print("Creating internal stage for Streamlit...")
cs.execute("CREATE STAGE IF NOT EXISTS STREAMLIT_STAGE DIRECTORY = (ENABLE = TRUE)")

# 2. Upload streamlit_app.py, cortex_copilot.py, and snowflake_logo.png
files_to_upload = [
    "/Users/gsaikrishnareddy/pandashield-v2/Snowflake/streamlit_app.py",
    "/Users/gsaikrishnareddy/pandashield-v2/Snowflake/cortex_copilot.py",
    "/Users/gsaikrishnareddy/pandashield-v2/Snowflake/snowflake_logo.png"
]

for f in files_to_upload:
    print(f"Uploading {os.path.basename(f)} to @STREAMLIT_STAGE...")
    put_sql = f"PUT file://{f} @STREAMLIT_STAGE AUTO_COMPRESS=FALSE OVERWRITE=TRUE"
    cs.execute(put_sql)
    res = cs.fetchone()
    print(" ->", res)

# 3. Create or replace Streamlit app in Snowflake
print("Creating Streamlit in Snowflake (SiS) object...")
create_streamlit_sql = """
CREATE OR REPLACE STREAMLIT SNOWSHIELD_COPILOT
ROOT_LOCATION = '@SNOWSHIELD_DB.RISK_INTELLIGENCE.STREAMLIT_STAGE'
MAIN_FILE = '/streamlit_app.py'
QUERY_WAREHOUSE = 'COMPUTE_WH'
TITLE = 'SnowShield: Risk & Regulatory Copilot';
"""
cs.execute(create_streamlit_sql)
print(" ->", cs.fetchone())

# 4. Describe Streamlit app to get details
cs.execute("SHOW STREAMLITS")
streamlits = cs.fetchall()
print("\nStreamlit apps in schema:")
for s in streamlits:
    print(" - Name:", s[1], "| URL:", s[7] if len(s) > 7 else "N/A")

cs.close()
conn.close()
print("\nDEPLOYMENT OF STREAMLIT IN SNOWFLAKE (SiS) COMPLETE!")
