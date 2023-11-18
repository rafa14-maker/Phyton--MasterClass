def GuessNumber(name):
    gameCount = 0
    gameWin = 0
    from random import choice

    def playGame():
        nonlocal gameCount
        nonlocal gameWin
        nonlocal name

        print(f"\n{name} , guess which Number")
        print(f"\nI'm thinking of 1, 2 or 3.\n")
        playerchoice = input("Give Your Number :")

        mychoice = choice("123")

        if mychoice == playerchoice:
            gameCount += 1
            gameWin += 1
            print(f"{name} , you won !!!")
        else:
            gameCount += 1
            print(f"Sorry , {name}.Better luck next time.")

        score = 0

        if gameCount != 0 and gameWin != 0:
            score = gameWin / gameCount

        print(f"\nGame Count: {gameCount}")
        print(f"\n{name} Count: {gameWin}")
        print(f"\nWinning Percentage : {score:.2f}")

        print(f"\nPlay Again !!!")
        print(f"\n Y for Yes")
        print(f"\nQ for No")

        gameprogress = input("\nEnter your consent :").lower()

        while gameprogress != "y" and gameprogress != "q":
            print("\n\nPlease Enter Letter Y or Q !!")
            gameprogress = input("\nEnter your consent :").lower()

        if gameprogress == "y":
            playGame()
        else:
            print(f"\n{name} , Thanks for playing .\n\nBye !!!!\n")
            return

    playGame()
