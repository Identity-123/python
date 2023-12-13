# even number up to 10
def for_loop():
    for x in range(10):
        if x % x == 0:
            print(x)


def while_loop():
    y = 1
    while y <= 10:
        if y % 2 == 0:
            print("\n", y)
        y = y + 1


# for_loop()
# while_loop()

# for odd num


i = 1
while i <= 10:
    if i % 2 == 1:
        print(i)
    i = i + 1
