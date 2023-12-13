# Challenge:

# Given a list of population sensus done by Gol. You need to Find the total population.
# Each element in the list represents total members in a family
L = [4, 6, 5,  8, 9, 3, 2, 4, 5, 4, 3, 2, 3, 4]
add = 0
for i in L:
    add += i
print(f'total population ={add}')
