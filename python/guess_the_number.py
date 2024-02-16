import random

r = random.randrange(1,20)
print("******************Guessing the number***************")
n = None
print("Guess the number between 1 to 20: ")
while (n!=r):
    n = int(input())
    if (n==r):
        print("WOW! You guess the correct number!!!")
        break
    elif(r <= 20 and r > 15):
         print("\nChoose a number between 16 and 20")
    elif(r > 10 and r <= 15):
        print("\nChoose a number between 11 and 15")
    elif(r <= 10 and r > 5):
        print("\nChoose a number between 6 and 10")
    elif(r <= 5 and r >= 1):
        print("\nChoose a number between 1 and 5")
    else:
        print('\nYou never know')
	
