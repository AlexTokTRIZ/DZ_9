# ООП
# . 1. Класс - семейство объектов (Кошка)
# . 2. Свойства - характеристики сеймества объектов (Порода, Кол во лап, Цвет, Возраст, Длина хвоста)
# 3. Методы - действия которые могут делать кошки (Кусаться, Царапать, Ходить, Спать, ...)
# 4. Объект - конкретная Кошка "Муся" свойства (Сиамсая, 4 лапы, серый, 3, 30см)

class Bill:

    def __init__(self):
        self.money = 0
        self.history = []

    def add(self, count):
        """
        Добавить деньги на счет
        :param count:
        :return:
        """
        self.money += count

    def can_by(self, count):
        return count <= self.money

    def buy(self, count, name):
        """
        Покупка
        :param count:
        :param name:
        :return:
        """
        if self.can_by(count):
            # снимаем деньги
            self.money -= count
            self.history.append((name, count))
        else:

            raise Exception('Не хватает денег')
            # print('Денег недостаточно')


class SavingBill(Bill):

    def can_by(self, count):
        return False

    def buy(self, count, name):
        raise Exception('Нельзя снимать с накопительного счета')


if __name__ == '__main__':
    # Создание объекта класса Bill
    leo_bill = Bill()

    print(type(leo_bill))
    print(leo_bill.money)

    leo_bill.add(10)
    leo_bill.add(20)

    print(leo_bill.money)

    kate_bill = Bill()
    print(kate_bill.money)

    kate_bill.add(1)
    print(kate_bill.money)

    print('А у Leo осталось 30 т.к. это другой объект', leo_bill.money)

    bills = [leo_bill, kate_bill]

    for bill in bills:
        print(bill.money)

        bill.add(100)

        print(bill.money)

    bill = SavingBill()
    bill.add(10)