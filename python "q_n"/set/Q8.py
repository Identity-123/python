set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
common = set1 & set2
set1.update(set2)

newset = set1 - common
print(newset)
