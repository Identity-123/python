# Parameters

# • These are placeholders in the function.
# • When defining them, we call them as Parameters
# • When passing the actual value, we call them as Arguments.

def greet(name):  # this is a parameter
    print(f"hey!, how are you {name}")


hello = input("enter the name")
greet(hello)  # this is an argument


def add(a, b):
    c = a + b
    print(c)


add(3, 4)
