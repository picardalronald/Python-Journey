#output a number, and wait for a keypress, then increment the number and print it out, then repeat

#starting number
number = 0

while True:
  #Ask for increment the number
    print(f"Current number: {number}")
    user =  input("Press Enter to increment: ")

    number +=1
