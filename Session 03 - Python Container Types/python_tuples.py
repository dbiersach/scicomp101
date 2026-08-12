#!/usr/bin/env -S uv run
"""python_tuples.py"""

# C = Create and R = Read
print("Part #1 - Create a List and Tuple and Read Items")
a = []
b = ()

print(f"{a=}")
print(f"{b=}")
#
print(f"{a[0]=}, {a[-1]=}, {a[1:]=}")
#

print("Is 20 in list?", 20 in a)
#
print()

# U = Update, D = Delete
print("Part #2 - Update and Delete Items")
#
#
print(f"{a=}")
try:
    # This will cause an error
    pass
except TypeError as e:
    print("Error:", e)
print(f"{b=}")
try:
    # This will cause an error
    pass
except TypeError as e:
    print("Error:", e)
# "delete" first element by creating a new tuple
#
print(f"{b=}")
print()

print("Part #3 - Insert and Append Items")
try:
    # This will cause an error
    pass
except AttributeError as e:
    print("Error:", e)
try:
    # This will cause an error
    pass
except AttributeError as e:
    print("Error:", e)
#
print(f"{b=}")  # tuples can have duplicate items
print()

print("Part #4 - Clearing Lists and Tuples")
print(f"{a=}")
#
print(f"{a=}")
try:
    pass
except AttributeError as e:
    print("Error:", e)
#
#
print(f"{a=}")
print(f"{b=}")
print()

print("Part #5 - Tuples with Mixed Data Types")
b = ()
print(f"{b=}")
print()

print("Part #6 - Looping Through Tuples")
#
#
print()
#
#
