# A function call ends when a return statement is executed
# it return statement are not executed
# the code after a return statement are not executed
# if there is no return value then function returns none

def add(a, b):
    c = a + b
    print(c)
    print(c + 1)


b = add(3, 4)

print(b, type(b))


# if you dont use return function, the type will be none or it will not return any value

def add1(e, d):
    sum = e + d
    print(sum + 1)
    return sum
    print(2 + 1)


f = add1(3, 5)
print(f, type(f))
