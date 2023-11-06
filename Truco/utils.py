from Back import *
import re


def find_key_by_value(dictionary, value):
    return next((key for key, val in dictionary.items() if val == value), None)

def get_values(manilla,VALUES):
    #manilla=(rank)
    #SUITS,RANKS = Deck composition.
    #VALUES = original values.
    VALUES_copy = VALUES.copy()
    card_value = VALUES[f'{manilla}']
    if card_value != 10:
        new_manilla = find_key_by_value(VALUES,card_value+1)
    else:
        new_manilla = '4'
    for card, value in VALUES_copy.items():
        if value > card_value:
            VALUES_copy[f'{card}'] = VALUES_copy[f'{card}']-1
    del VALUES_copy[f'{new_manilla}']
    VALUES_copy[f'{new_manilla}','Diamonds'] = 10
    VALUES_copy[f'{new_manilla}','Spades'] = 11
    VALUES_copy[f'{new_manilla}','Hearts'] = 12
    VALUES_copy[f'{new_manilla}','Clubs'] = 13
    return new_manilla , VALUES_copy

def round(VALUES,decision_player1,decision_player2,manilla):
    value_player1,value_player2 = 0,0
    if decision_player1[0] != manilla and decision_player2[0] != manilla:
        value_player1 = VALUES[decision_player1[0]]
        value_player2 = VALUES[decision_player2[0]]
    elif decision_player1[0] == manilla and decision_player2[0] != manilla:
        value_player1 = VALUES[decision_player1]
        value_player2 = VALUES[decision_player2[0]]
    elif decision_player1[0] != manilla and decision_player2[0] == manilla:
        value_player1 = VALUES[decision_player1[0]]
        value_player2 = VALUES[decision_player2]
    elif decision_player1[0] == manilla and decision_player2[0] == manilla:
        value_player1 = VALUES[decision_player1]
        value_player2 = VALUES[decision_player2]
    if value_player1>value_player2:
        return ((1,0))
    elif value_player1==value_player2:
        return ((0,0))
    else:
        return ((0,1))

def set_up_hands():
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', 'Jack', 'Queen', 'King', 'Ace']
    deck = Deck(SUITS,RANKS)
    deck.shuffle()
    player_1 = Player(1)
    player_2 = Player(1)
    player_1.add_card(deck.deal())
    player_2.add_card(deck.deal())
    player_1.add_card(deck.deal())
    player_2.add_card(deck.deal())
    player_1.add_card(deck.deal())
    player_2.add_card(deck.deal())
    manilla_precursor = deck.deal()[0]
    return player_1,player_2,manilla_precursor

def partition_sequence(s):
    # Use regex to find the rank and suit
    match = re.match(r'(\d+|[A-Za-z]+)([A-Z][a-z]+)', s)
    
    if match:
        rank = match.group(1)
        suit = match.group(2)
        return rank, suit
    else:
        return None

def winner_round(manilla,nbround,moves,values,truco=0):
    p1 = moves[0]
    p2 = moves[1]
    #p1 = ('Rank','Suit') or ('Red', 'Joker')
    winner = (-1,-1,-1)
    #winner = (party_winner,round_winner,party_winner_truco)
    if p1 == ('Red', 'Joker') and p2 == ('Red', 'Joker'):
        winner = (-1,-1,-1)
    elif p2 == ('Red', 'Joker'):
        winner = (0,-1,-1)
    elif p1 == ('Red', 'Joker'):
        winner = (1,-1,-1)
    elif nbround < 3:
        card1 = p1
        card2 = p2
        if card1[0] == manilla and card2[0] == manilla:
            value_player1 = values[card1]
            value_player2 = values[card2]
            if value_player1>value_player2:
                winner = (-1,0,-1)
            else:
                winner = (-1,1,-1)
        elif card1[0] == manilla:
            winner = (-1,0,-1)
        elif card2[0] == manilla:
            winner = (-1,1,-1)
        else:
            value_player1 = values[card1[0]]
            value_player2 = values[card2[0]]
            if value_player1>value_player2:
                winner = (-1,0,-1)
            elif value_player1==value_player2:
                winner = (-1,-1,-1)
            else:
                winner = (-1,1,-1)
    elif nbround == 3:
        card1 = p1
        card2 = p2
        if truco:
            if card1[0] == manilla and card2[0] == manilla:
                value_player1 = values[card1]
                value_player2 = values[card2]
                if value_player1>value_player2:
                    winner = (-1,0,-1)
                else:
                    winner = (-1,1,-1)
            elif card1[0] == manilla:
                winner = (-1,0,-1)
            elif card2[0] == manilla:
                winner = (-1,1,-1)
            else:
                value_player1 = values[card1[0]]
                value_player2 = values[card2[0]]
                if value_player1>value_player2:
                    winner = (-1,0,-1)
                elif value_player1 == value_player2:
                    winner = (-1,-1,-1)
                else:
                    winner = (-1,1,-1)
        else:
            if card1[0] == manilla and card2[0] == manilla:
                value_player1 = values[card1]
                value_player2 = values[card2]
                if value_player1>value_player2:
                    winner = (-1,0,-1)
                else:
                    winner = (-1,1,-1)
            elif card1[0] == manilla:
                winner = (-1,0,-1)
            elif card2[0] == manilla:
                winner = (-1,1,-1)
            else:
                value_player1 = values[card1[0]]
                value_player2 = values[card2[0]]
                if value_player1>value_player2:
                    winner = (-1,0,-1)
                elif value_player1==value_player2:
                    winner = (-1,-1,-1)
                else:
                    winner = (-1,1,-1)
    return winner