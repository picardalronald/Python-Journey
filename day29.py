# Create a function greatest(x,y,z) that returns which of the 3 given numbers are greater (using > or < signs)

def great(x,y,z):
    
    if x > y and x > z:
       print(f"x-({x}) is greatest number")
    elif z > x and z > y:
       print(f" z-({z}) is greatest number")
    elif y > x and y > z:
        print(f"y-({y}) is greatest number")
    else:
       print("All numbers are same!")
       

x = int(input("Enter the number of x: "))
y = int(input("Enter the number of y: "))
z = int(input("Enter the number of z: "))

print(f"what is the greatest number of 3 numbers input")
print(great(x,y,z))
