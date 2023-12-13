set_1 = {1, 2, 3, 3, 4, 5, 5, 2}
# set will remove the duplicate and only print or have unique value

set_1.add(9)
set_1.add(9)
# adding the same number or string in sets is useless because it will take one value and ignore all values

print(set_1)

# update() method to update sets
s = 'Rajan'
# string has no update attribute so,
set_1.update(s)
print(set_1)

# Deleting an element
# 1. pop

set_1.pop()
print(set_1)
# pop will remove any value from sets randomly

# 2.remove method
set_1.remove("R")
print(set_1)

