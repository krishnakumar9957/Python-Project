from lists_of_any_project_and_arts import logo
import random
HARD_LEVEL_TURN = 5
EASY_LEVEL_TURN = 10

def check_condion(guess ,answer,turns):
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low ")
        return turns-1
    else:
        print(f"you got it ,The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty . Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print(logo)
    print("welcome to the guess number game!")
    print("I am guessing the number between 1 to 100")
    answer = random.randint(1,100)
    print(f"the correct answer is {answer}")



    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")



        guess = input("enter your number ")

        turns = check_condion(guess,answer,turns)


        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()