a = 0
b = 1
fibo = []
count = int(input("enter how many time  you want to print "))

if count == 0:
    print(count)
else:
    fibo = [1]
    while count-1 > 0:
        add = a + b
        a = b
        b = add
        fibo.append(add)
        count -= 1
print(fibo)
