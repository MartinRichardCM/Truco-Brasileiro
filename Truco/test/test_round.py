import sys
sys.path.append('../')
from utils import *

if __name__ == "__main__":
    VALUES_ORIGINAL = {'4': 1, '5': 2, '6': 3, '7': 4, 'Queen': 5, 'Jack': 6, 'King': 7, 'Ace': 8, '2': 9, '3': 10}
    manilla_precursor = 'Jack'
    new_manilla , NEW_VALUES = get_values(manilla_precursor,VALUES_ORIGINAL)
    print(new_manilla)
    decision_player1 = ('5', 'Diamonds')
    decision_player2 = ('Jack', 'Diamonds')
    print(decision_player1,decision_player2)
    print(round(NEW_VALUES,decision_player1,decision_player2,new_manilla))
    decision_player1 = ('King', 'Diamonds')
    decision_player2 = ('Jack', 'Diamonds')
    print(decision_player1,decision_player2)
    print(round(NEW_VALUES,decision_player1,decision_player2,new_manilla))
    decision_player1 = ('Jack', 'Clubs')
    decision_player2 = ('Jack', 'Diamonds')
    print(decision_player1,decision_player2)
    print(round(NEW_VALUES,decision_player1,decision_player2,new_manilla))
    decision_player1 = ('King', 'Diamonds')
    decision_player2 = ('King', 'Clubs')
    print(decision_player1,decision_player2)
    print(round(NEW_VALUES,decision_player1,decision_player2,new_manilla))