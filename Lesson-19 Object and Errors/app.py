class JustNotCoolError(Exception):
    pass


x = 2
try:
    raise JustNotCoolError("no colling")
    # raise Exception("I`m a custom Exception")
    # if not type(x) is str:
    #     raise TypeError("Only Strinfs are allowed")
except NameError:
    print("There is an error")
except Exception as error:
    print(error)
except ZeroDivisionError:
    print("NO more zero division")
else:
    print("no error.")
finally:
    print("I'm going to print with or not error")
