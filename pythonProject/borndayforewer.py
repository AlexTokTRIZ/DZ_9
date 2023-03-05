# дата рождения Пушкина - June 6, 1799
year_pushkin, day_pushkin = '',''
while year_pushkin != '1799':
    year_pushkin = input("Введите год рождения А.С.Пушкина: ")
    if year_pushkin == '1799':
        while day_pushkin != '6':
            day_pushkin = input("Введите день (число) рождения А.С.Пушкина: ")
            if day_pushkin == '6':
                print("Верно")
            else:
                print("Неверный день рождения")
    else:
            print("Неверный год")