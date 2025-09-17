# Simple Grading System
while True:
    grade = float(input("Enter Your Grade: "))

    if grade > 100 or grade < 0:
        print("Invalid grade, please try again.")
    elif grade >= 95:
        print("Excellent")
    elif grade >= 90:
        print("You are in the top class")
    elif grade >= 85:
        print("You are in the middle class")
    elif grade >= 75:
        print("You are in the lower class")
    else:
        print("You did not pass")
        break
