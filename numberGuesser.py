from random import randrange



correctAnswer = randrange(1,100)
guess = 0
numOfGuesses = 0
while guess != correctAnswer:
    guess = int(input("Pick a number 1-100\n"))
    if guess > 100:
        print("Guess was not within 1-100")
        guess = int(input("Pick a number 1-100\n"))
    elif guess > correctAnswer:
        print("Lower")
        numOfGuesses+=1
    elif guess < correctAnswer:
        print("Higher")
        numOfGuesses+=1
    else:
        print("You're correct")
        numOfGuesses+=1
        print("It took you " + str(numOfGuesses) + " guesses.")
        break