fruits = {
    "Apple ": 120,
    "Mango": 100,
    "Banana": 100
}
# we can excess dictionary nby corresponding key
print(fruits['Mango'])
print(fruits["Banana"])


# if we try to excess a key
# which is not present inside the dictionary, then we will get error
def error():
    print(fruits["Orange"])


# There is another method to excess value inside dict. It basically avoids error
print(fruits.get("Guava"))
print(fruits.get("Guava", " Not Available"))
print(fruits["Guava"])
