import random
randomNumber = random.randint(1,10)
score = 10
while True:
    userInput=int(input("Guess : "))
    if userInput==randomNumber:
        print(f"Congratulations! You Guessed it Right! Your Score is {score}")
        break
    else:
        print("Try Again!")
        score-=1