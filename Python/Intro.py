# Builtin Primitive Types

students_count = 1000  # integer

rating = 4.99  # float

isPublished = True  # boolean

course_name = "Python programming"

print(course_name)


# String

course = "Python Programming"

message = """
Hi Gk
hello
What are you doing
"""
print(message)


# String Builtin Function

# len() : Number of character in a String

print(len(course))  # 18

print(course[0])
print(course[-1])
print(course[0:4])
print(course[0:])
print(course[:7])
print(course[0:4])
print(course[:])

# Escape Sequance
course = "Python \"programming"
print(course)


course = "Python \nProgramming"

print(course)

first = "Mosh"
last = "Hamedani"

full = first+" "+last

print(full)

first = "Evil"
last = "Hound"


full = f"{first} {last}"
full = f"{len(first)} {last}"


print(full)

# String Functions

course = "  Python Programming  "

print(course.upper())
print(course.lower())

print(course)

print(course.title())
print(course.strip)  # lstrip()  rstrip()


print(course.find("Pro"))  # -1 if string is not found in original String


print(course.replace("P", "g"))

print("Pro" in course)  # Boolean Return if Fiund true else Flase


# Returns Boolean if Not found returns True else flase
print("Swift" not in course)


# Arithematic Operators in Python

# + add
# - sub
# * Multiplication
# / Division
# // Division with Integer Output

# % Modulus

# ** Exponent

x = 10
x = x+3

x += 3

print(x)

# Number Functions


# Round for rounding a number

print(round(9.9))  # 10

# abs returns Absolute value

print(abs(-2.3))   # 2.3

# Math Module

# https://www.w3schools.com/python/module_math.asp


# Type Conversion

# type(varible)

# example int(x) bool(isTrue)

x = input("x: ")
y = int(x) + 1  # Type Error due to python takes iput as String

print(f"x : {x}, Y :{y}")


# Boolean in Ptyhon (Truthy and Falsy)

# Falsy   = "" , 0 , None , anything else will be true
