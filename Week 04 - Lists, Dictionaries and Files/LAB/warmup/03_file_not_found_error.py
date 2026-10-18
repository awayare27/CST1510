# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

try:
    with open("records.txt", "r") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print("Error: The file 'records.txt' could not be found.")

