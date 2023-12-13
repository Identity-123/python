c = 0
text = input('enter a text')
letter = input('enter a letter to count')
for i in text:
    print(i)

    if i == letter:
        c = c + 1
        
print(c)
x = ((c / len(text)) * 100)
print(x)
