"""
RECORD CHECK  -  my version
===========================

Name  : Awa Yare Fall
Lane  :   Cyber
Date  :10/02/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ==================================================================== INPUT
<<<<<<< HEAD
# 1. Ask the user for your three values.
=======
>>>>>>> ec335120d474d80b212ef6ee064fc5fcefc14679

address_IT = input("Enter  your IT address: ")
login_time = float(input("Enter your login time: "))
total_time = float(input("Enter total time: "))
<<<<<<< HEAD

=======
>>>>>>> ec335120d474d80b212ef6ee064fc5fcefc14679

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

# : your report lines go here

print (f" Your IT address: {label}")
print (f" Your login time: {first}")
print (f" Your total time: {second}")

print (f"The difference of time is: {difference:>+10.2f}")
print (f" The percentage is: {percent:>10.2f}%")
print(" Status          : Session verified successfully.") 

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
