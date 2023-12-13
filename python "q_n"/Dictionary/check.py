fruits = {
    "Mango": 100,
    "Banana": 40,
    "kiwi": 400,
    "Guava": 270
}

find = input("what you want to find ")

if find in fruits:
    print(f"Item found:{fruits[find]}")
else:
    print(find, "not fount")
