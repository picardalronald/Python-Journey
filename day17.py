#print out unique characters from a string using built-in array-unique function or it's equivalent
lang = "PPYTHOONN"
#unique characters and organized in an ordered     
unique = "".join(dict.fromkeys(lang))

print(unique)
