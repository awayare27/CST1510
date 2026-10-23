"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  :   Cyber
Date  :10/02/2026

Run it:   python template.py

# ==================================================================== INPUT


address_IT = input("Enter  your IT address: ")
login_time = float(input("Enter your login time: "))
total_time = float(input("Enter total time: "))


label = address_IT
first = login_time
second = total_time

# ================================================================== PROCESS

difference = (second - first)  
percent =  (first / second) * 100     

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)



print (f" Your IT address: {label}")
print (f" Your login time: {first}")
print (f" Your total time: {second}")

print (f"The difference of time is: {difference:>+10.2f}")
print (f" The percentage is: {percent:>10.2f}%")
print(" Status          : Session verified successfully.") 

print("=" * 34)



