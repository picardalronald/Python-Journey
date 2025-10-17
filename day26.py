# Create functions: subtract(x,y), divide(x,y), multiple(x,y)
def sub(x,y):
  
  sum = x - y
  return sum

def div(x,y):
  
  sum = x / y
  return sum

def multi(x,y):
  sum = x * y 
  return sum

while True:
    x = int(input("Enter First number: "))
    y = int(input("Enter Secopnd number: "))
    ope = input("Enter Operators Subtract/Divide/Multiple: ")

    match ope:
        case '-':
         print(sub(x,y))

        case '/':
         print(div(x,y))

        case '*':
         print(multi(x,y))
         
        case _:
            print("Invalid input operators!")
            break
