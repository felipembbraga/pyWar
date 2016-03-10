from readTerritories import readFile
from deck import Deck
import os

LOCAL = lambda x: os.path.join(os.path.dirname(__file__), x)

class Game():

    def __init__(self):
        self.__locais = readFile(LOCAL('territories.txt'))
        self.__deck = Deck(self.__locais)

    @property
    def deck(self):
        return self.__deck