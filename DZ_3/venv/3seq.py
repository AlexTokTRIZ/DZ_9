import random

str_1 = input("Введите все элементы 1-го списка через запятую: ")
set_1 = set(str_1.split(','))

str_1 = input("Введите все элементы 2-го списка через запятую: ")
set_2 = set(str_1.split(','))

my_set=set_1-set_2
print('Результат: ', end='')
print(*list(my_set), sep=', ')