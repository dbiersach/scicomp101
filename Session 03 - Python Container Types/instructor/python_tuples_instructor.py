#!/usr/bin/env -S uv run
"""python_tuples_instructor.py"""

# C = Create and R = Read
print("Part #1 - Create a List and Tuple and Read Items")
a = [10, 20, 30]
b = (50, 60, 70, 80)

print(f"{a=}")
print(f"{b=}")
print(f"{len(a)=}, {len(b)=}")
print(f"{a[0]=}, {a[-1]=}, {a[1:]=}")
print(f"{b[0]=}, {b[-1]=}, {b[1:]=}")

print("Is 20 in list?", 20 in a)
print("Is 20 in tuple?", 20 in b)
print()

# U = Update, D = Delete
print("Part #2 - Update and Delete Items")
a[1] = 99
a.append(40)
print(f"{a=}")
try:
    # This will cause an error
    b[1] = 99
except TypeError as e:
    print("Error:", e)
print(f"{b=}")
try:
    # This will cause an error
    del b[1]
except TypeError as e:
    print("Error:", e)
# "delete" first element by creating a new tuple
b = b[1:]
print(f"{b=}")
print()

print("Part #3 - Insert and Append Items")
try:
    # This will cause an error
    b.insert(2, 30)
except AttributeError as e:
    print("Error:", e)
try:
    # This will cause an error
    b.append(50)
except AttributeError as e:
    print("Error:", e)
b = b + (50,)  # "append" by creating a new tuple
print(f"{b=}")  # tuples can have duplicate items
print()

print("Part #4 - Clearing Lists and Tuples")
print(f"{a=}")
a.clear()
print(f"{a=}")
try:
    b.clear()
except AttributeError as e:
    print("Error:", e)
a = []  # A new empty list
b = ()  # A new empty tuple
print(f"{a=}")
print(f"{b=}")
print()

print("Part #5 - Tuples with Mixed Data Types")
b = ("Alice", 42, 3.14, True)
print(f"{b=}")
print()

print("Part #6 - Looping Through Tuples")
for i in range(len(b)):
    print(i, b[i])
print()
for index, item in enumerate(b):
    print(index, item)
