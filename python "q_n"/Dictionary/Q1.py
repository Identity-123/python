list1 = list(map(int, input("enter the first list").split()))
list2 = list(map(int, input("enter the second list").split()))
dict_1 = dict(zip(list1, list2))
print(dict_1)
