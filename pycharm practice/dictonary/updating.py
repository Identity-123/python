# we can update a dictionary using two method
# 1- Using key
fruits = {
    "Apple": 100,
    "Mango": 120,
    "Banana": 40,
}
fruits["Apple"] = {"small": 40, "large": 100}
print(fruits)
fruits["guava"] = 80
print(fruits)

# to add multiple value inside dict, there is a method i.e., update
new = {"Grapes": 90, "Papaya": 120, "Jackfruit": 30}
fruits.update(new)
print(fruits)

