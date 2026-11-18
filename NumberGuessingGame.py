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
            print(f"------Congratulations! You Guessed it Right! Your Score is {score} ------\n")
            break
    else:
        print("------You Ran Out of Chances-------")
        
while True:
    players = int(input("1. Let Computer Guess \n2. Let Another Person Guess \n3. Exit\nChoose 1 / 2 / 3: "))
    if players==1:
        randomNumber = random.randint(1,100)
        GuessNumber(randomNumber)
    elif players==2:
        print("------Enter Number you Guess (Between 1-100) below ------")
        secure = random.randint(1,5)
        for i in range(secure):
            print(random.randint(1,100))
        randomNumber = int(input())
        for i in range(secure):
                    print(random.randint(1,100))
        score = int(input("Enter Number of Chances: "))
        GuessNumber(randomNumber,score)
    elif players==3:
        print("------EXITING------")
        break
    else:
        print("------Invalid Option, Please Try again------")