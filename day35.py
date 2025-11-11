# ask for a year input and output if it's a leap year or not using built in functions if possible
year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"it is a leap year {year}")
else:
    print(f"it is not leap year {year}")

