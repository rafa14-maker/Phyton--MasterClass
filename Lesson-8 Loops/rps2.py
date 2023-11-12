# rock papar scisser

# value = input("Please enter a value :\n")
# print(value)

import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    print("")
    playerchoice = input(
        "Enter ...\n1 for Rock\n2 for Paper , or \n3 for Scissors:\n\n"
    )

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1 , 2 or 3.")

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

    playagain = input("\nPlay again?\nY for Yes|\nQ to Quit\n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("Celebrate\nThank You for playing")
        playagain = False

sys.exit("Bye !!!!")
