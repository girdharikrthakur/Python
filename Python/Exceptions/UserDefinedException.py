from timeit import timeit


# raise an Exception

code1 = """

def calculate_xfactor(age):
    if age <= 0:
        return none
    return 10/age


xfactor = None
try:
    xfactor = calculate_xfactor(10)
    print(xfactor)
except ValueError as error:
    pass


# Cost Of raising Exception

"""

code2 = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or None")
    return 10/age


xfactor = None
try:
    xfactor = calculate_xfactor(10)
    print(xfactor)
except ValueError as error:
    pass


# Cost Of raising Exception

"""
print(timeit(code1, number=10000))
print(timeit(code2, number=10000))
