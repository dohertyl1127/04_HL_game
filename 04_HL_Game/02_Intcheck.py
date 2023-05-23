# int_check function
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


# Main routine
lowest = int_check("low number: ")
highest = int_check("High number: ", lowest + 1)
rounds = int_check("Rounds: ", 1)
guess = int_check("Guess: ", lowest, highest)
print(lowest)
print(highest)