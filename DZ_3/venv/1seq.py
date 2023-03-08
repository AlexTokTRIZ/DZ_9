list_num=0
while list_num >= 5 or list_num <10:
    list_num=int(input("Введите количество элементов списка (от 1 до ): "))
my_list=[]
for i in range(list_num):
    text='Введите '+ str(i+1) + ' элемент списка: '
    my_list.append(int(input(text)))
my_list.sort()
print('Вот Ваш список: ', my_list)