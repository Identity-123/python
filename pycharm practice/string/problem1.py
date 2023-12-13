# YOUR CODE GOES H
c = 0
sent1 = input('=')
sent2 = input('= ')
x = ['use', 'process', 'create', 'better', 'analysis', 'in', 'it', 'further', 'and', 'we', 'data', 'interpreted', 'to',
     'collected', 'more', 'be', 'and', 'data', 'passively', 'will']
sent3 = sent1 + sent2
sent4 = sent3.split()
for i in sent4:
    if i in x:
        c = c + 1
def hello():

print(c)
 
x = ['new', 'old', 'future', 'past']
y = '''
i want new mobile because old one is not working. 
For buying new mobile  i more money than i spent to buy that old mobile in past .
In future , the price of new mobile is also going to drop .
'''

yz = y.split()
# r = y.count('new')
# print(r)
# s = y.count('old')
# print(s)
# t = y.count('future')
# print(t)
# u = y.count('past')
# print(u)
# print(r + s + t + u)
c = 0
for i in yz:
    if i in x:
        c = c+1
        print(i)
print(c)
