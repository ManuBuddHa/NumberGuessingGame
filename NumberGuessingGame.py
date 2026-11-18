import random
def GuessNumber(randomNumber,score=10):
    while score>0:
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
    else:
        print("------You Ran Out of Chances-------")
try:
    players = int(input("1. Let Computer Guess \n2. Let Another Person Guess\nChoose 1 or 2 : "))
    if players==1:
        randomNumber = random.randint(1,100)
        GuessNumber(randomNumber)
    elif players==2:
        randomNumber = int(input("Enter Number you Guess (Between 1-100): "))
        score = int(input("Enter Number of Chances: "))
        GuessNumber(randomNumber,score)
    else:
        print("Invalid Option, Please Try again")
except ValueError:
    print("Invalid Input")