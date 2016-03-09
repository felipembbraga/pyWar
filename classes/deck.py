import collections

Card = collections.namedtuple('Card', ['place', 'figure'])


class Deck(object):
    places = ['joker', 'joker']
    figures = 'square triangle circle all'.split()

    def __init__(self):
        self._cards = [Card(p, self.figures[-1]) for p in self.places]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
