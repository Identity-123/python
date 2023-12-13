# finding vowel letter from the given string
def vowel():
    text = 'The quick brown fox jumps over the very lazy dog'
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            return i


def palindrome():
    pal = input('enter a string = ')
    if pal == pal[::-1]:
        print('is palindrome')
    else:
        print('nota palindrome')


palindrome()
