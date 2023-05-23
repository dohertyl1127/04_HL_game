
secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >=1:

    guess = int(input("Guess: "))

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

    else:
        if guess < secret:
            print("Too low!")

        elif guess > secret:
            print("Too high!")

if guess == secret:
    if guesses_left == guesses_allowed:
        print(f"Amazing! You got it in {guesses_allowed}")

    else:
        print(f"Well done! you got it in {guesses_allowed}")
