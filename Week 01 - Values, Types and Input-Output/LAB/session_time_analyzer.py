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
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
address_IT = input("Enter  your IT address: ")

#    - the second is a NUMBER (use float(), not int())
login_time = float(input("Enter your login time: "))

#    - the third  is a NUMBER (use float(), not int())
total_time = float(input("Enter total time: "))
#
#    Remember: input() always gives back text.

label = ""      # : replace with an input() call
first = 0.0     # : replace with an input() call, converted
second = 0.0    # : replace with an input() call, converted

label = address_IT
first = login_time
second = total_time

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = (second - first)  
percent =  (first / second) * 100     


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

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

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
