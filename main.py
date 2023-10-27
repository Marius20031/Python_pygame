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
board_width, board_height = 600, 600
board_x, board_y = (width - board_width) // 4, (height - board_height) // 2
cell_size = board_width // 10

# Set the dimensions of the second board
board2_width, board2_height = 600, 600
board2_x, board2_y = (width - board2_width) // 4 * 3, (height - board2_height) // 2
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

# Function to move the second board
def move_board2():
    global board2_x
    board2_x += cell2_size

# Main function to run the game
def run_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(Fundal)  # Fill the screen with Fundal
        draw_board()  # Draw the boards
        draw_board()  # Draw the boards
        #move_board2()  # Move the second board
        pygame.display.flip()  # Update the full display Surface to the screen

    pygame.quit()

# Call the main function to run the game
if __name__ == "__main__":
    run_game()
