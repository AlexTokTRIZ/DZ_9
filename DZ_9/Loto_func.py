def print_card(card):
    print('-' * 15)
    for j in range(3):
        for i in range(5):
            print(card[i + j * 5], end=' ')
        print('\n', '-' * 15)


def cross(b, card, des):
    winner = ''
    if des == '1':
        if b in card.card:
            card.replace_num(b)
            if card.card.count('--') == 15:
                winner = 'Man'
        else:
            winner = 'Komp'
    else:
        if b in card.card:
            winner = 'Komp'

    return winner
