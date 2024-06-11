import random
cont = ""
while cont != "no":
    nummer = random.randint(1,10)
    ans = -1
    guesses = 0
    while ans != nummer:
        ans = int(input("Guess a random number: "))
        if ans < nummer:
            print("higher")
        elif ans > nummer:
            print("lower")
        guesses += 1
    print("You guessed it!")
    cont = input("Want to play again?").lower()

