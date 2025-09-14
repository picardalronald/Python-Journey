#Get the accurate date & time and day

from datetime import datetime


today = datetime.now()

print(today.strftime("Date Today is: %B %d, %Y"))
print(today.strftime("Day of the Week: %A"))
