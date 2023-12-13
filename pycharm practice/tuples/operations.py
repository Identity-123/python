t = (1, 2, 3, 4)

print(t.count(1))

# there are only two methods available for python
#   1. Indexing
#   2. counting
print(t.index(4))

# iteration using tuple
for i in t:
    print(i)

# Concatenation
t1 = (4, 5)
t2 = t + t1
print(t2)
print(t2 * 2)

lst = list(t)
print(type(lst))
t = tuple(lst)
print(type(t))
