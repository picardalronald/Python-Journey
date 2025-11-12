# Censor the word fuck and dead with constant length asterisk

fuck = "fuck"
dead = "dead"

hiddenF = "*" * len(fuck)
hiddenD = "*" * len(dead)


while True:
  print("Check if your word is bad or not\n")
  user = input("Enter Word: ").lower()

  if user == fuck:
     print(f"your word is bad for everyone! ({hiddenF})")
     
  elif user == dead:
      print(f"your word is bad for everyone! ({hiddenD})")
      
  else:
    print(f"Your word is not bad Congrats ({user})")