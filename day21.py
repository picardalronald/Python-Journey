#Ask for a number input, print an error when it's not a number using if else
while True:
        user = input("Enter a number: ")

       #accepting 1234514 num and so on
        if user.isdigit():
            print(f"Correct its a number: {user}")
        else:
            print(f"it is not a input number: {user}")
            break
