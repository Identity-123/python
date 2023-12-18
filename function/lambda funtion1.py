def add(a, b):
    return a + b


print(add(3, 4))
# instead of the doing above, we can simply use lambda function

add = lambda a, b: a + b
print(add(4, 5))

# instead of declaring variable use can print a lamda function like this
# by passing a single argument
print((lambda c: c + 10)(4))

# by passing multiple argument
print((lambda a, b: a * b)(5, 7))

