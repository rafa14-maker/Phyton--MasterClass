def hello():
    print("Hello world!")


hello()


def sum(num1=0, num2=0):  # default parameter
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum(7, 3)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "john", "sara")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_items(first="dave", last="dave")
