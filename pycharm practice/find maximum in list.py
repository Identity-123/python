marks = [20, 50, 100, 85, 70, 69]
highest = marks[0]
for i in marks:
    if i > highest:
        highest = i
print("highest is =", highest)

#alternative
x = max(marks)
print(x)