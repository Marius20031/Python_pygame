import pygame
from Importuri import *

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

# dimensiunea barcilor

def show_timer(seconds):
    font = pygame.font.Font(None, 75) # FONTUL TIMMERULUI
    screen.fill((255, 255, 255))
    text = font.render(str(seconds), True, (0, 0, 0))
    text_rect = text.get_rect(center=(450, 450))
    screen.blit(text, text_rect)
    pygame.display.flip()

# functia de afisare timer
def move_board2():
    #move_board = True
    #if move_board==False :
    global board2_x
    board2_x +=  15*(cell2_size-15)
    #move_board=True

# functia main de a rula
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
                    # calcule
                    min_x = board_x
                    max_x = board_x + board_width - (selected + 2) * cell_size
                    min_y = board_y
                    max_y = board_y + board_height - cell_size
                    # ajustarea pozitiei
                    boat_x = min(max(round((mouse_x - offset_x - board_x) / cell_size) * cell_size + board_x, min_x),
                                 max_x)
                    boat_y = min(max(round((mouse_y - offset_y - board_y) / cell_size) * cell_size + board_y, min_y),
                                 max_y)
                    boats[selected] = (boat_x, boat_y)
                # ...

        screen.fill(Fundal)  # funddalula
        draw_board()  # desenam
        color_1=(65,84,178)
        color_2 = (58, 45, 240)
        color_3 = (232, 252, 56)
        color_4 = (48, 195, 126)
        for i, (boat_x, boat_y) in enumerate(boats):
            if i == selected:
                color = (255, 0, 0)  # se face rosu cand ii dam drag
            else:
                color = (0, 0, 255)  #culoarea default
            if i == 0:
                pygame.draw.rect(screen, color_1, (boat_x, boat_y, boat_width_1, boat_height_1))
            elif i == 1:
                pygame.draw.rect(screen, color_2, (boat_x, boat_y, boat_width_2, boat_height_2))
            elif i == 2:
                pygame.draw.rect(screen, color_3, (boat_x, boat_y, boat_width_3, boat_height_3))
            elif i == 3:
                pygame.draw.rect(screen, color_4, (boat_x, boat_y, boat_width_4, boat_height_4))

        pygame.display.flip()  # faceme update mere in running

    pygame.quit()
