def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


my_newtotal = add_one(0)
print(my_newtotal)
