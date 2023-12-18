# Parameters: - the values we pass while defining a function
# Arguments = The actual value of we pass when calling a function

def fun(identity):
    # above identity variable is known as parameter
    print(f"Hello my name is {identity}")


fun("Rajan")
# actual value is known as argument

name = input("Enter your name: -")
# we can create a variable and take input from user and then pass that value as arguments

fun(name)
