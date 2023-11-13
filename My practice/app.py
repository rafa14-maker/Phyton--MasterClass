x = "banana"
y = 10

print("all of my", x, "I have only", y)


title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, "."), "$1".rjust(4))


# name = input("You name :")

# print(name)

data = ["fahim", 42]
users = ["fahim", "hossain", "dave"]

print(users)

users.append("rafayet")
print(users)

users.extend(["kp", "kc"])
print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["robert"]
print(users)

users[2:3] = ["karim"]
print(users)

# users.remove("robert")
# print(users)

# users.pop()

users.sort()
print(users)
