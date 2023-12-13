


def solve(x):
    if (x % 400 == 0) and (x % 100 == 0):
        print(1)
    elif (x % 4 == 0) and (x % 100 != 0):
        print(1)
    else:
        print(0)


class Solution:
    A = int(input('enter a number'))

    # @return an integer
    solve(2020)



