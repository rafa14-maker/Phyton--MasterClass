# name = 90
# print(name)
# print(type(name))
# name = str(name)
# print(type(name))


# multiline = """
# hey, How are you??
# I am fine .
# """

# print(multiline)
# multiline = multiline.replace("fine", "ok")
# print(multiline)

# first = "hello"
# print(first)
# first = first.upper()
# print(first)

# name = "fahim"
# print(name)
# name = name.strip("f")
# print(name)

# result = "abcabababababcababc"
# print(result)
# result = result.lstrip("ab")
# print(result)

# text = "ABCDABCDDCBA"
# result = text.lstrip("AB")
# print(result)

# title = "menu".upper()
# print(title.center(20, "="))
# print("coffee".ljust(16, ".") + "$1".rjust(4))


# first = "name"
# print(first[1:-1])


# name = input("Your name : ")
# print(name)

data = ["fahim", "Hossain"]
users = ["dave", "John", "Sara"]

# print(users.index("Sara"))
# users.append("Elsa")
# print(users)
# users += "rafayet"
# print(users)
# users += ["rafayet"]
# print(users)
# users.extend(["jimmy", "robert"])
# print(users)

# users.insert(0, "Bob")
# print(users)

# users[2:2] = ["Eddie", "Alex"]
# print(users)

# users[1:3] = ["Robert", "JPJ"]
# print(users)

# users.remove("Bob")
# print(users)

# users.pop()
# print(users)

# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)

# band = {
#     "vocals": "plant",
#     "guiter": "page",
# }

# print(type(band))

# print(band.values())

# print(band.items())

# print("guiter" in band)


# band["vocals"] = "coverdate"
# print(band)

# band.update({"bass": "JPJ"})
# print(band)

# band["drums"] = "bonham"
# print(band)

# value = 1

# while value <= 10:
#     print(value)
#     value += 1

# name = ["rafayet", "fahim", "Hossain"]
# idx = len(name)

# for x in range(0, idx):
#     print(name[x])

# for x in range(1, 11):
#     for y in range(1, 11):
#         print(f"{x} X {y} = {x*y}")\


# def fibo(num):
#     if num <= 0:
#         return 0
#     if num == 1:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)


# for x in range(0, 10):
#     print(fibo(x))

# num = 10

# print(f"\n 2.25 times {num} is {2.25 * num:.4f} \n")


# squared = lambda num: num * num
# sum = lambda a, b: a + b

# print(squared(4))
# print(sum(10, 90))


# def fb(x):
#     return lambda num: num + x


# addten = fb(10)
# addtwenty = fb(20)

# print(addten(8))
# print(addtwenty(7))


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("The car is moving")

    def get_make_model(self):
        print(f"I'm a {self.make} and {self.model}")


my_car = Car("Honda", "toyota")

my_car.get_make_model()
