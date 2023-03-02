# 230302
import random as rd
import art

RANDOM_NUMBER = rd.randrange(1, 100)


def game(life):
    global RANDOM_NUMBER
    print(f"You have {life} attempts remaining to guess the number.")
    answer = int(input("Make a guess : "))
    if answer > RANDOM_NUMBER:
        return 2
    elif answer < RANDOM_NUMBER:
        return 1
    else:
        return 0


def start_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    life = 0
    level_choice = True
    while level_choice:
        level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
        if level == "hard":
            life = 5
            level_choice = False
        elif level == "easy":
            life = 10
            level_choice = False
        else:
            print("you entered worng value.")
            level_choice = True
    for i in range(life, 0, -1):
        result = game(i)
        if result == 2:
            print("Too high")
        elif result == 1:
            print("Too low")
        else:
            break
        print("Guess again")
        life = i - 1

    print(f"Random number is {RANDOM_NUMBER}")
    if life != 0:
        print("You win")
    else:
        print("You lose")


start_game()
