file = None  

try:
    file = open("Exceptions/app.py", "r")  
    age = int(input("Age : ")) 
    xfactor = 10 / age
except (ValueError, ZeroDivisionError, FileNotFoundError, NameError) as ex:
    print("You Didn't enter a valid age or the file is missing")
    print(ex)
    print(type(ex))
    print(ex.with_traceback)
else:
    print("No Exceptions were thrown")
finally:
    if file is not None:
        file.close()
