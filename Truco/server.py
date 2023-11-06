import socket
from _thread import *
from Back import *
from utils import *
from copy import *



######################################################
server = "0.0.0.0"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
######################################################
print(f"{server} is listening")


try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

# Define the initial card hands for each player
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', 'Jack', 'Queen', 'King', 'Ace']
VALUES_ORIGINAL = {'4': 1, '5': 2, '6': 3, '7': 4, 'Queen': 5, 'Jack': 6, 'King': 7, 'Ace': 8, '2': 9, '3': 10}
usernames = [0,0]
deck = Deck(SUITS,RANKS)
deck.shuffle()
cards_player1 = []
cards_player2 = []
action_players = [None,None]
manilla = []
cards_player1.append(deck.deal())
cards_player1.append(deck.deal())
cards_player1.append(deck.deal())
cards_player2.append(deck.deal())
cards_player2.append(deck.deal())
cards_player2.append(deck.deal())
manilla.append(deck.deal())
initial_hands = [[''.join(card) for card in cards_player1],[''.join(card) for card in cards_player2]]
for hand in initial_hands:
    hand.append('RedJoker')
initial_hands_copy = copy(initial_hands)
pre_manilla_combined = [''.join(card) for card in manilla]
pre_manilla = partition_sequence(pre_manilla_combined[0])[0]
manilla , NEW_VALUES = get_values(pre_manilla,VALUES_ORIGINAL)
currentPlayer = 0
connections = []
turn = 0
nbround = 1
scoreround = [0, 0]
party = [0, 0]
both_played = 1
truco = 0
Who_won = None
Who_trucoed = [0,0]
first_move = 0
first_game = 1
power = 1



def send_hand_and_message(player, message, prev_move="", nbround=1, round=[0, 0], party=[0, 0], additional_card=None):
    print(initial_hands)
    hand = initial_hands[player]
    conn = connections[player]

    if additional_card:
        additional_card_str = f"[{additional_card}]"
    else:
        additional_card_str = ""

    round_str = f"{round[0]},{round[1]}"
    party_str = f"{party[0]},{party[1]}"

    data_to_send = ",".join(hand) + ";" + message + ";" + prev_move + ";" + str(nbround) + ";" + round_str + ";" + party_str + ";" + additional_card_str
    conn.send(str.encode(data_to_send))



def threaded_client(conn, player):
    global turn, both_played, nbround, initial_hands, action_players, scoreround, party, Who_won, Who_trucoed, first_move, manilla, NEW_VALUES, pre_manilla_combined, first_game, power, truco, prev_move, usernames

    try:
        username = conn.recv(2048).decode()
        print(f"Player {player + 1} has set the username: {username}")
        # Acknowledge the username is set
        if player == 0:
            print(player)
            send_hand_and_message(player, "¡Apurate! Te estamos esperando...",nbround=nbround, additional_card = pre_manilla_combined)
            turn = 1
            usernames[0] = username
        else:
            print(player)
            usernames[1] = username
            send_hand_and_message(player, "Esperando mi oponente...",nbround=nbround, additional_card = pre_manilla_combined)

        while True:
            try:
                data = conn.recv(2048).decode()
                prev_move = data
                print(data)
                if not data:
                    print(f"Player {player + 1} disconnected")
                    break
                print(f"la manilla es {pre_manilla_combined}")
                print(f"Received from Player {player + 1}: {data}")
                data_betterformat = partition_sequence(f"{data}")
                other_player = 1 - player
                action_players[player] = data_betterformat
                if data_betterformat == ('Black', 'Joker'):
                    Who_trucoed[player] = 1
                    while True:
                        message = 'No sea un terrorista...'
                        send_hand_and_message(other_player,message, nbround=nbround, round=scoreround, party=party, additional_card=pre_manilla_combined)
                        data = conn.recv(2048).decode()
                        data_betterformat = partition_sequence(f"{data}")
                        power +=1
                        Who_trucoed[player] = 1
                        both_played = -1
                        if data_betterformat == ('Red', 'Joker'):
                            Who_trucoed[player] = 1
                            break
                        elif data_betterformat != ('Black', 'Joker'):
                            break
                if both_played == 1 and first_move and Who_won is not None:
                    Who_won = 1-Who_won
                first_move = 1
                if Who_trucoed[0]==1 and Who_trucoed[1] == 1:
                    action_players[0] = partition_sequence(f"{initial_hands[0][0]}")
                    action_players[1] = partition_sequence(f"{initial_hands[1][0]}")
                    truco = 1
                    Who_trucoed = [0,0]
                if both_played == -1 and nbround == 1:
                    winner = winner_round(manilla,nbround,action_players,NEW_VALUES)
                    #We wait for client's new input.
                    action_players = [None,None]
                    if winner[0]==-1:
                        nbround += 1
                        if winner[1]!=-1:
                            Who_won = winner[1]
                            scoreround[winner[1]] += 1
                    else:
                        nbround = 1
                        Who_won = winner[0]
                        party[winner[0]] += 1
                        first_game = 0
                elif both_played == -1 and nbround == 2:
                    winner = winner_round(manilla,nbround,action_players,NEW_VALUES)
                    action_players = [None,None]
                    if winner[0]==-1:
                        nbround += 1
                        if winner[1]!=-1:
                            scoreround[winner[1]] += 1
                            Who_won = winner[1]
                            if [i for i, item in enumerate(scoreround) if item >= 2]:
                                position = [i for i, item in enumerate(scoreround) if item >= 2]
                                nbround = 1
                                party[position[0]] += 1
                                first_game = 0
                                scoreround = [0,0]
                    else:
                        nbround = 1
                        Who_won = winner[0]
                        party[winner[0]] += 1
                        first_game = 0
                        scoreround = [0,0]
                elif both_played == -1 and nbround == 3 and not truco:
                    winner = winner_round(manilla,nbround,action_players,NEW_VALUES)
                    action_players = [None,None]
                    if winner[0]==-1:
                        if winner[1]!=-1:
                            nbround = 1
                            scoreround[winner[1]] += 1
                            if scoreround[0]>scoreround[1]:
                                party[0] += 1
                                first_game = 0
                                Who_won = 0
                            elif scoreround[0]<scoreround[1]:
                                Who_won = 1
                                party[1] += 1
                                first_game = 0
                        else:
                            if scoreround[0]>scoreround[1]:
                                Who_won = 0
                                party[0] += 1
                                first_game = 0
                            elif scoreround[0]<scoreround[1]:
                                Who_won = 0
                                party[1] += 1
                                first_game = 0
                    else:
                        Who_won = winner[0]
                        party[winner[0]] += 1
                        first_game = 0
                    nbround,scoreround = 1,[0,0]
                elif both_played == -1 and nbround == 3 and truco:
                    winner = winner_round(manilla,nbround,action_players,NEW_VALUES,truco)
                    action_players = [None,None]
                    if winner[0]==-1:
                        if winner[1]!=-1:
                            nbround = 1
                            party[winner[1]] += (3*power)
                            first_game = 0
                            truco = 0
                            Who_won = winner[1]
                            power = 1
                        else:
                            if scoreround[0]>scoreround[1]:
                                party[0] += 1
                                first_game = 0
                                Who_won = 0
                            elif scoreround[0]<scoreround[1]:
                                party[1] += 1
                                first_game = 0
                                Who_won = 1
                    else:
                        party[winner[0]] += 1
                        first_game = 0
                        Who_won = winner[0]
                    nbround,scoreround = 1,[0,0]
                    Who_trucoed = [0,0]
                if nbround == 3 and both_played == -1:
                    for hand in initial_hands:
                        hand.append('BlackJoker')
                played_card = data.strip()
                initial_hands[player].remove(played_card)
                if first_game and nbround == 1:
                    with open('/Users/richardmartin/Documents/Truco_test/results.txt', 'a') as file:
                        # Write data to the file
                        file.write(f"{usernames}\n")
                        file.write(f"{initial_hands_copy}\n")
                        file.write(f"{[0,0]}\n")
                if not first_game:
                    if nbround ==1 and both_played == -1:
                        deck = Deck(SUITS,RANKS)
                        deck.shuffle()
                        cards_player1 = []
                        cards_player2 = []
                        manilla = []
                        cards_player1.append(deck.deal())
                        cards_player1.append(deck.deal())
                        cards_player1.append(deck.deal())
                        cards_player2.append(deck.deal())
                        cards_player2.append(deck.deal())
                        cards_player2.append(deck.deal())
                        manilla.append(deck.deal())
                        initial_hands = [[''.join(card) for card in cards_player1],[''.join(card) for card in cards_player2]]
                        pre_manilla_combined = [''.join(card) for card in manilla]
                        pre_manilla = partition_sequence(pre_manilla_combined[0])[0]
                        manilla , NEW_VALUES = get_values(pre_manilla,VALUES_ORIGINAL)
                        for hand in initial_hands:
                            hand.append('RedJoker')
                        with open('/Users/richardmartin/Documents/Truco_test/results.txt', 'a') as file:
                            # Write data to the file
                            file.write(f"{initial_hands}\n")
                            file.write(f"{party}\n")
                if Who_won == player:
                    turn = other_player
                    both_played = (both_played)*(-1)

                    send_hand_and_message(other_player, "Esperando mi oponente...", prev_move = f"{data}", nbround=nbround,  round=scoreround, party=party, additional_card = pre_manilla_combined)
                    send_hand_and_message(player, "¡Apurate! Te estamos esperando...", prev_move = f"{data}", nbround=nbround, round=scoreround, party=party, additional_card = pre_manilla_combined)
                else:
                    turn = player
                    both_played = (both_played)*(-1)
                    send_hand_and_message(player, "Esperando mi oponente...", prev_move = f"{data}", nbround=nbround,  round=scoreround, party=party, additional_card = pre_manilla_combined)
                    send_hand_and_message(other_player, "¡Apurate! Te estamos esperando...", prev_move = f"{data}", nbround=nbround,  round=scoreround, party=party, additional_card = pre_manilla_combined)

            except ConnectionResetError as e:
                print(f"Player {player + 1} disconnected unexpectedly: {e}")
                break
    except Exception as e:
            print(f"Player {player + 1} encountered an error: {str(e)}")
    print(f"Player {player + 1} lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print(f"Connected to Player {currentPlayer + 1}:", addr)
    connections.append(conn)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1