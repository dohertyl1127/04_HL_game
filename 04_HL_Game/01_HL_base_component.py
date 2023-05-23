import math
import random


# functions go here
def int_check(question, low=None, high=None):
    situation = ""
    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))
            # checks int is not too low or high if lower and upper bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"please enter a number between {low} and {high}")
                    continue
            # checks int is not too low
            elif situation == "low only":
                if response < low:
                    print(f"please enter a number between {low} and {high}")
                    continue

            return response

        except ValueError:
            print("please choose an integer")
            continue


def statement_gen(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def yes_no(question):
    while True:

        # ask user if they have played before
        response = input(question).lower()

        # if yes continue code
        if response == "yes" or response == "y":
            return "yes"
        # if no display instructions
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please choose yes/no")


def instructions():
    print("**** higher low instructions: ****")
    print("FIRST USER:")
    print("choose your range of numbers to guess from.")
    print("choose a secret number that the second user will have to guess")
    print()
    print("SECOND USER:")
    print("guess a  number within the selected range to try to find the secret number")
    print("if you dont find the number you will lose and if you do find the number you win")
    print("Have fun!")

    return ""

# main routine goes here


# print statement
statement_gen("Welcome to higher lower", "=")

played_before = yes_no("have you played before? ")

if played_before == "no":
    instructions()

game_end = ""
while game_end == "":

    # lists
    already_guessed = []

    # define low and high
    print()
    low_num = int_check("lowest number? ", 1)
    high_num = int_check("Highest number? ", low_num)

    # allow number of guesses

    RANGE = high_num - low_num + 1
    max_raw = math.log2(RANGE)
    max_upped = math.ceil(max_raw)
    guesses_allowed = max_upped + 1
    guesses_left = guesses_allowed
    print(f"Max guesses: {guesses_allowed}")

    print()
    # find secret number
    secret = int_check("secret number? ", low_num, high_num)
    print(secret)
    print()

    guess = ""
    while guess != secret and guesses_left >= 1:

        guess = int_check("Guess: ", low_num, high_num)

        if guess in already_guessed:
            print(f"You have already guessed that number! please guess again, you have {guesses_left} guesses left")
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left >= 1:

            if guess < secret:
                print(f"Guess too low, try a higher number. Guesses left: {guesses_left}")

            elif guess > secret:
                print(f"Guess too high, try a lower number. Guesses left : {guesses_left}")

        elif guesses_left < 1:
            if guess < secret:
                print("Too low! Sorry but you didn't get the number")

            elif guess > secret:
                print("Too high! Sorry but you didn't get the number")

    if guess == secret:
        if guesses_left == guesses_allowed:
            print(f"Amazing! You got it in {guesses_allowed}")

        else:
            print(f"Well done! you got it in {guesses_allowed - guesses_left}")
    print()
    game_end = input("press <enter> to play again or xxx to exit")
print()
print("Thank you for playing higher lower game")
