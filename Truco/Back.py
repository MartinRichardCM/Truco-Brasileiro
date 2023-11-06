import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def as_tuple(self):
        return (self.rank, self.suit)

# Deck class
class Deck:
    def __init__(self,suits,ranks):
        self.deck = []
        self.suits = suits
        self.ranks = ranks
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card.as_tuple())

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
    def print_deck(self):
        print(self.deck)

# Hand class
class Player:
    def __init__(self,identity=None):
        self.cards = []
        self.id = identity

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

    def print_hand(self):
        print(self.cards)
    
    def decision(self,decision):
        self.cards.remove(decision)
    
    def status(self):
        return self.cards