# write a program to swap first and last element in a list
l = []
x = int(input('enter the number of elements you want'))
for i in range(0, x):
    r = int(input(f' enter {i} elements '))
    l.append(r)
print(l)
for j in range(0,x):
    temp = l[0]
    l[j] = l[x-1]
    l[x-1] = temp
print(l)
