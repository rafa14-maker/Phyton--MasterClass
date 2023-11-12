# rock papar scisser

# value = input("Please enter a value :\n")
# print(value)

import random
import sys
from ast import Continue
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "Enter ...\n1 for Rock\n2 for Paper , or \n3 for Scissors:\n\n"
    )

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1 , 2 or 3")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".")
    print("")

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 1:
        print("You win!")
    elif player == computer:
        print("draw")
    else:
        print("python wins")

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes|\nQ to Quitn\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Celebrate\nThank You for playing")
        sys.exit("Bye !!!!")


play_rps()
