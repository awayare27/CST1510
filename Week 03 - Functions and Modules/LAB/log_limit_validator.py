"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  :  Cyber 
Date  :11/10/2026



<<<<<<< HEAD
=======
# =================================================================== FUNCTIONS

>>>>>>> e30e108b88d78c0993f9cb951dd55227101bc894
def status_of(percent):    # Return the status based on the given percentage threshold.
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):      # Calculate and return the difference and percentage of failed logins vs threshold.      
    
    difference = value - limit 
    percent = (value / limit) * 100 
    return difference, percent

def print_report(label, value, limit, difference, percent, status):  # Print the complete formatted security report.
    
    print(f"User/IP: {label}\n  Failed Attempts: {value}\n Threshold: {limit}\n  Difference: {difference}\n  Percent: {percent:.1f}%\n  Status: {status}\n")

# ==================================================================== INPUT

while True:
    label = input("Enter username or IP (or 'quit' to stop): ")
    if label.lower() == "quit":
        break
        
    # Prompt user for failed attempts 
    value = float(input("Enter failed login attempts: "))
    # Prompt user for maximum allowed failed limit 
    limit = float(input("Enter maximum allowed failed limit: "))

    # ================================================================== PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)

    over_limit_count = 0      
    if status == "OVER LIMIT":
        over_limit_count += 1

    # =================================================================== OUTPUT

    print()
    
    print("=" * 34)
    print(f"  LOGIN SECURITY CHECK  -  {label}")
    print("=" * 34)
        
    print_report(label, value, limit, difference, percent, status)
        
    print("=" * 34)

    # Print the total count of security breaches triggered
    print(f"Total OVER LIMIT Breaches: {over_limit_count}")
    print() 
<<<<<<< HEAD
=======

# ==========================================================================

# ==========================================================================
>>>>>>> e30e108b88d78c0993f9cb951dd55227101bc894

# ==========================================================================