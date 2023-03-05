great_mans = {"А.С.Пушкина": "1799", "М.Ю.Лермонтова": "1814", "Н.А.Некрасова": "1821",
              "Л.Н.Толстого": "1828", "А.П.Чехова": "1860"}
play = True
while play:
    good = 0
    numbers = len(great_mans)
    print('Викторина! Хорошо ли Вы знаете года рождения знаменитостей?')
    for i in great_mans.keys():
        year_gm = input("Введите год рождения " + i + ': ')
        if year_gm == great_mans.get(i):
            good += 1
    print("Количество правильных ответов:", good)
    print("Количество ошибок:", numbers - good)
    print("Процент правильных ответов:", good * 100 / numbers)
    print("Процент неравильных ответов:", 100 - good * 100 / numbers)

    if input("Хотите начать игру сначала (1-Да,0-Нет)?: ") == "1":
        play = True
    else:
        play = False