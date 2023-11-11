import math

print("hello")


def hello(n):
    return n * n


print(hello(9))


# String data type


# literal assignment

first = "Dave"

last = "Gray"


# print(type(first) == str)

# print(type(first))

# print(isinstance(first,str))

# constructor function

# pizza = str("peparonni")

# print(type(pizza) == str)

# print(type(pizza))

# print(isinstance(pizza,str))

# concatination

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)


# casting a number to string

decade = str(1980)

print(type(decade))

print(decade)


statement = "i like rock music from the " + decade + "s."
print(statement)

# multiple lines

multiline = """ 

hey, how are you ?


i was just checking in .


         all good ?
"""
print(multiline)


# Escaping special characters

# sentence = "I'm back at work!\they!\n\nWhers\s this at\\located ?"
# print(sentence)


# string methods


print(first)

print(first.lower())

print(first.upper())

print(first)

print(multiline.title())

print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))

multiline += "                             "

multiline = "                 " + multiline
print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))


# build a menu

title = "menu".upper()


print(title.center(20, "="))

print("Coffee".ljust(16, ".") + "$1".rjust(4))

print("Muffin".ljust(16, ".") + "$2".rjust(4))

print("ChesseCake".ljust(16, ".") + "$6".rjust(4))

print("")


# string index values

print(first[1])

print(first[-1])

print(first[1:-1])

print(first[1:])


# Some methods return boolean data

print(first.startswith("D"))

print(first.endswith("Z"))


# Boolean Data type

myvalue = True

x = bool(False)

print(type(x))

print(isinstance(myvalue, bool))


# numeric data type

price = 100

best_price = int(80)

print(type(price))

print(isinstance(best_price, int))


# float type
y = float(1.14)
print(type(3.28))

# complex type

# comp_value = 5+3j


# print(type(comp_value))

# print(comp_value.img)

# print(comp_value.real)


# bulit in functions for numbers


print(abs(3.28))

print(abs((3.28) * -1))

print(round(3.28))

print(round(3.28, 1))


print(math.pi)

print(math.sqrt(64))

print(math.ceil(3.28))
print(math.floor(3.28))

# Casting a String to a number

zipcode = "10001"

zip_value = int(zipcode)

print(type(zip_value))


# Error if you attempt to cast incorrect data
