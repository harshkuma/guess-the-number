import random
import time

print("Hi, I'm Nisha\nI'm thinking a number\nGuess the number I am thinking")
print("!!!Note: Each time you enter the wrong guess I'll change my number!!!")
print()
time.sleep(5)

while True:
    try:
        element = random.randint(0,10)

        print("!!!Type 'exit' for exit!!!")
        guess = input("Enter number between 0-10: ")
        

        if guess.lower() == "exit":
            print()
            print("I hope you enjoy the game.")
            break

        elif element == int(guess):
            print("You guessed it right")
            print()

        elif int(guess)>10:
            print("Number cannot be greater than 10")
            print()

        elif int(guess)<0:
            print("Number cannot be smaller than 0")
            print()

        else:
            print("Guess again")
            print()

    except ValueError as error:
        print(error)
        print()