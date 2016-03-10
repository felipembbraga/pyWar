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
            from classes.game import Game
        except ImportError, e:
            self.fail('Class doesn\'t exists.')

        game= Game()
        self.assertEqual(len(game.deck), 44, 'Carta errada')
if __name__ == '__main__':
    unittest.main()
