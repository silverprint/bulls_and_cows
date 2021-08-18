# Second Engeto project Bulls and Cows

import random


def welcome() -> None:
    print("Hi there!")
    separator()
    print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    separator()


def generate_number() -> (list, int):
    number = [random.randint(1, 9)]
    for i in range(3):
        number.append(random.randint(0, 9))
        while number[-1] in number[:-1]:
            number[-1] = random.randint(0, 9)
    return number


def make_a_guess() -> (list, int): #!!!!!! ohlídat stejná čísla
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


def evaluate_guess(number: (list, int), guess: (list, int)) -> dict:
    score = {"bulls": 0, "cows": 0}
    for pos, num in enumerate(guess):
        if num == number[pos]:
            score["bulls"] += 1
        elif num in set(number):
            score["cows"] += 1
    return score


def print_evaluation(score: dict,  guesses: int) -> None:
    # !!!!!!!
    print(" ")


def goodbye(guesses: int) -> None:
    if guesses <= 3:
        message = "amazing"
    elif guesses <= 6:
        message = "average"
    elif guesses <= 8:
        message = "not so good"
    else:
        message = "terrible"
    print(f"That's {message}")


def main():
    welcome()
    guesses = 0
    guess = []
    number = generate_number()
    print(number)
    while number != guess:
        guess = make_a_guess()
        guesses += 1
        print(guess)
        score = evaluate_guess(number, guess)
        print_evaluation(score, guesses)
    goodbye(guesses)


if __name__ == '__main__':
    main()
