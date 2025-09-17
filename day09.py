#Guess the day today game practice python
from datetime import datetime

today = datetime.now()
weekdays = today.weekday() + 1

print("Guess the number of days today :D")

attempts = 5

while attempts > 0:
  day = int(input("Enter your number days [1-7]: "))
  attempts -=1
     
  match day:
        case 1:
            print("Today is: Monday")
        case 2:
            print("Today is: Tuesday")
        case 3:
            print("Today is: Wednesday")
        case 4:
            print("Today is: Thursday")
        case 5:
            print("Today is: Friday")
        case 6:
            print("Today is: Saturday")
        case 7:
            print("Today is: Sunday")
        case _:
            print("Invalid Days try again.")
            
 
  if day == weekdays:
      print(f"Your day is Match Today! Your Remaining attempts ({attempts})")
      break
  else:
     print(f"Your days is not match: Today is {today.strftime('%A')}, Remaining attempts {attempts} ")
     
                 
