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

# Boat dimensions
boat_width_1 = 2 * cell_size
boat_height_1 = 1 * cell_size

boat_width_2= 3 * cell_size
boat_height_2 = 1 * cell_size

boat_width_3 = 4 * cell_size
boat_height_3 = 1 * cell_size

boat_width_4 = 5 * cell_size
boat_height_4 = 1 * cell_size

# Boats' initial positions
boats = [
    (2 * cell_size, 1 * cell_size),
    (3 * cell_size, 2 * cell_size),
    (4 * cell_size, 3 * cell_size),
    (5 * cell_size, 4 * cell_size)
]

# Drag and drop variables
selected = None
offset_x = 0
offset_y = 0

def show_timer(seconds):
    font = pygame.font.Font(None, 75) # FONTUL TIMMERULUI
    screen.fill((255, 255, 255))
    text = font.render(str(seconds), True, (0, 0, 0))
    text_rect = text.get_rect(center=(450, 450))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Timer func
# tion
def move_board2():
    #move_board = True
    #if move_board==False :
    global board2_x
    board2_x +=  15*(cell2_size-15)
    #move_board=True
# Main function to ru
def timer():
    for i in range(3, 0, -1):
        show_timer(i)
        pygame.time.wait(1000)

# Main function to run the game
def run_game():
    global selected
    global offset_x
    global offset_y
    timer()
    move_board2()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, (boat_x, boat_y) in enumerate(boats):
                    if boat_x <= mouse_x <= boat_x+(i+2)*cell_size and boat_y <= mouse_y <= boat_y+cell_size : # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                        selected = i
                        offset_x = mouse_x - boat_x
                        offset_y = mouse_y - boat_y
            elif event.type == pygame.MOUSEBUTTONUP:
                selected = None
            elif event.type == pygame.MOUSEMOTION:
                if selected is not None:
                    mouse_x, mouse_y = event.pos
                    boats[selected] = (mouse_x - offset_x, mouse_y - offset_y)

        screen.fill(Fundal)  # Fill the screen with background color
        draw_board()  # Draw the board
        for i, (boat_x, boat_y) in enumerate(boats):
            if i == selected:
                color = (255, 0, 0)  # Highlight the selected boat in red
            else:
                color = (0, 0, 255)  # Set the default boat color to blue
            if i == 0:
                pygame.draw.rect(screen, color, (boat_x, boat_y, boat_width_1, boat_height_1))
            elif i == 1:
                pygame.draw.rect(screen, color, (boat_x, boat_y, boat_width_2, boat_height_2))
            elif i == 2:
                pygame.draw.rect(screen, color, (boat_x, boat_y, boat_width_3, boat_height_3))
            elif i == 3:
                pygame.draw.rect(screen, color, (boat_x, boat_y, boat_width_4, boat_height_4))

        pygame.display.flip()  # Update the full display surface

    pygame.quit()

# Call the main function to run the game
if __name__ == "__main__":
    run_game()
