# Create a function roll() that generates 2 numbers between 1 to 6
import random

def roll():
    rannumb = random.randint(1,6)
    rannumb1 = random.randint(1,6)
    return rannumb1, rannumb
    
print(roll())
