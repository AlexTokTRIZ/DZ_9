import random
from loto_classes import Loto_card
from Loto_func import*

# начало
#variant=int(input('Выберите вариант игры: (1 - чел./комп.), 2 - чел./чел., 3 - комп/комп'))
#variant=variant if variant>=2 and variant <=3 else 1
card_k=Loto_card()
card_k.init_card()

# печать карточки
card_m=Loto_card()
card_m.init_card()
print_card(card_k.card)
print_card(card_m.card)
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
            card_k.replace_num(b)
            if card_k.card.count('--')==15:
                winner='card_k'
                print('Winner - Komp!')
        print('Карточка компьютера')
        print_card(card_k.card)
        print('Карточка человека')
        print_card(card_m.card)
        dell=input('Зачеркнуть? 1-Да/2-Нет')
        if dell=='1':
            if b in card_m.card:
                card_m.replace_num(b)
                if card_m.card.count('--') == 15:
                    winner = 'card_m'
                    print('Winner - Man!')
            else:
                winner='card_k'
                print('Winner - Komp!')
        else:
            if b in card_m.card:
                winner='card_k'
                print('Winner - Komp!')



