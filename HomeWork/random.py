# def strip_string(b_function):
#     def wrapper():
#         func = b_function();
#         strip_string = func.strip('-')
#         return strip_string
#     return wrapper

# def uppercase_decorator(some_function):
#     def wrapper():
#         func = some_function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
 
# @strip_string
# @uppercase_decorator
# def cli_code():
#     print('The Florida router cli code is', end = '')
#     return '---tpaflxacg19---'
# print(cli_code())

# letter_grades = ['A', 'B+', 'B', 'C']
# grades = [95, 88, 85, 75]
# print(f'The original list {letter_grades}')
# print(f'The zipped tuples {list(zip(letter_grades, grades))}')
# print(f'Next is a map-lambda version')
# print(list(map(lambda *a: a, letter_grades, grades)))

# cli_names = ['flxa99443oc', 'gaxb32443oc', 'caxo99323oc', 'flxa11443ds']
# print(list(filter(lambda x : x[0].upper() in 'FC', cli_names)))

# print([(x, y) for x in ['a', 'b', 'c'] for y in ['first', 'b', '3'] if x != y])

# print([i*-1for i in[7,5,-4,6]if i<0])

import sys
a = [x for x in range(1000000)]
b = (x for x in range(1000000))
print(f'list comp byte size is {sys.getsizeof(a)}')
print(f'generator expression byte size is {sys.getsizeof(b)}')
