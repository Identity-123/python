def intro(name, age, hobby):
    return name, age, hobby


a, b, c = intro("rajan", 20, "gaming")
# above variable are writen in the form of tuple

print(a, b, c)
x = intro("rajan", 20, "gaming")
print(x, type(x))
