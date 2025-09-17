# Simple Calculator

fnum = input("Enter first number: ")
snum = input("Enter second number: ")
symbol = input("Choose operation (+, -, *, /): ")

# Convert inputs to integers
fnum = int(fnum)
snum = int(snum)

# Perform calculation
if symbol == "+":
    total = fnum + snum
elif symbol == "-":
    total = fnum - snum
elif symbol == "*":
    total = fnum * snum
elif symbol == "/":
    if snum == 0:
        print("Error: Cannot divide by zero!")
        total = None
    else:
        total = fnum / snum
else:
    print("Invalid operation!")
    total = None

# Show result only if valid
if total is not None:
    print("Result:", total)
