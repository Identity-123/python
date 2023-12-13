# empty dictionary
def empty_dict():
    d = {}
    print(type(d))
    print(d)

    # second method
    e = dict()
    print(type(e))
    print(e)


def non_empty_dict():
    fruits = {""
              "Apple = 220",
              "Mango = 100",
              "Banana = 100"
              }
    print(fruits)
    # we can create a dict using another method i.e., zip method
    name = ["apple", 'mango', 'banana']
    prices = [120, 100, 100]
    fruit = dict(zip(name, prices))
    print(fruit)


non_empty_dict()
