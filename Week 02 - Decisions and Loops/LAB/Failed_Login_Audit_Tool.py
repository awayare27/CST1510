"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  : Cyber
Date  : 10/04/26

Run it:   python template.py

Cyber scenario: label = hostname, value = failed logins seen,
limit = the lockout / alert threshold.
"""


    # ================================================================ INPUT
over_limit_count = 0          

while True:

    label = input("Enter Hostname (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Failed logins seen: "))
    limit = float(input("Lockout threshold: "))

    # ============================================================== PROCESS
    
    difference = value - limit
    percent = value / limit * 100    

    
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # ================================================================ OUTPUT
    
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Failed logins : {value:>14.2f}")
    print(f"  Threshold     : {limit:>14.2f}")
    print(f"  Difference    : {difference:>14.2f}")
    print(f"  Percent       : {percent:>13.2f}%")
    print(f"  Status        : {status:>14}")
    print("=" * 34)
    print()


print(f"Records OVER LIMIT: {over_limit_count}")