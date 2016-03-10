import collections
from string import strip

Continent = collections.namedtuple('Continent', ['id', 'name', 'extra_troops', 'color'])
Local = collections.namedtuple('Local', ['id', 'name', 'picture', 'continent', 'link'])


def readFile(filename):
    continents = []
    locais = []
    with open(filename, 'r') as f:
        for row in f:
            obj = map(strip, row.split('|'))
            if(len(obj) < 2):
                continue
            if obj[1] == 'c':
                continents.append(Continent(*obj[:1] + obj[2:]))
            if obj[1] == 'l':
                continent = next((c for c in continents if c.id == obj[4]))
                local = obj[:1] + obj[2:-2] + [continent] + [obj[-1].split()]
                locais.append(Local(*local))
    return locais
