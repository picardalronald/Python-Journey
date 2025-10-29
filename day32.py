# print out current date; then print out current time; using 2 separate function call, but outputting on the same line

from datetime import datetime


def date():
    date = datetime.today()
    print(date.strftime('%B %d, %Y'))
    

def time():
    time = datetime.today()
    print(time.strftime('%I:%M %S %p'))\
        
        
date()
time()

