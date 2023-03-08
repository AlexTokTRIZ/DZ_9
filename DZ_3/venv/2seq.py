import random

razdel = (',', ';', '/')
razdel_txt = ('запятую', 'точку с запятой', 'слэш')
r = random.randint(0, len(razdel))
razdel_str = razdel_txt[r]
str_1 = input("Введите все элементы списка (целые числа), используя " + razdel_str + " : ")
my_list = str_1.split(razdel[r])
my_set = set(my_list)
print('Вот Ваш список: ', end='')
print(*my_set, sep=', ')
