#-*- coding: utf-8 -*-
from random import choice

class Dice(object):

    def __init__(self):
        self.values = range(1,7)
    def sort(self):
        return choice(self.values)
