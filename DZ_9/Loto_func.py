def cross(b, card, des):
    winner = ''
    if des == '1':
        if b in card:
            card.replace_num(b)
            if card.card.count('--') == 15:
                winner = 'Man'
        else:
            winner = 'Komp'
    else:
        if b in card.card:
            winner = 'Komp'

    return winner
