import greeting
import GuessNumber
import rps as RockPaperScissor

playername = greeting.GetName()

# RockPaperScissor.rps(playername)
# GuessNumber.GuessNumber(playername)


def arcade():
    count = 0
    greeting = "welcome"
    while 1:
        if count == 0:
            greeting = "welcome"
        else:
            greeting = "Welcome back"

        print(f"\n\n{greeting} , {playername} to the Arcade !!")
        print("\n Please choose a Game :")
        print("\n 1 = Rock , Paper and Scissors")
        print("\n 2 = Guess the Game")
        print("\n 3 = Quit Arcade")
        n = int(input("\nEnter your consent :"))

        if n != 1 and n != 2 and n != 3:
            print("\nPlease Enter valid choice")
            continue
        elif n == 1:
            RockPaperScissor.rps(playername)
            count += 1
        elif n == 2:
            GuessNumber.GuessNumber(playername)
            count += 1
        else:
            print(f"\n Thanks for begin here {playername}\n\n Bye , Have fun !!\n")
            break


arcade()
