# дата рождения Пушкина - June 6, 1799
year_pushkin = input("Введите год рождения А.С.Пушкина: ")
if year_pushkin == '1799':
    day_pushkin = input("Введите день рождения А.С.Пушкина в формате 00.00 (день.месяц): ")
    if day_pushkin == '6.6' or day_pushkin == '06.06' or day_pushkin == '06.6' or day_pushkin == '6.06':
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год")
