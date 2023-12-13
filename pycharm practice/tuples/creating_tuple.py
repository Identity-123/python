# creating a tuple
# creating and empty tuple
t = ()
x = tuple()
z = tuple
print(type(x))
print(type(z))
print(type(t))

# creating non-empty tuple

# >> creating single elements tuple

t4 = (2,)
print(type(t4))

# >>iterable in tuple
t5 = tuple('Rahul')
print(t5)
# we can add list inside tuple
t6 = ([1, 2], [3, 4])

# mutability in tuples
# if you have any kind of list inside tuple we can change elements inside list:
# reference is not changing
tup_le = ([2, 3, 4], "rahul")
tup_le[0][0] = 4
print(tup_le)
