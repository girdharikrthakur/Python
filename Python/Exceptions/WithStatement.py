file = None

try:
    with open("app.py") as file:
        print("File Opened")
        file.__exit__ 
    age = int(input("Age : "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError, FileNotFoundError, NameError) as ex:
    print("You Didn't enter a valid age or the file is missing")
    print(ex)
    print(type(ex))
    print(ex.with_traceback)
else:
    print("No Exceptions were thrown")
