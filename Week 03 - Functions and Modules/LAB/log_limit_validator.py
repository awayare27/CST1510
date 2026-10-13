"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  :  Cyber 
Date  :11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def status_of(percent):    #Return the status based on the given percentage.

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):      #Calculate and return the difference and percentage.       
   
    difference = value - limit
    percent = (value / limit) * 100 
    return difference, percent

def print_report(label, value, limit, difference, percent, status):  #Print the complete formatted report.
    #Print the complete formatted report.
    print(f"{label}  Value: {value}, Limit: {limit}  Difference: {difference}  Percent: {percent:}%  Status: {status}")

# ==================================================================== INPUT

while True:
    label = input("Enter label (or 'quit' to stop): ")
    if label.lower() == "quit":
        break
        
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))

# ================================================================== PROCESS

difference, percent = check(value, limit)
status = status_of(percent)

over_limit_count = 0      
if status == "OVER LIMIT":
        over_limit_count += 1

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
    
print_report(label, value, limit, difference, percent, status)
    
print("=" * 34)

print(f"Total OVER LIMIT: {over_limit_count}")

# ==========================================================================

