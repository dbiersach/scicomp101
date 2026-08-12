#!/usr/bin/env -S uv run
"""python_lists_instructor.py"""

# C = Create and R = Read
print("Part #1 - Create a List and Read Items")
a = [10, 20, 30, 40, 50]
print(f"{a=}")
print(f"{a[0]=}, {a[4]=}, {a[-1]=}, {a[-2]=}")
print()

# U = Update, D = Delete
print("Part #2 - Update and Delete Items")
a[0] = 15
print(f"{a=}")
del a[2]
print(f"{a=}")
print()

print("Part #3 - Insert and Append Items")
a.insert(2, 30)
print(f"{a=}")
a.append(60)
a.append(20)  # Lists can have duplicate items
print(f"{a=}")
print()

print("Part #4 - Extending Lists")
a.extend([70, 80, 90])
print(f"{a=}")
print()

print("Part #5 - Slicing Lists")
print(f"{a[1:4]=}")
print(f"{a[:2]=}")
print(f"{a[2:]=}")
print(f"{a[::2]=}")
print(f"{a[1:5:2]=}")
print(f"{a[1::2]=}")
print()

print("Part #6 - Lists with Mixed Data Types")
b = ["Alice", 42, 3.14, True]
print(f"{b=}")
print()

print("Part #7 - Looping Through Lists")
for i in range(len(b)):
    print(i, b[i])
print()
for index, item in enumerate(b):
    print(index, item)
