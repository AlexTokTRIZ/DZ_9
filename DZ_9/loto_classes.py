from random import randint

class Loto_card:

    def __init__(self):
        self.card=[]

    def init_card(self):
        self.card=[]
        while len(self.card)<15:
            r=randint(1,90)
            card_10 = list(map(lambda x: x // 10, self.card))
            if r not in self.card and card_10.count(r//10)<2:
                self.card.append(r)
        self.card.sort()
        self.card=list(map(lambda x: str(x), self.card))
        #return self.card

    def replace_num(self, num):
        for i in range(len(self.card)):
            self.card[i] = self.card[i] if self.card[i]!=num else "--"
        return self.card


if __name__ == '__main__':
    lotto=Loto_card()
    lotto.init_card()
    print(lotto.card)

