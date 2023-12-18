# we can assign value inside a lambda function like this
add = lambda x, y=2, z=3: x + y + z
print(add(7))
# in the above code we only assign the value of x to call the function

# we can use built-in function like the sum for adding number
addition = lambda *args: sum(args)
print(addition(2, 4, 5, 6, 7, 8))
# in above, we use *args to pass multiple values
# there is a sum(built-in function) that will add the number provided to it
