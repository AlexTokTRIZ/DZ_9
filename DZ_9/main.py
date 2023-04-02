import random
from loto_classes import Loto_card
from Loto_func import*


def print_card(card):
    print('-' * 15)
    for j in range(3):
        for i in range(5):
            print(card[i + j * 5], end=' ')
        print('\n', '-' * 15)

# начало
#variant=int(input('Выберите вариант игры: (1 - чел./комп.), 2 - чел./чел., 3 - комп/комп'))
#variant=variant if variant>=2 and variant <=3 else 1
card_k=Loto_card()
card_k.init_card()

card_m=Loto_card()
card_m.init_card()

# игра!
sumka=[str(i) for i in range(1,91)]
otval=[]
winner=''
while not winner:
    b=random.choice(sumka)
    sumka.remove(b)
    if b not in otval:
        print('Выпал бочонок № ', b, winner)
        otval.append(b)
        if b in card_k.card:
            winner = cross(b, card_k, '1')

        print('Карточка компьютера')
        print_card(card_k.card)
        if winner=='':
            if b in card_m.card:
                print('Карточка человека')
                print_card(card_m.card)
                des=input('Зачеркнуть? 1-Да/2-Нет')

                winner=cross(b,card_m,des)
                if winner!='':
                    print('Игра окончена, выиграл ', winner)




