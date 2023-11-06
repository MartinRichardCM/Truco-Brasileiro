import sys
import os
sys.path.append('../')
from Back import *
from utils import *


if __name__ == "__main__":
    moves = [('2', 'Hearts'), ('King', 'Spades')]
    nbround = 1
    pre_manilla_combined = ['JackHearts']
    VALUES_ORIGINAL = {'4': 1, '5': 2, '6': 3, '7': 4, 'Queen': 5, 'Jack': 6, 'King': 7, 'Ace': 8, '2': 9, '3': 10}
    pre_manilla = partition_sequence(pre_manilla_combined[0])[0]
    manilla , NEW_VALUES = get_values(pre_manilla,VALUES_ORIGINAL)
    print("One player does not want to play the game:")
    moves = [('Red', 'Joker'), ('Queen', 'Spades')]
    print("Should output that player 2 won the party since the opponent doesnot want to play, thus giving us (party_winner,round_winner,party_winner_truco) =(0, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('Queen', 'Spades'),('Red', 'Joker')]
    print("Should output that player 2 won the party since the opponent doesnot want to play, thus giving us (party_winner,round_winner,party_winner_truco) =(1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("Both players do not want to play the game:")
    moves = [('Red', 'Joker'), ('Red', 'Joker')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES)) 
    print("\n")
    print("With none of the players having the manilla:")
    moves = [('2', 'Hearts'), ('Queen', 'Spades')]
    print("should output that player 1 won round 1 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('Queen', 'Spades'),('2', 'Hearts')]
    print("should output that player 2 won round 1 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("With none of the players having the manilla but they have the same rank:")
    moves = [('2', 'Hearts'), ('2', 'Diamonds')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('2', 'Diamonds'),('2', 'Hearts')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("Let us have another test with none of the players having the manilla:")
    moves = [('Ace', 'Diamonds'), ('7', 'Clubs')]
    print("should output that player 1 won round 1 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('7', 'Clubs'),('Ace', 'Diamonds')]
    print("should output that player 2 won round 1 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")    
    print("With one player having the manilla:")
    moves = [('2', 'Hearts'), ('King', 'Spades')]
    print("should output that player 2 won round 1 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('King', 'Spades'),('2', 'Hearts')]
    print("should output that player 1 won round 1 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("With two players having the manilla:")
    moves = [('King', 'Clubs'), ('King', 'Spades')]
    print("should output that player 1 won round 1 since he has the better manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('King', 'Spades'),('King', 'Clubs')]
    print("should output that player 1 won round 1 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("\n")
    print("\n")
    print("Let us try all the same but with nb_round=3, let us note that we should have the exact same behavior.")
    nbround = 3


    print("One player does not want to play the game:")
    moves = [('Red', 'Joker'), ('Queen', 'Spades')]
    print("Should output that player 2 won the party since the opponent doesnot want to play, thus giving us (party_winner,round_winner,party_winner_truco) =(0, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('Queen', 'Spades'),('Red', 'Joker')]
    print("Should output that player 2 won the party since the opponent doesnot want to play, thus giving us (party_winner,round_winner,party_winner_truco) =(1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("Both players do not want to play the game:")
    moves = [('Red', 'Joker'), ('Red', 'Joker')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES)) 
    print("\n")
    print("With none of the players having the manilla:")
    moves = [('2', 'Hearts'), ('Queen', 'Spades')]
    print("should output that player 1 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('Queen', 'Spades'),('2', 'Hearts')]
    print("should output that player 2 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("With none of the players having the manilla but they have the same rank:")
    moves = [('2', 'Hearts'), ('2', 'Diamonds')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('2', 'Diamonds'),('2', 'Hearts')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("Let us have another test with none of the players having the manilla:")
    moves = [('Ace', 'Diamonds'), ('7', 'Clubs')]
    print("should output that player 1 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('7', 'Clubs'),('Ace', 'Diamonds')]
    print("should output that player 2 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")    
    print("With one player having the manilla:")
    moves = [('2', 'Hearts'), ('King', 'Spades')]
    print("should output that player 2 won round 3 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('King', 'Spades'),('2', 'Hearts')]
    print("should output that player 1 won round 3 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("\n")
    print("With two players having the manilla:")
    moves = [('King', 'Clubs'), ('King', 'Spades')]
    print("should output that player 1 won round 3 since he has the better manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 0, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))
    print("Let us play with the same hands but reversing the players")
    moves = [('King', 'Spades'),('King', 'Clubs')]
    print("should output that player 1 won round 3 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, 1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES))

    print("\n")
    print("\n")
    print("\n")
    print("Finally, let us try with truco.")


    print("One player does not want to play the game:")
    moves = [('Red', 'Joker'), ('Queen', 'Spades')]
    print("Should output that player 2 won the party since the opponent doesnot want to play, thus giving us (party_winner,round_winner,party_winner_truco) =(0, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("Let us play with the same hands but reversing the players")
    moves = [('Queen', 'Spades'),('Red', 'Joker')]
    print("Should output that player 2 won the party since the opponent doesnot want to play, thus giving us (party_winner,round_winner,party_winner_truco) =(1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("\n")
    print("Both players do not want to play the game:")
    moves = [('Red', 'Joker'), ('Red', 'Joker')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1)) 
    print("\n")
    print("With none of the players having the manilla:")
    moves = [('2', 'Hearts'), ('Queen', 'Spades')]
    print("should output that player 1 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 0) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("Let us play with the same hands but reversing the players")
    moves = [('Queen', 'Spades'),('2', 'Hearts')]
    print("should output that player 2 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("\n")
    print("With none of the players having the manilla but they have the same rank:")
    moves = [('2', 'Hearts'), ('2', 'Diamonds')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("Let us play with the same hands but reversing the players")
    moves = [('2', 'Diamonds'),('2', 'Hearts')]
    print("Should output no one won anything, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, -1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("\n")
    print("Let us have another test with none of the players having the manilla:")
    moves = [('Ace', 'Diamonds'), ('7', 'Clubs')]
    print("should output that player 1 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 0) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("Let us play with the same hands but reversing the players")
    moves = [('7', 'Clubs'),('Ace', 'Diamonds')]
    print("should output that player 2 won round 3 since he has the better card, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("\n")    
    print("With one player having the manilla:")
    moves = [('2', 'Hearts'), ('King', 'Spades')]
    print("should output that player 2 won round 3 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("Let us play with the same hands but reversing the players")
    moves = [('King', 'Spades'),('2', 'Hearts')]
    print("should output that player 1 won round 3 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 0) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("\n")
    print("With two players having the manilla:")
    moves = [('King', 'Clubs'), ('King', 'Spades')]
    print("should output that player 1 won round 3 since he has the better manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 0) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))
    print("Let us play with the same hands but reversing the players")
    moves = [('King', 'Spades'),('King', 'Clubs')]
    print("should output that player 1 won round 3 since he has the manilla, thus giving us (party_winner,round_winner,party_winner_truco) =(-1, -1, 1) ", winner_round(manilla,nbround,moves,NEW_VALUES,1))