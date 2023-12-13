x = input()
tup = tuple(map(eval, x.split(',')))
for i in tup:
    frequency = tup.count(i)
    print(f"{i}:{frequency}")
