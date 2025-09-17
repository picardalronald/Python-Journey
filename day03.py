#Number Guessing Game

import random

ran_num = random.randint(1,20)

print("WelCome to my Game 'Number Guessing'")

attempts = 5

while attempts > 0:
   guess = int(input("Guess the number 1-20: "))
   attempts -=1

   if guess < ran_num:
      print("Too low try again!")
   elif guess > ran_num:
     print("Too high Try again")
   else:
      print("🎉 Correct! You guessed the number.")
      print(f"You have Last {attempts} attempts.")
      break
