import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesnt exit .

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())  # read one line then move to the next

for line in f:
    print(line)

f.close()  # if we open the file we should close the file .

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file dont exist")
finally:
    f.close()

# Append - crates the file if it doesnt exist
f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# opens a file for writing , creates the file if it does not exits

f = open("name_list.txt", "w")
f.close()

# Creates the specified file , but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file
# aviod an error if it doesnt exit
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("the file you wish to delete does not exit")


with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
