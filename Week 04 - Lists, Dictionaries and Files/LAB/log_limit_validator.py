"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  :Cyber
Date  : 10/16/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def status_of(percent):    # Return the status based on the given percentage threshold.
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check_record(value, limit):
    difference = value - limit 
    percent = (value / limit) * 100
    status = status_of(percent) 
    return difference, percent,status

def print_report(label, value, limit, difference, percent, status):
     print(f"User/IP: {label}\n  Failed Attempts: {value}\n Threshold: {limit}\n  Difference: {difference}\n  Percent: {percent:.1f}%\n  Status: {status}\n")

# ====================================================================== STORE
# ====================================================================== STORE
def load_records(path):
    """Load login records from a file (label,value,limit) and return a list of dicts."""
    records_list = []
    try:
        with open(path, "r") as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records_list.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
    except FileNotFoundError:
        print(f"Error: Security log file '{path}' not found.")
    return records_list

# Automatically create a sample login log file for testing if it doesn't exist
with open("login_logs.txt", "w") as f:
    f.write("admin_IP,120,100\n")
    f.write("user_john,95,100\n")
    f.write("guest_node,45,100\n")

# Load records using the function
records = load_records("login_logs.txt")


# =============================================================== PROCESS + OUTPUT
over_limit_count = 0
results_output = []

print("=" * 35)
print("     LOGIN SECURITY VALIDATOR REPORT")
print("=" * 35)
print()

# Loop over each record, check thresholds, and print report
for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]
    
    difference, percent, status = check_record(value, limit)
    print_report(label, value, limit, difference, percent, status)
    
    # Keep running count of OVER LIMIT breaches
    if status == "OVER LIMIT":
        over_limit_count += 1
        
    # Collect data to write out to a new file (label,status)
    results_output.append(f"{label},{status}\n")

# Print final summary of breaches
print("=" * 35)
print(f"Total OVER LIMIT Breaches: {over_limit_count} of {len(records)}")
print("=" * 35)

# Write results out to a new file (Excellent criteria)
with open("security_results.txt", "w") as res_file:
    res_file.writelines(results_output)

# ==========================================================================

