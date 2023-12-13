# Scope of a variable

# There are two scopes of a variable: Global and Local
# Global variable can be used anywhere in a program
# Local variable can only be used locally inside a program(function)
# a can be used anywhere in the program
a = 5


# it is independent to local variable


def fun():
    print(a)


fun()
print(a)


def fun1():
    x = 3
    # x is the local variable to the function
    print(x)


fun1()
print(a)

# if we want to change global vale inside function
x = 5


def fun3():
    global x
    x = 39
    print(x)


# if we dont call function, the value of x is unchangeable
print(x)
# after calling fun3() it will change the variable value
fun3()
print(x)
