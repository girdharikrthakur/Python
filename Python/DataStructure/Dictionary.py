#  Dictionary

# Key Value Pair

point = {"x": 1, "y": 2}
point = dict(x=1, y=2, z=3)
print(point)
print(point["x"])

if "x" in point:
    print(point["x"])
print(point.get("x", 0))

del point["x"]
print(point)

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)


# Dictionary Comprehensions

print("============== Dict Comprehensions ===========================")

# Syntax: [expression:  for item in items]


# Generates a Dictionary with key value pair
values = {x: x*2 for x in range(5)}


print("Values", values)

items = (x*2 for x in range(5))  # Generates Generator Object


print("Items", items)
