import random
n = random.randint(1, 7)
guess = int(input("Enter an integer from 1 to 7: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 7: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 7: "))
    else:
        print ("you guessed it!")
        break
    print


sample input 1 to 7:4
sample output you guessed it
