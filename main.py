# Second Engeto project Bulls and Cows

import random


def welcome() -> None:
    print("Hi there!")
    separator()
    print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    separator()


def generate_number() -> int:
    number = [random.randint(1, 9)]
    for i in range(3):
        number.append(random.randint(0, 9))
        while number[-1] in number[:-1]:
            number[-1] = random.randint(0, 9)
    return number


def make_a_guess() -> int: #!!!!!! ohlídat stejná čísla
    while True:
        guess = input('Enter a number: ')
        if not guess.isnumeric():
            print("Only numbers are allowed")
            continue
        elif len(guess) != 4:
            print("Number must be 4 digit long")
            continue
        elif guess[0] == str(0):
            print("Number cannot start with zero")
            continue
        else:
            guess = num_to_list(int(guess))
            break
    return guess


def separator() -> None:
    print('-' * 47)


def num_to_list(number: int) -> (list, int):
    return [int(x) for x in str(number)]


def list_to_num(number: (list, int)) -> int:
    return int("".join([str(x) for x in number]))


def evaluate_guess(number: int, guess: int) -> int:
    bulls = 0
    cows = 0
    #!!!!!!!
    return bulls, cows


def print_evaluation(bulls: int, cows:int,  guesses:int) -> None:
    # !!!!!!!
    print(" ")


def goodbye(guess: int) -> None:
    if guess <= 3:
        message = "amazing"
    elif guess <= 6:
        message = "average"
    elif guess <= 8:
        message = "not so good"
    else:
        message = "terrible"
    print(f"That's {message}")


def main():
    welcome()
    guesses = 0
    number = generate_number()
    print(number)
    while number != guess:
        guess = make_a_guess()
        guesses += 1
        print(guess)
        bulls, cows = evaluate_guess(number, guess)
        print_evaluation(bulls, cows, guesses)
    goodbye(guess)


if __name__ == '__main__':
    main()
