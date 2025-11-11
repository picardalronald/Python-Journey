# add 1 hour interval to current time and output (date/time manipulation [oop??])
from datetime import datetime, timedelta


class Time:
    
    def __init__(self):
        self.time = None
        self.date = None
        
    def currentTime(self):
      addIntervalTime = datetime.now();
      self.time = addIntervalTime + timedelta(hours=1)
      print(self.time.strftime("%I:%M %p"));
      
    def currentDate(self):
       self.date = datetime.today();
       print(self.date.strftime("%B %d %A %Y"))
      
        

r = Time()
r.currentTime()
r.currentDate()