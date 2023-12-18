higher_order_fun = lambda x, fun: x + fun(x)

print(higher_order_fun(20, lambda x: x * x))
# in the above code we use function inside function

#  using lambda inside filter
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x: (x % 2 == 0), list_))
# in the above code we use lambda inside filter
print(even)
# using lambda inside map
lst2 = [5, 10, 15, 20, 25]
mul = list(map(lambda x: x * 2, lst2))
print(mul)
lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
power = list(map(lambda x: pow(x, 3), lst3))
print(power)

# use reduce function in python
# reduce function is a part of functools module, so we have to import from there

from functools import reduce

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_ = reduce(lambda x, y: x + y, list4)
# above code will print all the number inside list
print(sum_)

