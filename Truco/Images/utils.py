from Back import *



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