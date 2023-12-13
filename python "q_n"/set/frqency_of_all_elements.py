import ast

try:

    user_input = input('enter the number')
    tup_input = tuple(map(eval, user_input.split(' ')))
    unique_elements = set(tup_input)
    for i in unique_elements:
        frequency = tup_input.count(i)
        print(f'{i}:{frequency}')
except (ValueError, SyntaxError) as e:
    print(f'error: {e}')
