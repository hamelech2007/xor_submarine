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


def validate_input(x_in: str, y_in: str) -> Tuple[bool, int, int]:
    """
    Validates the given input.
    :return: A tuple of which the 1st element describes wether or not the input is valid,
             and the 2nd and 3rd elements are the inputs as ints
    """
    if not x_in.isdigit() or not y_in.isdigit():
        return False, 0, 0

    x, y = int(x_in), int(y_in)

    if x > MAX_GUESS or x < MIN_GUESS:
        return False, 0, 0
    if y > MAX_GUESS or y < MIN_GUESS:
        return False, 0, 0

    return True, x, y


def play_submarine() -> None:
    sub_x, sub_y = random.randint(MIN_GUESS, MAX_GUESS), random.randint(MIN_GUESS, MAX_GUESS)
    tries = 0

    while True:
        tries += 1
        in_y = input("Guess a row: ")
        in_x = input("Guess a column: ")
        valid, x, y = validate_input(in_x, in_y)

        if not valid:
            continue

        if x == sub_x and y == sub_y:
            print("Exactly")
            break
        elif is_one_away(sub_x, sub_y, x, y):
            print("Close")
        elif x == sub_x or y == sub_y:
            print("Interesting")
        else:
            print("Keep thinking")
    print(f"You guessed the submarine's location in {tries} tries")
