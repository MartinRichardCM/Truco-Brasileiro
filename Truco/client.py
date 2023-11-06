import pygame
import sys
import socket
import os
import threading



######################################################
server = socket.gethostbyname(socket.gethostname())
port = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
######################################################


current_directory = os.getcwd()
# Initialize Pygame
pygame.init()
image_above_buttons,Previous_move = None,None
# Define constants for screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
FONT_SIZE = 24
FONT_COLOR = (0, 0, 0) 
font = pygame.font.Font(None, FONT_SIZE)
RENDER_TEXT = font.render("Manilla:", True, FONT_COLOR)
WHITE = (255, 255, 255)
additional_text_party1 = font.render("Partida:", True, FONT_COLOR)
SHOW_TEXT = True
additional_text_round1 = font.render("Rondo:", True, FONT_COLOR)
Last_Card = font.render("Ultima carta:", True, FONT_COLOR)
# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jefa del mundo.")
player2_buttons,player2_cards = [],[] 
# Define the dimensions for the card images and buttons
CARD_WIDTH, CARD_HEIGHT = 100, 150
party = (0,0)
round = (0,0)
message = ""
# Create buttons for Player 2
# Create a socket for communication with the server
client.connect((server, port))
def receive_data():
    while True:
        data = client.recv(2048).decode()
        if not data:
            break
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, data=data))

network_thread = threading.Thread(target=receive_data)
network_thread.daemon = True  # Allow the thread to exit when the main program ends
network_thread.start()
# Function to update the card images and buttons based on the received hand data
SPACING = 10
Y_POSITION = SCREEN_HEIGHT - CARD_HEIGHT - 20
PADDING = 20

def initialize_buttons(hand_size, card_width, card_height):
    buttons = []
    total_width = hand_size * (card_width + SPACING) - SPACING
    initial_x = (SCREEN_WIDTH - total_width) / 2
    y = SCREEN_HEIGHT - card_height - PADDING  # Set the Y position to the bottom
    for i in range(hand_size):
        x = initial_x + i * (card_width + SPACING)
        button = pygame.Rect(x, y, card_width, card_height)
        buttons.append(button)
    return buttons
def load_card_images(hand,additional_card,additional_card2):
    card_images = []
    for card in hand:
        try:
            print(card,f"Images/{card}.png")
            image = pygame.image.load(f"Images/{card}.png")
            image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
            card_images.append(image)
        except pygame.error as e:
            print(f"Error loading image for card {card}: {e}")
            # You can handle the error as needed, e.g., by displaying a placeholder image
    image_above_buttons = pygame.image.load(f"Images/{additional_card[1:-1]}.png")
    image_above_buttons = pygame.transform.scale(image_above_buttons, (CARD_WIDTH, CARD_HEIGHT))
    if additional_card2 != "":
        Previous_move = pygame.image.load(f"Images/{additional_card2}.png")
        Previous_move = pygame.transform.scale(Previous_move, (CARD_WIDTH, CARD_HEIGHT))
    else:
        Previous_move = None
    return card_images,image_above_buttons,Previous_move

def display_hand_and_message(data):
    parts = data.split(";")
    global hand_list,player2_buttons,player2_cards,image_above_buttons,SHOW_TEXT,Previous_move,prev_move,round,party,message
    hand, message, prev_move, nbround, round_str, party_str, additional_card_str = parts[:7]
    nbround = int(nbround)
    round = tuple(map(int, round_str.split(",")))
    party = tuple(map(int, party_str.split(",")))
    if additional_card_str:
        additional_card = additional_card_str[1:-1]
    else:
        additional_card = None
    print(f"Your initial hand: {hand}")
    print(f"Previous move: {prev_move}")
    additional_card = additional_card.strip("[]")
    print(f"nbround: {nbround}")
    print(f"round: {round}")
    print(f"party: {party}")

    if additional_card:
        print(f"Additional card: {additional_card}")
    print(f"message {message}")

    # Load the card images for the updated hand
    hand_list = hand.split(",")
    player2_buttons = initialize_buttons(len(hand_list), CARD_WIDTH, CARD_HEIGHT)
    player2_cards = []
    try:
        player2_cards,image_above_buttons,Previous_move = load_card_images(hand_list,additional_card,prev_move)
    except Exception as e:
        print(f"Error loading card images: {e}")
    # Update the buttons and card images for Player 2
    button_width = CARD_WIDTH
    total_button_width = len(player2_buttons) * (button_width + PADDING)
    x_offset = (SCREEN_WIDTH - total_button_width) / 2
    for i, card in enumerate(player2_cards):
        player2_buttons[i] = pygame.Rect(x_offset + i * (button_width + PADDING), SCREEN_HEIGHT - CARD_HEIGHT - PADDING, CARD_WIDTH, CARD_HEIGHT)

    # Draw the buttons (rectangles) for Player 2
    for button in player2_buttons:
        pygame.draw.rect(screen, (200, 200, 200), button)

    # Draw the card images for Player 2 over the buttons
    for i, card in enumerate(player2_cards):
        screen.blit(card, player2_buttons[i].topleft)
    if image_above_buttons is not None:
        image_rect = image_above_buttons.get_rect()
        image_rect.centerx = SCREEN_WIDTH // 2
        image_rect.bottom = SPACING+CARD_HEIGHT + 50
        screen.blit(image_above_buttons, image_rect)
    if Previous_move is not None:
        image_rect.centerx = 650
        screen.blit(Previous_move, image_rect)
    if SHOW_TEXT: 
        text_rect = RENDER_TEXT.get_rect()
        text_rect.centerx = SCREEN_WIDTH // 2
        text_rect.bottom = SPACING + CARD_HEIGHT - 120
        screen.blit(RENDER_TEXT, text_rect)
        SHOW_TEXT = False
        additional_text_party2 = font.render(str(party), True, FONT_COLOR)
        additional_text_party_rect1 = additional_text_party1.get_rect()
        additional_text_party_rect2 = additional_text_party2.get_rect()
        additional_text_party_rect1.centerx = 40
        additional_text_party_rect2.centerx = 40
        additional_text_party_rect1.top = text_rect.bottom - 20
        additional_text_party_rect2.top = text_rect.bottom + 5
        screen.blit(additional_text_party1, additional_text_party_rect1)
        screen.blit(additional_text_party2, additional_text_party_rect2)

        message_rendered = font.render(str(message), True, FONT_COLOR)  
        additional_text_action = message_rendered.get_rect()
        additional_text_action.centerx = 150
        additional_text_action.top = text_rect.bottom + 50
        screen.blit(message_rendered, additional_text_action)

        additional_text_round2 = font.render(str(round), True, FONT_COLOR)
        additional_text_round_rect1 = additional_text_round1.get_rect()
        additional_text_round_rect2 = additional_text_round2.get_rect()
        additional_text_round_rect1.centerx = 170
        additional_text_round_rect2.centerx = 170
        additional_text_round_rect1.top = text_rect.bottom - 20
        additional_text_round_rect2.top = text_rect.bottom + 5
        screen.blit(additional_text_round1, additional_text_party_rect1)
        screen.blit(additional_text_round2, additional_text_party_rect2)

        additional_text_Last_Card = Last_Card.get_rect()
        additional_text_Last_Card.centerx = 650
        additional_text_Last_Card.top = text_rect.bottom - 15
        screen.blit(Last_Card, additional_text_Last_Card)
    pygame.display.flip()



input_active = True
input_text = ""
text_color = (0, 0, 0)
input_rect = pygame.Rect(200, 150, 400, 50)


def input_username():
    global input_active, input_text
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Send the username to the server
                    username = input_text
                    client.send(username.encode())
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill((255, 255, 255))
        color = text_color if input_active else (128, 128, 128)
        pygame.draw.rect(screen, color, input_rect, 2)

        text_surface = font.render(input_text, True, text_color)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()



input_username()
running = True
user_input = None
received_data = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            for i, button in enumerate(player2_buttons):
                if button.collidepoint(click_pos):
                    print(f"Player 2 - Card {i + 1} clicked")
                    # Send a message to the server when a card is clicked
                    user_input = hand_list[i]
        elif event.type == pygame.USEREVENT:
            received_data = event.data
    if received_data:
        display_hand_and_message(received_data)
        if "¡Apurate! Te estamos esperando..." in received_data:
            if user_input != None:
                client.send(str.encode(user_input))
                user_input=None
        elif "Esperando mi oponente.." in received_data:
            print("Waiting for the opponent's move...")
        elif "No sea un terrorista" in received_data:
            if user_input != None:
                client.send(str.encode(user_input))
                user_input=None
    additional_text_party2 = font.render(str(party), True, FONT_COLOR)
    additional_text_roound2 = font.render(str(round), True, FONT_COLOR)
    message_rendered = font.render(str(message), True, FONT_COLOR)
    pygame.time.delay(500)
    # Clear the screen
    screen.fill(WHITE)
    print(player2_buttons)
    # Draw the buttons and card images for Player 2
    for button in player2_buttons:
        pygame.draw.rect(screen, (200, 200, 200), button)

    for i, card in enumerate(player2_cards):
        screen.blit(card, player2_buttons[i].topleft)
    # Update the display
    if image_above_buttons is not None:
        image_rect = image_above_buttons.get_rect()
        image_rect.centerx = SCREEN_WIDTH // 2
        image_rect.bottom = SPACING+CARD_HEIGHT + 50
        screen.blit(image_above_buttons, image_rect)
        if Previous_move is not None:
            image_rect.centerx = 650
            screen.blit(Previous_move, image_rect)
        text_rect = RENDER_TEXT.get_rect()
        text_rect.centerx = SCREEN_WIDTH // 2
        text_rect.bottom = SPACING + CARD_HEIGHT - 120
        screen.blit(RENDER_TEXT, text_rect)
        additional_text_party_rect1 = additional_text_party1.get_rect()
        additional_text_party_rect2 = additional_text_party2.get_rect()
        additional_text_party_rect1.centerx = 40
        additional_text_party_rect2.centerx = 40
        additional_text_party_rect1.top = text_rect.bottom - 20
        additional_text_party_rect2.top = text_rect.bottom + 5
        screen.blit(additional_text_party1, additional_text_party_rect1)
        screen.blit(additional_text_party2, additional_text_party_rect2)

        additional_text_action = message_rendered.get_rect()
        additional_text_action.centerx = 150
        additional_text_action.top = text_rect.bottom + 50
        screen.blit(message_rendered, additional_text_action)


        additional_text_round2 = font.render(str(round), True, FONT_COLOR)
        additional_text_round_rect1 = additional_text_round1.get_rect()
        additional_text_round_rect2 = additional_text_round2.get_rect()
        additional_text_round_rect1.centerx = 170
        additional_text_round_rect2.centerx = 170
        additional_text_round_rect1.top = text_rect.bottom - 20
        additional_text_round_rect2.top = text_rect.bottom + 5
        screen.blit(additional_text_round1, additional_text_round_rect1)
        screen.blit(additional_text_round2, additional_text_round_rect2)

        additional_text_Last_Card = Last_Card.get_rect()
        additional_text_Last_Card.centerx = 650
        additional_text_Last_Card.top = text_rect.bottom - 15
        screen.blit(Last_Card, additional_text_Last_Card)
    pygame.display.flip()

    # Add a delay (optional) to prevent high CPU usage
    pygame.time.delay(50)


# Close the client socket
client.close()

# Quit Pygame
pygame.quit()
sys.exit()
