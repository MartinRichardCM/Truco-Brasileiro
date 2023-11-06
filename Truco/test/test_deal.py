import sys
sys.path.append('../')
from utils import *

if __name__ == "__main__":
    SUITS = ['Hearts', 'Diamonds']
    RANKS = ['2', '3','4','5']
    deck = Deck(SUITS,RANKS)
    deck.shuffle()
    deck.print_deck()
    player_1 = Player(1)
    player_1.add_card(deck.deal())
    player_1.print_hand()
    deck.print_deck()
    player_2 = Player(2)
    player_2.add_card(deck.deal())
    player_2.print_hand()
    deck.print_deck()