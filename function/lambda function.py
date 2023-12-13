large = (lambda a, b: a if a > b else b)
print(large(2, 3))


# we are now calling function as an arguments to the function


def double(fx, value):
    return 7 + fx(value)


print(double(lambda x: x * x * x, 2))
