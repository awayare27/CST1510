"""
RECORD CHECK  -  my version
===========================

Name  :Awa Yare Fall
Lane  :  Cyber 
Date  :11/8/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

#Create a CSV file
data =pd.DataFrame({
    "Server ID": ["SRV-Auth-01", "SRV-Web-02", "SRV-DB-03", "SRV-API-04", "SRV-Mail-05"],
    "Failed login attempts": [120, 94, 45, 105, 82], 
    "Max allowed failed attempt": [100, 100, 100, 100, 100] 
}) 

data.to_csv("server_login_logs.csv",index=False)

# Read data from the CSV file
data=pd.read_csv("server_login_logs.csv")

# ================================================================= PROCESS
#Add a "percent" column and a categorized "status" security column

data["percent"] = (data["Failed login attempts"] / data["Max allowed failed attempt"]) * 100

# Lambda function to triage security risks
data["status"] = data["percent"].apply(
    lambda x: "OVER allowed failed attempts" if x >= 100 else ("WARNING" if x >= 90 else "OK")
)


# ================================================================== OUTPUT

print("=== FULL SERVER LOGS ===")
print(data)
print("\n" + "="*40 + "\n")

# Filter to show only the rows that require security attention (not "OK")

print("=== SECURITY ALERTS & WARNINGS ===")
security_alerts = data[data["status"] != "OK"]
print(security_alerts)
print("\n" + "="*40 + "\n")

# Group by status to get threat counts per category
print("=== THREAT LEVEL SUMMARY ===")
grouped = data.groupby("status")
print(data["status"].value_counts())

# Save the full processed DataFrame to a new incident report CSV
data.to_csv("security_incidents.csv", index=False)

print(f"Full report saved to :{"security_incidents.csv"}")

# Generate and save a bar chart of the threat counts

data["status"].value_counts().plot(kind="bar", title="Server Security Status Counts")
plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()
print("[+] Bar chart saved to 'status_counts.png'")
# ==========================================================================

