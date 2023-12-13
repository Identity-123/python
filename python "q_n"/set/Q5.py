def firstMethod():
    set1 = {10, 20, 30, 40, 50}
    set1.remove(10)
    set1.remove(20)
    set1.remove(30)
    print(set1)


# another method
def secodMethod():
    set1 = {10, 20, 30, 40, 50}
    remove = {10, 20, 30}
    set1 -= remove
    print(set1)


def third():
    set1 = {10, 20, 30, 40, 50}
    items_to_remove = {10, 20, 30}

    result_set = set1.difference(items_to_remove)

    print(result_set)


firstMethod()
secodMethod()
third()