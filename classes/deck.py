import collections

Card = collections.namedtuple('Card', ['place', 'figure'])

class Deck(object):

    def __init__(self, locais):
        self.__cards = [Card(local.name, local.picture) for local in locais] + 2*[Card('joker', 'all')]

    @property
    def cards(self):
        return self.__cards

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]
