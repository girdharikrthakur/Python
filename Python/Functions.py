# Defineing a Fucntions

def greet():
    print("Hello World")
    print("Welcome Aboard")


greet()


# Passing Arguments


def name(first_name, last_name):
    print(f"My Name is {first_name} {last_name}")


name("Girdhari", "Thakur")


name("Evil", "Hound")


# Types of a function
# 1- Performs a task
# 2- Returns a Value

def name(name):
    return f"Hi {name}"


message = name("Evil Hound")

print(message)

file = open("Content.txt", "w")

file.write(message)


def test(message):
    print(f"hi {message}")


print(test("Jack"))


print("============================================")


def increment(number, by):
    return number+by


print(increment(10, by=2))


print("=====================================================")

# Optional Parameter


def decrement(number, by=2):  # Here By=2 is an Optional Parameter And all the optional parametr shound come after required Parameter
    return number-by


print(decrement(6, 1))


print("==============================================")


# xargs

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


print("=============================================================")


# xxargs


def save_user(**user):
    print(user)
    print(f"name of the user is {user["name"]}")


save_user(id=1, name="John", age=30)
