from loto_classes import*
import unittest

class TestLoto(unittest.TestCase):
    def setUp(self):
        #print('Я выполняюсь до каждого теста')
        self.card=Loto_card()
    #    self.card.init_card()

    #def tearDown(self):
    #    print('Я выполняюсь после каждого теста')
    #    del self.bill

    def test_init(self):
        self.assertEqual(self.card.card, [])
        #self.assertFalse(self.bill.history)
    def test_init_card(self):
        self.card.init_card()
        self.assertEqual(len(self.card.card),15)
        self.assertLess(int(self.card.card[0]),int(self.card.card[14]))

    def test_replace_num(self):
        self.card.card=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
        self.assertEqual(self.card.replace_num('7')[6],'--')


if __name__ == '__main__':
    unittest.main()





