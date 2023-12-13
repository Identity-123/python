# Code for creating nested tuples
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')

tuple3 = (tuple1, tuple2)
print(tuple3)
print(tuple3[1])
# we can delete tuple by using del function
x = (1,)
del x
tup = ('code',)
for i in range(5):
    tup = (tup,)
    print(tup)
