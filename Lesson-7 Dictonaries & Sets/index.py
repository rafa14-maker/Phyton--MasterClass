print("hello")
# dictonaries

band = {"vocals": "plant", "guitar": "page"}

band2 = dict(vocals="plant", guiter="page")

print(band)
print(band2)
print(len(band))
print(type(band))

# acess items
print(band["vocals"])
print(band.get("guitar"))


# List all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# varify a key exits
print("guiter" in band)
print("triangle" in band)


# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop())
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)

print(band.popitem())  # return a tuple
print(band())

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictonaries

# band2 = band  # create a reference
# print("Bad copy !")
# print(band2)
# print(band)

# band2["drums"] = "dave"
# print(band)

band2 = band.copy
band2["drums"] = "Dave"
print(band2)

# or use the direct() constructor function
band3 = dict(band)
print(band3)

# Nested dictionaries

member1 = {"name": "plant", "instrument": "vocals"}
member2 = {"name": "page", "instrument": "guitar"}
band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])


# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1 , false is a dupe of zero
nums = {1, True, 2, False, 0}
print(nums)

# check if a vlaue is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists , tuples and dictonaries , too.

# Merge Two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
