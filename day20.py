#output fibonacci sequence (base 1) on each keypress

num1 , num2 = 1, 1

while True:
    print(f"Current Fibonacci: {num1}")
    input("Enter The number fibonacci: ")

    num1 , num2 = num2, num1 + num2
    
