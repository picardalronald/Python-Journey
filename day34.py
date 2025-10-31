# print out the current date time but with the specific format: Mon Jan 13 2025 14:54:30

from datetime import datetime 

current = datetime.today()

result = current.strftime('%A %b %d %Y %X')

print(result)