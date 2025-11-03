import random


def is_one_away(sub_x: int, sub_y: int, x: int, y: int) -> bool:
    """Checks wether or not the given coords are one sqaure away from the submarine."""
    delta_x, delta_y = abs(sub_x - x), abs(sub_y - y)
    if delta_x == 0 and delta_y == 0:
        return False
    return delta_x <= 1 and delta_y <= 1


def play_submarine() -> None:
    sub_x, sub_y = random.randint(1, 10), random.randint(1, 10)
    tries = 0

    while True:
        tries += 1
        y = int(input("Guess a row: "))
        x = int(input("Guess a column: "))

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
