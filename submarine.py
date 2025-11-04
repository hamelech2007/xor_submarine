from typing import Tuple
import random


MAX_GUESS = 10
MIN_GUESS = 1


def is_one_away(sub_x: int, sub_y: int, x: int, y: int) -> bool:
    """Checks wether or not the given coords are one sqaure away from the submarine."""
    delta_x, delta_y = abs(sub_x - x), abs(sub_y - y)
    if delta_x == 0 and delta_y == 0:
        return False
    return delta_x <= 1 and delta_y <= 1


def is_valid_guess(x: int, y: int) -> bool:
    """
    Checks if a guess is within bounds
    """
    if x > MAX_GUESS or x < MIN_GUESS:
        return False
    if y > MAX_GUESS or y < MIN_GUESS:
        return False

    return True


def is_input_int(x_in: str, y_in: str) -> bool:
    """
    Checks if the user's input is an integer
    """
    try:
        int(x_in)
        int(y_in)
    except ValueError:
        return False
    return True


def handle_guess(sub_x: int, sub_y: int, x: int, y: int) -> bool:
    """
    Prints the correct statement in regards to the provided guess.
    :return: True if the user guessed the submarine's location
    """
    if x == sub_x and y == sub_y:
        print("Exactly")
        return True
    elif is_one_away(sub_x, sub_y, x, y):
        print("Close")
    elif x == sub_x or y == sub_y:
        print("Interesting")
    else:
        print("Keep thinking")
    return False


def play_submarine() -> None:
    sub_x, sub_y = random.randint(MIN_GUESS, MAX_GUESS), random.randint(MIN_GUESS, MAX_GUESS)
    tries = 0

    while True:
        tries += 1
        in_y = input("Guess a row: ")
        in_x = input("Guess a column: ")
        if not is_input_int(in_x, in_y):
            print("Please enter an integer")
            continue

        x, y = int(in_x), int(in_y)

        if not is_valid_guess(x, y):
            print(f"{x}, {y} is not a valid guess")
            continue

        if handle_guess(sub_x, sub_y, x, y):
            break

    print(f"You guessed the submarine's location in {tries} tries")
