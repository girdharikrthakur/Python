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

# Syntax: [expression: ]