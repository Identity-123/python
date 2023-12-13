pet = ['dog', 'cat', 'parrot', 'mouse', 'rabbit', 'dog']
animal = ['lion', 'tiger', 'rhino', 'giraffe']

def count():
    # count
    cnt = pet.count('dog')
    print(cnt)


def index():
    # index : it is used to find the position of any given data in list
    r = pet.index('cat')
    print(r)


def append():
    # append is used for adding data at last of the list
    s = pet.append('cow')
    print(s)


def extend():
    pet.extend(animal)
    print(pet)


extend()