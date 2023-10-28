import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

# Set colors
Fundal = (44,62,80)
WHITE = (255, 255, 255)

# Set the dimensions of the board
board_width, board_height = 400, 400
board_x, board_y = (width - board_width) // 10, (height - board_height) // 2
cell_size = board_width // 10

# Set the dimensions of the second board
board2_width, board2_height = 400, 400
board2_x, board2_y = (width - board2_width) // 4 , (height - board2_height) // 2
cell2_size = board2_width // 10

#TIMMER
import numpy as np


# Draw the board

def draw_board():
    for i in range(11):
        pygame.draw.line(screen, WHITE, (board_x + i * cell_size, board_y),
                         (board_x + i * cell_size, board_y + board_height), 2)
        pygame.draw.line(screen, WHITE, (board_x, board_y + i * cell_size),
                         (board_x + board_width, board_y + i * cell_size), 2)

    for i in range(11):
        pygame.draw.line(screen, WHITE, (board2_x + i * cell2_size, board2_y),
                         (board2_x + i * cell2_size, board2_y + board2_height), 2)
        pygame.draw.line(screen, WHITE, (board2_x, board2_y + i * cell2_size),
                         (board2_x + board2_width, board2_y + i * cell2_size), 2)

# Function to move
#the second board
def move_board2():
    #move_board = True
    #if move_board==False :
    global board2_x
    board2_x +=  15*(cell2_size-15)
    #move_board=True
# Main function to run the game
global zz

import pygame
import sys



# Set up the display
#screen = pygame.display.set_mode((400, 300))
#pygame.display.set_caption("Timer Example")

# Initialize font

# Function to display the timer
def show_timer(seconds):
    font = pygame.font.Font(None, 75) # FONTUL TIMMERULUI
    screen.fill((255, 255, 255))
    text = font.render(str(seconds), True, (0, 0, 0))
    text_rect = text.get_rect(center=(450, 450))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Timer function
def timer():
    for i in range(3, 0, -1):
        show_timer(i)
        pygame.time.wait(1000)

    # Call your function here after the timer is finished


# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

boat_width_1 = 3 * cell_size
boat_height_1 = 1 * cell_size

boat_width_2= 4 * cell_size
boat_height_2 = 1 * cell_size

boat_width_3 = 5 * cell_size
boat_height_3 = 1 * cell_size
# Boat dimensions

boat_width_4 = 2 * cell_size
boat_height_4 = 1 * cell_size


# Draw boats
def draw_boats():
    boat1_x, boat1_y = board_x + 2 * cell_size, board_y + 2 * cell_size
    boat2_x, boat2_y = board_x + 5 * cell_size, board_y + 4 * cell_size
    boat3_x, boat3_y = board_x + 1 * cell_size, board_y + 7 * cell_size
    boat4_x, boat4_y = board_x + 7 * cell_size, board_y + 1 * cell_size

    pygame.draw.rect(screen, BLUE, (boat1_x, boat1_y, boat_width_1, boat_height_1))
    pygame.draw.rect(screen, BLUE, (boat2_x, boat2_y, boat_width_2, boat_height_2))
    pygame.draw.rect(screen, BLUE, (boat3_x, boat3_y, boat_width_3, boat_height_3))
    pygame.draw.rect(screen, BLUE, (boat4_x, boat4_y, boat_width_4, boat_height_4))

# Your function to be called after the timer
def your_function():
    # Your function logic goes here
    print("Your function is called after the timer.")

# Call the timer function

def run_game():
    timer()
    zz = False
    running = True
    # if zz==False :
    #draw_board()  # Draw the board
    initial_state=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # conditie de iesire tre in while sa ii zic daca apesi pe x sau cv puton whatever si le fac butoane casutele
        if initial_state==True:
            print("a-")
            screen.fill(Fundal)  # Fill the screen with Fundal
            #draw_board()  # Draw the boards
            #draw_board()  # Draw the board
            draw_boats()  # Draw boats
            #draw_board()  # Draw the boards
            move_board2()  # Move the second board

            draw_board()  # Draw the boards

            pygame.display.flip()  # Update the full display Surface to the screen
            zz = True
            initial_state=False
                # de revazut de ce nu se modifica
        pygame.display.flip()  # Update the full display Surface to the screen

    pygame.quit()

# Call the main function to run the game
if __name__ == "__main__":
    run_game()

