# finding quadratic
def qudratic(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = qudratic(2, 3, 4)

# in above,The quadratic function is called with the arguments 2, 3, and 4.

result = f(1)

# The lambda function stored in f is called with argument 1.
# This evaluates the quadratic equation 2(1)^2 + 3(1) + 5,
# and the result is stored in the variable result.
print(result)
