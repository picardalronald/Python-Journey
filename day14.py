#split a name string into a char-array, then capitalize the first letter by overwriting char-array item zero, then reconstruct into a string
name = "ronald"

chars  = list(name)

chars = name.upper()

capitalized = "".join(chars)

print("Original: " + name )
print("Capitalized Version: " + capitalized)
