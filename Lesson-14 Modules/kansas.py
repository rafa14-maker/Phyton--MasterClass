from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the range"


def randomfunfact():
    funfacts = [
        "kansas is considered flat, but it does have mountain.",
        "Wichita is the largest city.",
        "A considerable portion of kansas city is actually in Missouri .",
        "Most Kansans are annoyed by wizard of Oz",
    ]

    index = choice("0123")
    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
