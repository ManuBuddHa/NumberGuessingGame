import random
try:
    players = int(input("1. Let Computer Guess \n2. Let Another Person Guess\nChoose 1 or 2 : "))
    if players==1:
        randomNumber = random.randint(1,100)
        score = 10
        while True:
            userInput=int(input("Guess : "))
            if userInput<randomNumber:
                print("Your Guess is Lower, Try Again")
                score-=1
            elif userInput>randomNumber:
                print("Your Guess is Higher, Try again")
                score-=1
            else:
                print(f"Congratulations! You Guessed it Right! Your Score is {score}")
                break
    elif players==2:
        randomNumber = int(input("Enter Number you Guess: "))
        score = 10
        while True:
            userInput=int(input("Guess : "))
            if userInput<randomNumber:
                print("Your Guess is Lower, Try Again")
                score-=1
            elif userInput>randomNumber:
                print("Your Guess is Higher, Try again")
                score-=1
            else:
                print(f"Congratulations! You Guessed it Right! Your Score is {score}")
                break
except ValueError:
    print("Invalid Input")