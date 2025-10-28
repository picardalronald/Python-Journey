# print out current date/time
from datetime import datetime 


curdate = datetime.today()


print(curdate.strftime("%B %d, %Y"))
print(curdate.strftime("%I:%M %S %p"))
