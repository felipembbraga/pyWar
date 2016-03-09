# -*- coding: utf-8 -*-

import unittest


class DiceTestCase(unittest.TestCase):

    def testSortDice(self):
        '''
        testar a classe dados
        '''

        # primeiramente, importamos a classe
        try:
            from classes.dice import Dice
        except ImportError, e:
            self.fail('Class doesn\'t exists.')

        # depois, instanciamos ela
        dice = Dice()
        # depois sortearemos ela
        self.assertIn(dice.sort(), range(1, 7), 'Dice sort error')


class DeckTestCase(unittest.TestCase):

    def testDeck(self):
        try:
            from classes.deck import Deck
        except ImportError, e:
            self.fail('Class doesn\'t exists.')

        deck = Deck()

        self.assertEqual(deck[1].place, 'joker', 'Carta errada')
if __name__ == '__main__':
    unittest.main()
