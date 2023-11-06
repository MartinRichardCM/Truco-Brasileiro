import sys
import os
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
    player_1.add_card(deck.deal())
    player_1.add_card(deck.deal())
    deck.print_deck()
    print(player_1.status())
    print([''.join(card) for card in player_1.status()])
    player_1.decision(player_1.status()[-1])
    print(player_1.status())
    print([''.join(card) for card in player_1.status()])
    player_1.decision(player_1.status()[0])
    print(player_1.status())
    print([''.join(card) for card in player_1.status()])