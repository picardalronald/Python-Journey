# (formerly day18) print out unique characters and their count on a string

#Continue the executing
while True:
    user  = input("Input the words: ")
    #unique char and in an oredered 
    unique = "".join(dict.fromkeys(user.upper()))

    count = len(user)

    print(f"Count String input: {count}")
    print(f"Unique Characters: {unique}")
