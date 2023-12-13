greeting = 'hello'
name = 'rajan'
message = f'{greeting}, {name.upper()}.welcome'
print(message)


# count string and print percentages
def count():
    text = input('enter a text')
    letter = input('enter a letter to count')
    x = text.count(letter)
    print(x)
    z = int(((x / len(text)) * 100))
    print(z)


count()
