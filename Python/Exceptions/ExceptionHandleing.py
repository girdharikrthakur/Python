try:
    age = int(input("Age : "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError) as ex:
    print("You Didn;t entered a valid age")
    print(ex)
    print(type(ex))
    print(ex.with_traceback)
else:
    print("No Exceptions were thrown")
