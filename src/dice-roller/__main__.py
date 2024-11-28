"""Dice rolling simulator with ASCII art visualization."""

import os
from random import randint
from time import sleep

DICE_ART = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


def clear():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """Run the dice rolling simulator with user interaction."""
    horizontal_display = True

    mode = input("💻 Select display mode [horizontal / vertical]: ")
    if mode in "vertical":
        horizontal_display = False
    clear()

    while True:
        dice_amount = int(input("🎲 How many dices to roll?: "))
        plural = "s" if dice_amount > 1 else ""
        print(f"\n⚙️ Rolling the dice{plural}...\n")
        sleep(1)

        dices = []

        for _ in range(dice_amount):
            dice = randint(1, 6)
            dices.append([DICE_ART[dice], dice])

        if horizontal_display:
            for line in range(5):
                for dice in dices:
                    print(dice[0][line], end=" ")

                print()
        else:
            for dice in dices:
                for line in dice[0]:
                    print(line)

        if all(value == 6 for _, value in dices):
            print("🥳 Awesome! All 6's!")

        input("\n❗ Press [Enter] to retry")
        clear()


if __name__ == '__main__':
    main()
