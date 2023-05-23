import math

for item in range(0, 4):

    low = int(input("low: "))
    high = int(input("High: "))

    range = high - low + 1
    max_raw = math.log2(range)
    max_upped = math.cell(max_raw)
    max_guesses = max_upped +1
    print(f"Max guesses: {max_guesses}")

    print()