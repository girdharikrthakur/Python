x = 10
y = 20

# z = x
# x = y
# y = z
print("Before")
print(f"X: {x} \nY: {y}\n")

x, y = y, x

print("After")
print(f"X: {x} \nY: {y}")
