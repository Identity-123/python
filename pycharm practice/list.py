marks = [3, 4, 5, 8, 90,'rajan']
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-3])
if 3 in marks:
    print('yes')
else:
    print("no")
if 'an' in "rajan":
    print('yes')
print(marks[:])
print(marks[1:5])
print(marks[2:-2])
print(marks[0:5:2])#jump index


#list compression
lst = [i*i for i in range(9)]
print(lst)
