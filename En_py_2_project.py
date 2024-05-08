"""
projekt_2.py
discord: petulek
"""

import random


"""
Computer 4 digit number generation
First digit cannot be zero. 
Digits must be unique.
"""
def generate_secret_num():

    first_digit = random.randint(1, 9)  # První číslice nemůže být nula
    other_digits = random.sample(range(10), 3)
    unique_digits = [str(first_digit)] + [str(digit) for digit in other_digits if digit != first_digit]

    while len(unique_digits) != 4:
        remaining_digit = random.choice([digit for digit in range(10) if str(digit) not in unique_digits])
        unique_digits.append(str(remaining_digit))

    return ''.join(unique_digits)

"""
Count bulls and cows
"""
def check_guess(secret_num, guess):
    
    bulls = sum(s == g for s, g in zip(secret_num, guess))
    cows = sum(s in guess for s in secret_num) - bulls
    return bulls, cows

"""
Verification of 4 unique digits
"""
def is_valid_guess(guess):
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4 and guess[0] != '0'

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_num = generate_secret_num()
    guesses = 0

    while True:
        guess = input("Enter a number: ")

        if not is_valid_guess(guess):
            print("Invalid input. Please enter a 4-digit number with unique digits. First digit cannot be zero.")
            continue

        bulls, cows = check_guess(secret_num, guess)
        guesses += 1

        if bulls == 4:
            print("Correct, you've guessed the right number in {} guesses!".format(guesses))
            break
        else:
            print("{} bull{}, {} cow{}".format(bulls, 's' if bulls != 1 else '', cows, 's' if cows != 1 else ''))

if __name__ == "__main__":
    main()