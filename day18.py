#Ask for a input, print out the unique characters on that input

#Continue the executing
while True:
    user  = input("Input the words: ")
    #unique char and in an oredered 
    unique = "".join(dict.fromkeys(user.upper()))

    print(unique)
