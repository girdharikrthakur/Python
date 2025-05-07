# List

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

matrix = [[1, 2], [2, 3]]

zeros = [0]*5

combined = zeros+letters

numbers = list(range(20))
print(numbers)


chars = list("Evil Hound")

print(chars)
print(f"length of chars is {len(chars)}")


print(letters[0])
print(letters[-2])


# Slicing List
print(letters[1:3])
print(letters)
print(letters[::3])


# Unpacking List

numbers = list(range(1, 21))

print(numbers)

first, second, third, * others = numbers
print(first)
print(second)
print(third)
print(others)

# Looping ober a list

print("============================================================")

numbers = [1, 2, 3, 4, 5, 6]

for index, num in enumerate(numbers):
    print(index, num)


# Add and Remove Items


# Add ? Insert
letters = ["a", "b", "c", "d"]
print(letters)
letters.append("e")
letters.insert(0, "_")
print(letters)


# Delete/Remove
letters.pop(0)
print(letters)
letters.remove("b")
print(letters)

del letters[0]
del letters[0:2]
print(letters)


# Shorting List
print("========================+ Shorting List ================================")
numbers = [1, 2, 3, 4, 5, 6, 10, 7, 8, 11, 9]
print(f"unsorted list {numbers}")

numbers.sort()  # Modifies the Origina List
numbers.sort(reverse=True)  # Sorted in  Decending Order
print(f"Sorted List {numbers}")


new_sorted_List = sorted(numbers)  # Returns a New List
NewListDecending = sorted(numbers, reverse=True)
print(f"Original List {numbers}")
print(f"New List {new_sorted_List}")
print(f"New List Sorted in decending Order {NewListDecending}")


items = [
    ("Product1", 50),
    ("Product2", 20),
    ("Product3", 40),
    ("Product4", 10)
]


# def sort_items(item):
#     return item[1]


# items.sort(key=sort_items)
# print(items)


# Lambda Function


# We Can define a Lambda
# (lambda Parameter:Expression)  lambda is keyword

print("==================== Lambda Function =======================================")

# Sorting using lambda Function

items.sort(key=lambda item: item[1])
print(items)


# Mam Function


print("============== Map function =======================")

# Syntax : map(function, iterable)


# without a map function
# prices =[]
# for price in items:
#     prices.append[1]
# print(prices)

# Using lambda expression


x = map(lambda item: item[1], items)  # A map obkect is Iterable
print(list(x))


# Fiter Function


print("============== Filter Function ======================")

# Syntax : filter(function, iterable)

# filetr object is Iterable
filtered = filter(lambda item: item[1] >= 20, items)

print(list(filtered))


# List Comprehensions

print("============= Comprehensions ==========================")

# Syntax : [expression for itemm in items]


# for map
# prices = map(lambda item: item[1], items)
# prices =[item[1] for item in items]


prices = [item[1] for item in items]

print(f" Prices are: {prices}")


# for Filter

filtered = [item for item in items if item[1] >= 10]

print(filtered)


# Zip Function

print("========== Zip Function ===================")


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(list(zip(list1, list2)))
print(list(zip("abc")))


