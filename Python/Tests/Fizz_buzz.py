def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz_buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    return number


print(fizz_buzz(5))
