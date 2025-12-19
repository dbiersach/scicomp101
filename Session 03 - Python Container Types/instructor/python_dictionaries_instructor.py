# python_dictionaries_instructor.py

from pprint import pprint

# C = Create and R = Read
print("Part #1 - Create Dictionary and Read Items")
capitals = {
    "USA": "Washington D.C.",
    "Egypt": "Cairo",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "France": "Paris",
    "Morocco": "Rabat",
    "Germany": "Berlin",
    "South Africa": "Pretoria",
}
print(capitals)
pprint(capitals)
print(capitals["USA"])
print()

# U = Update, D = Delete
print("Part #2 - Update and Delete Items")
capitals["USA"] = "New York"
del capitals["Russia"]
pprint(capitals)
print()

# Part #3 - Insert Items
print("Part #3 - Insert Items")
capitals.update({"United Kingdom": "London"})
capitals["Spain"] = "Madrid"
pprint(capitals)
print()

# Part #4 - Looping Through Dictionaries
print("Part #4 - Looping Through Dictionaries")
for country in capitals:
    print(f"Country: {country}, Capital: {capitals[country]}")
print()
for country, city in capitals.items():
    print(f"Country: {country}, Capital: {city}")
print()

# Part #5 - Dictionary Components
print("Part #5 - Dictionary Components")
keys = capitals.keys()
values = capitals.values()
print("Countries:", list(keys))
print("Capitals:", list(values))
