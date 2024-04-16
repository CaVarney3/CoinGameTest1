import random
# The Coin Flip itself and the Choices
def coin_flip():
# Variables
  number= input("How many times would you like to flip the Coin: ")
  heads=[]
  tails=[]
  recordlist=[]
# Coin Flip Generation  
  for amount in range(number):
    flip = random.randint(0,1)
    if (flip == 1):
      print("You flipped the Coin and it landed on Heads!"
      recordlist.append("Heads")
    Else:
      print("You flipped the coin and it landed on Tails!"
      recordlist.append("Tails")
# Recording Coin Flip stats
  print(str(recordList))
  print(str(recordList.count("Heads")) + str(recordList.count("Tails")))




