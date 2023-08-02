from enum import Enum
import random

class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    def __init__(self, suit, face):
        self.suit,self.face = suit, face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suit.value]}{faces[self.face]}'
    
    def __lt__(self, other):
        return self.face < other.face
  
class Poker:
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        self.current = 0
    
    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)
    
    def deal(self):
        card = self.cards[self.current]
        self.current+=1
        return card
    
    @property
    def has_next(self):
        return self.current < len(self.cards)

class Person:
    def __init__(self, name):
        self.name = name
        self.card = []

    def get_one(self, card):
        self.card.append(card)
    
    def arrange(self):
        self.card.sort()

poker = Poker()
poker.shuffle()
persons = [Person('东邪'), Person('西毒'), Person('南帝'), Person('北丐')]

for _ in range(13):
    for player in persons:
        player.get_one(poker.deal())

for player in persons:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(f'{player.card}')