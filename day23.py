#Ask for a string input for numbers 1 to 10 in words (e.g. one, two...) then output it's translation in tagalog


num = {

   "one": "isa",
   "two": "dalawa",
   "three": "tatlo",
   "four": "apat",
   "five": "lima",
   "six": "anim",
   "seven": "pito",
   "eight": "walo",
   "nine": "siyam",
   "ten": "sampo",

}

user = input("input for numbers 1 to 10 in words: ").lower()

if user in num:
    print(f"The Tagalog translation of '{user}' is '{num[user]}'.")
else:
    print("Invalid input! Please enter a word from 'one' to 'ten'.")

