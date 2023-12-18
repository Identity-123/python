# write a python function that takes a list and returns a new list with unique elements of the first list
list = [1, 2, 3, 4, 5, 3, 3, 8, 9, 7, 4]
new = []


def unique(li):
    for i in li:
        if i not in new:
            new.append(i)

    return new


print(unique(list))
