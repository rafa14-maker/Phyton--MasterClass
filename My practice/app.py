# x = "banana"
# y = 10

# print("all of my", x, "I have only", y)


# title = "menu".upper()
# print(title.center(20, "="))
# print("coffee".ljust(16, "."), "$1".rjust(4))


# # name = input("You name :")

# # print(name)

# data = ["fahim", 42]
# users = ["fahim", "hossain", "dave"]

# print(users)

# users.append("rafayet")
# print(users)

# users.extend(["kp", "kc"])
# print(users)

# users.insert(0, "Bob")
# print(users)

# users[2:2] = ["robert"]
# print(users)

# users[2:3] = ["karim"]
# print(users)

# # users.remove("robert")
# # print(users)

# # users.pop()

# users.sort()
# print(users)


names = ["fahim", "rafayet", "Hossain", "ammu", "abbu"]

# for x in names:
#     print(x)

# # for x in range(0, 10):
# #     print(x)

# for x in range(0, 10, 3):
#     print(x)

# for x in names:
#     print(x)


# odd = []
# even = []

# for i in range(0, len(names)):
#     if i % 2:
#         odd.append(names[i])
#     else:
#         even.append(names[i])

# print(odd)
# print(even)


# def fac(num):
#     if num == 0 or num == 1:
#         return 1

#     return num * fac(num - 1)


# n = input("Input factorial :")
# print(fac(int(n)))


# def make_multiplier(n):
#     def calculate(x):
#         return n * x

#     return calculate


# times3 = make_multiplier(3)
# times5 = make_multiplier(5)

# print(times3(4))
# print(times5(4))
# print(times3(times5(4)))

# import greet

# greet.greeting()

# ten3 = greet.fact(3)

# print(ten3(int(10)))


import argparse

parser = argparse.ArgumentParser(description="Provides the name to greet ")

parser.add_argument(
    "--n",
    "--name",
    metavar="name",
    dest="name",
    required=True,
    help="The name of the person to greet",
)

args = parser.parse_args()
msg = f"hello {args.name}!"

# print(msg)

# for x in range(2, 100, 2):
#     print(x)
