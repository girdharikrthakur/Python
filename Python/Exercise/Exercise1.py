# Display even numbers between 1 -10
count = 0

for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"we have {count} of even Numbers")
