import sys
sys.path.append('../')
from utils import *

if __name__ == "__main__":
    SUITS = ['Hearts', 'Diamonds']
    RANKS = ['2', '3']

    deck = Deck(SUITS,RANKS)
    deck.print_deck()
    deck.shuffle()
    deck.print_deck()
    deck = Deck(SUITS,RANKS)
    deck.print_deck()
    deck.shuffle()
    deck.print_deck()
