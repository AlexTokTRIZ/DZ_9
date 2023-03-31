def print_card(card):
    print('-' * 15)
    for j in range(3):
        for i in range(5):
            print(card[i + j * 5], end=' ')
        print('\n', '-' * 15)