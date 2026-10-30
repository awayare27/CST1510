"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  :  Cyber 
Date  : 08/26/2026
Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

class Record:
    over_limit_count = 0  # Class-level running total for security violations

    def __init__(self, label, value, limit):
        self.label = label
        self.value = float(value)  
        self.limit = float(limit)  
        
        if self.value >= self.limit:
            Record.over_limit_count += 1

    def status(self):
        #Evaluate metric against security threshold and return threat status.
        percentage = (self.value / self.limit) * 100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
with open("security_metrics.txt", "w") as f:
    f.write("Awa_Fall,120,100\n")
    f.write("john_Her,95,100\n")
    f.write("Diange_Moh,45,100\n")

def load_records(path):
    records = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                label, value, limit = line.split(",")
                records.append(Record(label, float(value), float(limit)))
    return records

records = load_records("security_metrics.txt")

# Initialize the running count variable properly
over_limit_total = 0


# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # Security metric report lines
    print(f" Current Metric Value : {record.value}")
    print(f" Safety Threshold     : {record.limit}")
    print(f" Threat Status        : {record.status()}")

    print("=" * 34)

    # Check status and accumulate violations inside the loop
    if record.status() == "OVER LIMIT":
        over_limit_total += 1

# Print the final summary once after the loop
print()
print(f"[ALERT SUMMARY] Total metrics breaching safe limits: {over_limit_total} out of {len(records)}")    

# ==========================================================================

