# deleting the data
# 1. pop
# 2. popitem
# 3. del


# 1. pop :-
def pop_dict():
    fruits = {
        "Apple": 120,
        "mango": 100,
        "pineapple": 90
    }
    fruits.pop("apple")
    print(fruits)


def popitem_dict():
    fruits = {
        "Apple": 120,
        "mango": 100,
        "pineapple": 90
    }
    fruits.popitem()
    # here pop item is used to remove last digit of dictionary.


def del_dict():
    fruits = {
        "Apple": 120,
        "mango": 100,
        "pineapple": 90
    }
    # del fruits
    # del method is used to delete entire elements of dictionary including dictionary.


pop_dict()
popitem_dict()
del_dict()
