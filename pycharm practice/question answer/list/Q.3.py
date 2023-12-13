# Python program to interchange first and Last elements in a List
# method 1: -
L = [int(L) for L in input('enter the List = ').split()]


def method(x):
    size = len(x)

    temp = x[0]
    x[0] = x[size - 1]
    x[size - 1] = temp
    print(x)


# method 2:-
def method2(y):
    y[0], y[-1] = y[-1], y[0]