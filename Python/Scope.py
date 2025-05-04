# Scope

message = "a"  # Gloable variable


def greet(name):
    global message
    message = "b"  # Local Variable :  scope is still is local


greet("Hound")


print(message)
