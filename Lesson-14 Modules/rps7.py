# rock papar scisser

# value = input("Please enter a value :\n")
# print(value)

import random
import sys
from ast import Continue
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        print(f"\nYou chose {str(RPS(player)).replace("RPS.", "")}.")
        print(f"Python chose  {str(RPS(computer)).replace("RPS.", "")}.")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win!"
            elif player == 3 and computer == 1:
                player_wins += 1
                return "You win!"
            elif player == computer:
                return "draw"
            else:
                python_wins += 1
                return "python wins"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count : {str(game_count)}")
        print(f"\nPlayer Wins : {str(player_wins)}")
        print(f"\nPython Wins : {str(python_wins)}")

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

    return play_rps


rock_paper_scissors = rps()


if __name__ == "__main__":
    rock_paper_scissors()
