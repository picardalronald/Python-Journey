#Ask for a number input, throw an error if it's more than 100 or less than zero

while True:
    user = int(input("Enter the number Range(0-100): "))

    if user < 0 or user > 100:
        print(f"Error: {user} is out of range (0–100).")
        break
    else:
        print(f"Correct! {user} is within the range (0–100).")
