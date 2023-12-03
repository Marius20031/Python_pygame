import pygame
from Importuri import *
from importuri_bgd import *
def rotate_boats(selected):
    #global boats
    global boat_width_1
    global boat_width_2
    global boat_width_3
    global boat_width_4
    global boat_height_1
    global boat_height_2
    global boat_height_3
    global boat_height_4
    if selected is not None and 0 <= selected < len(boats):
        boat_x, boat_y = boats[selected]
        var_swap_1=boat_width_VECT[selected]
        var_swap_2=boat_height_VECT[selected]
        boat_width_VECT[selected]=var_swap_2
        boat_height_VECT[selected]=var_swap_1
        #boats[selected]=boat_y, boat_x
        if selected == 0:
            #eu trb sa asez barca in functie de pozitia pe matrice
            #nu in functie de numarul ei, deci trb facute niste calcule in plus...
            boat_width, boat_height = boat_width_1, boat_height_1
            boat_width_1, boat_height_1 = boat_height, boat_width
            boats[selected]= boat_width_1, boat_height_1
        elif selected == 1:
            boat_width, boat_height = boat_width_2, boat_height_2
            boat_width_2, boat_height_2 = boat_height, boat_width
            boats[selected] = boat_width_2, boat_height_2
        elif selected == 2:
            boat_width, boat_height = boat_width_3, boat_height_3
            boat_width_3, boat_height_3 = boat_height, boat_width
            boats[selected] = boat_width_3, boat_height_3
        elif selected == 3:
            boat_width, boat_height = boat_width_4, boat_height_4
            boat_width_4, boat_height_4 = boat_height, boat_width
            boats[selected] = boat_width_4, boat_height_4
        boats[selected] = (boat_x, boat_y) #!!!!!!!!!!!!!!
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
    button_font = pygame.font.Font(None, 36)
    rotate_button = pygame.Rect(50, 50, 100, 50)
    start_button = pygame.Rect(350, 50, 100, 50)

    pygame.draw.rect(screen, (255, 0, 0), start_button)
    pygame.draw.rect(screen, (255, 0, 0), rotate_button)

    button_text = button_font.render("Rotate", True, (255, 255, 255))
    button_text_1 = button_font.render("Start", True, (255, 255, 255))

    screen.blit(button_text, (60, 60))
    screen.blit(button_text_1, (360, 60))

    last_one_tho=None
    move_board2()
    running = True
    semafor_start_game = 0 # nu s.a apasat start

    while running:
        button_font = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(semafor_start_game==0):
                    mouse_x, mouse_y = event.pos
                    # deci casuta stanga sus prima linie lrima coloana: 1,5-2,5| 7,5-8,5
                    # 1,5-2,5-3,5 pe x
                    #7,5-8,5 pe Y
                    print(mouse_x/cell_size)
                    print(mouse_y/cell_size) # pentru coordonate in matrice
                    for i, (boat_x, boat_y) in enumerate(boats):
                        # nu inteleg de ce functioneaza dar functioneaza efectiv....
                        # da aici trb sa verific daca intre alea se afla barca aici trb modificat:
                        # daca fac 1*cellsize si (i+2) imi iau pe verticala
                        #daca fac invers, imi ia pe orizontala
                        if boat_x <= mouse_x <= boat_x+boat_width_VECT[i]*cell_size and boat_y <= mouse_y <= boat_y+boat_height_VECT[i]*cell_size: # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                            selected = i
                            last_one_tho=selected
                            print("barca")
                            print(i)
                            offset_x = mouse_x - boat_x
                            offset_y = mouse_y - boat_y
                    if rotate_button.collidepoint(event.pos):
                        #print("seapasa")
                        rotate_boats(last_one_tho)
                    if start_button.collidepoint(event.pos):
                        print("CE PPPLMA")
                        semafor_start_game=1
                else:
                    mouse_x, mouse_y = event.pos
                    for i, (boat_x, boat_y) in enumerate(boats):
                        # nu inteleg de ce functioneaza dar functioneaza efectiv....
                        # da aici trb sa verific daca intre alea se afla barca aici trb modificat:
                        # daca fac 1*cellsize si (i+2) imi iau pe verticala
                        #daca fac invers, imi ia pe orizontala
                        if boat_x <= mouse_x <= boat_x+boat_width_VECT[i]*cell_size and boat_y <= mouse_y <= boat_y+boat_height_VECT[i]*cell_size: # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                            selected = i
                            last_one_tho=selected
                            print("BARCA A FOST LOVITA SI ESTE BARCA NR: ")
                            print(i)
                            #offset_x = mouse_x - boat_x
                            #offset_y = mouse_y - boat_y
            elif event.type == pygame.MOUSEBUTTONUP:
                last_one_tho=selected
                selected = None
            elif event.type == pygame.MOUSEMOTION:
                if(semafor_start_game==0):
                    if selected is not None:
                        mouse_x, mouse_y = event.pos
                        # calcule
                        min_x = board_x
                        max_x = board_x +board_width - boat_width_VECT[selected]*cell_size
                        min_y = board_y
                        max_y = board_y + board_height - boat_height_VECT[selected]*cell_size
                        # ajustarea pozitiei
                        boat_x = min(max(round((mouse_x - offset_x - board_x) / cell_size) * cell_size + board_x, min_x),
                                     max_x)
                        boat_y = min(max(round((mouse_y - offset_y - board_y) / cell_size) * cell_size + board_y, min_y),
                                     max_y)
                        boats[selected] = (boat_x, boat_y)
                        print(boat_x)
                        print(boat_y)
                # ...
        screen.fill(Fundal)  # funddalula
        draw_board()  # desenam
        pygame.draw.rect(screen, (255, 0, 0), rotate_button)
        pygame.draw.rect(screen, (255, 0, 0), start_button)
        button_text = button_font.render("Rotate", True, (255, 255, 255))
        button_text_1 = button_font.render("Start", True, (255, 255, 255))

        screen.blit(button_text, (60, 60))
        screen.blit(button_text_1, (360, 60))

        color_1=(65,84,178)
        color_2 = (58, 45, 240)
        color_3 = (232, 252, 56)
        color_4 = (48, 195, 126)
        for i, (boat_x, boat_y) in enumerate(boats):# ok deci boats pentru desenare dar _VECT pt pozitionarea tragerii!!!
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
            afisare_playeri()  # scris de mn
        pygame.display.flip()  # faceme update mere in running

    pygame.quit()


