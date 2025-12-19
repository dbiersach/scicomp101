# python_sets_instructor.py

# C = Create and R = Read
print("Part #1 - Create Sets and Read Items")
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = {10, 10, 20, 20, 30}  # duplicates ignored automatically

print(f"{a=}")
print(f"{b=}")
print(f"{c=}  # duplicates removed")

print(f"len(a) = {len(a)}")
try:
    first_item = a[0]  # This will fail because sets are unordered
except TypeError as e:
    print("Error:", e)
print("Is 20 in a?", 20 in a)
print("Is 99 in a?", 99 in a)
print()

# U = Update, D = Delete
print("Part #2 - Update and Delete Items")
try:
    a[0] = 7  # This will fail because sets are unordered
except TypeError as e:
    print("Error:", e)
a.add(50)
a.add(20)  # duplicate; has no effect
print(f"{a=}  # 20 was already in the set")
a.remove(30)  # removes 30 (error if missing)
print(f"{a=}")
a.discard(999)  # safe, no error if missing
print(f"{a=}")
popped_item = a.pop()
print(f"Popped item: {popped_item}")
print(f"{a=}")
print()

print("Part #3 - Clearing Sets")
print(f"{b=}")
b.clear()
print(f"{b=}")
b = set()  # Declare a new empty set
print(f"{b=}")
print()

print("Part #4 - Sets with Mixed Data Types")
mixed = {"Alice", 42, 3.14, True}
print(f"{mixed=}")
print()

print("Part #5 - Looping Through Sets")
d = {100, 200, 300}
for item in d:
    print("Set item:", item)
print()

print("Part #6 - Union, Intersection, Difference")
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(f"{x=}")
print(f"{y=}")
print("Union (x | y):", x | y)
print("Intersection (x & y):", x & y)
print("Difference (x - y):", x - y)
print("Difference (y - x):", y - x)
print("Symmetric Difference (x ^ y):", x ^ y)
print()

print("Part #7 - Demonstrating Duplicate Removal")
duplicates = {1, 1, 2, 2, 3, 3, 3}
print(f"{duplicates=}, {len(duplicates)=}")
print()
