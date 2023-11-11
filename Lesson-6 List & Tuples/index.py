users = ["dave", "john", "sara"]

data = ["hello", 42]

emptylist = []

print("dave" in data)
print(data[0])
print(data[-1])


print(users.index("sara"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])


print(len(data))

users.append("Elsa")
print(users)

users += ["jason"]
print(users)

users.extend(["robert", "jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)


users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)


print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)


# Tuples

mytuple = tuple(("dave", 42, True))
anothertuple = (1, 2, 2, 3, 4)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("neil")
newtuple = tuple(newlist)
print(newtuple)


(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
