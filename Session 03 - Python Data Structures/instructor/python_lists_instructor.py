# python_lists_instructor.py

print("\nPart #1 - Create Lists and Read Items")
a = [10, 20, 30, 40, 50]
print(f"{a=}")
print(f"{a[0]=}, {a[4]=}, {a[-1]=}, {a[-2]=}")

print("\nPart #2 - Update, Delete, and Append Items")
a[0] = 15
del a[2]
a.append(60)
a.append(20)  # Lists can have duplicate items
print(f"{a=}")

print("\nPart #3 - Insert Items")
a[0] = 10
a.insert(2, 30)
print(f"{a=}")

print("\nPart #4 - Extending Lists")
a.pop()
a.extend([70, 80, 90])
print(f"{a=}")

print("\nPart #5 - Slicing Lists")
print(f"{a[1:4]=}")
print(f"{a[:2]=}")
print(f"{a[2:]=}")
print(f"{a[::2]=}")
print(f"{a[1:5:2]=}")
print(f"{a[1::2]=}")

print("\nPart #6 - Lists with Mixed Data Types")
b = ["Alice", 42, 3.14, True]
print(f"{b=}")

print("\nPart #7 - Looping Through Lists")
for i in range(len(b)):
    print(i, b[i])
print()
for index, item in enumerate(b):
    print(index, item)
