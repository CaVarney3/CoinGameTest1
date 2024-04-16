import random

def coin_flip():
    number = int(input("How many times would you like to flip the Coin: "))
    heads = []
    tails = []
    recordlist = []

    for amount in range(number):
        flip = random.randint(0, 1)
        if flip == 1:
            print("You flipped the Coin and it landed on Heads!")
            recordlist.append("Heads")
        else:
            print("You flipped the coin and it landed on Tails!")
            recordlist.append("Tails")

    print(str(recordlist))
    print("Heads:", recordlist.count("Heads"))
    print("Tails:", recordlist.count("Tails"))

coin_flip()

