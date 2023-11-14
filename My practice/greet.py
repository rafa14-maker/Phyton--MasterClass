def greeting():
    print("hello")


def fact(n):
    def calculate(x):
        return x * n

    return calculate


# if ___name___ == ___main___ :
#    greeting()
