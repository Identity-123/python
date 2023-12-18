def even(li):
    for i in li:
        if i % 2 == 0:
            new_list.append(i)

    print(new_list)


# I am taking input by using a map and split function
lst = list(map(int, input('enter the value').split(' ')))

new_list = []

even(lst)
