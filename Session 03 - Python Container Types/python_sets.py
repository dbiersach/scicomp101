# python_sets.py

# C = Create and R = Read
print("Part #1 - Create Sets and Read Items")
a = {}
b = {}
c = {}  # duplicates ignored automatically

print(f"{a=}")
print(f"{b=}")
print(f"{c=}  # duplicates removed")

print(f"len(a) = {len(a)}")
#
#
#
#
print("Is 20 in a?", 20 in a)
#
print()

# U = Update, D = Delete
print("Part #2 - Update and Delete Items")
try:
    a[0] = 7  # This will fail because sets are unordered
except TypeError as e:
    print("Error:", e)
#
#
print(f"{a=}  # 20 was already in the set")
#
print(f"{a=}")
#
print(f"{a=}")
#
#
print(f"{a=}")
print()

print("Part #3 - Clearing Sets")
print(f"{b=}")
#
print(f"{b=}")
#
print(f"{b=}")
print()

print("Part #4 - Sets with Mixed Data Types")
#
#
print()

print("Part #5 - Looping Through Sets")
#
#
#
print()

print("Part #6 - Union, Intersection, Difference")
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(f"{x=}")
print(f"{y=}")
#
#
#
#
#
print()

print("Part #7 - Demonstrating Duplicate Removal")
#
#
print()
