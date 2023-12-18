import time

import pygame
from Importuri import *
from runde import *
import numpy as np

from bot import *
from importuri_bgd import *
circle_color_rosu = (255, 0, 0)
circle_color_verde = (0, 128, 0)


barca=pygame.image.load("Photos/barca5noua.png")
barca=barca.convert_alpha()
barca=pygame.transform.smoothscale(barca,(200,45))

dinghy = pygame.image.load("Photos/dingy2.png.png")
dinghy = dinghy.convert_alpha()
dinghy = pygame.transform.smoothscale(dinghy,( 88, 40))
dinghy = pygame.transform.rotate(dinghy,180)

barca2 = pygame.image.load("Photos/barca3noua.png")
barca2 = barca2.convert_alpha()
barca2 = pygame.transform.smoothscale(barca2,( 118, 40))

barca3 = pygame.image.load("Photos/barca4noua.png")
barca3 = barca3.convert_alpha()
barca3 = pygame.transform.smoothscale(barca3,( 210, 360))

barci_rotite=[0,0,0,0]
def rotate_boats(selected):
    global dinghy
    global barca
    global barca2
    global barca3
    global barci_rotite
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
            if barci_rotite[0]==0:
                dinghy=pygame.transform.rotate(dinghy,90)
                barci_rotite[0]=1
            else:
                dinghy = pygame.transform.rotate(dinghy, -90)
                barci_rotite[0] = 0
        elif selected == 1:
            boat_width, boat_height = boat_width_2, boat_height_2
            boat_width_2, boat_height_2 = boat_height, boat_width
            boats[selected] = boat_width_2, boat_height_2
            if barci_rotite[1]==0:
                barca2=pygame.transform.rotate(barca2,90)
                barci_rotite[1]=1
            else:
                barca2 = pygame.transform.rotate(barca2, -90)
                barci_rotite[1] = 0
        elif selected == 2:
            boat_width, boat_height = boat_width_3, boat_height_3
            boat_width_3, boat_height_3 = boat_height, boat_width
            boats[selected] = boat_width_3, boat_height_3
            if barci_rotite[2]==0:
                barca3 = pygame.transform.rotate(barca3,90)
                barci_rotite[2]=1
            else:
                barca3 = pygame.transform.rotate(barca3, -90)
                barci_rotite[2] = 0
        elif selected == 3:
            boat_width, boat_height = boat_width_4, boat_height_4
            boat_width_4, boat_height_4 = boat_height, boat_width
            boats[selected] = boat_width_4, boat_height_4
            if barci_rotite[3]==0:
                barca=pygame.transform.rotate(barca,90)
                barci_rotite[3]=1
            else:
                barci_rotite[3]=0
                barca=pygame.transform.rotate(barca,-90)
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
    font = pygame.font.Font(None, 120) # FONTUL TIMMERULUI
    screen.fill(albastru)
    screen.blit(back, (0, 0))
    show_text_timer()
    text = font.render(str(seconds), True, white)
    text_rect = text.get_rect(center=(450, 450))
    screen.blit(text, text_rect)
    pygame.display.flip()

# functia de afisare timer
def move_board2():
    global board2_x
    board2_x +=  15*(cell2_size-15)

# functia main de a rula
def timer():
    for i in range(3, 0, -1):
        show_timer(i)
        pygame.time.wait(1000)
def get_valid_pozitiei_barci():
    var=0;
    # iterez
    for i in range(2,12):
        for j in range(8,18):
            for w, (boat_x, boat_y) in enumerate(boats):
                if boat_x <= i*cell_size <= boat_x + boat_width_VECT[w] * cell_size and boat_y <= j*cell_size <= boat_y + boat_height_VECT[w] * cell_size:
                    var=var+1
                    mat[j-8][i-2]=1
                    break
    if var == 14:
        return 1
    for i in range(0, 10):
        for j in range(0, 10):
            mat[i][j]=0
    return 0

global trebuie_timer
trebuie_timer=[0]
meniu=0
def run_game():
    global selected
    global offset_x
    global offset_y
    running = True
    mai_continua = [1]
    if meniu == 0:
        enter_menu(mai_continua)
    if mai_continua[0] == 0:
        running = False
    else:
        timer()
    afisare_icon_bot()
    button_font = pygame.font.Font(None, 36)
    rotate_button = pygame.Rect(660, 800, 120, 50)
    start_button = pygame.Rect(430, 80, 120, 50)

    pygame.draw.rect(screen, (255, 0, 0), rotate_button)

    button_text_1 = button_font.render("Start", True, (255, 255, 255))

    screen.blit(button_text_1, (360, 60))
    global trebuie_timer

    last_one_tho=None
    move_board2()
    semafor_start_game = 0 # nu s.a apasat start

    creare_matrice_barci_poz()
    CUSTOM_MOUSEMOTION_EVENT = pygame.USEREVENT + 1
    semnal=0
    def simulate_mouse_motion():
        pygame.event.post(pygame.event.Event(CUSTOM_MOUSEMOTION_EVENT))
    # Post the custom event to the queue
    bot_win = 0
    while running:
        global nr_sec
        if joc_e_gata[0]==0:
            if jucam_cu_bot[0]==1:
                if al_cui_e_randul[0] == 1:
                    bot_alege_pozitie()
                    random_time_sleep=random.randint(1,2)
                    incepe_timer(1,trebuie_timer,nr_sec,random_time_sleep,1)
                    trebuie_timer[0] = 1
                    # aici e botul de fapt
                    runda_player_main(var_x[0], var_y[0])
                    if al_cui_e_randul[0]!=1:
                        nr_sec[0]=30
                        semnal=1
                    else:
                        semnal=0
                    if check_if_game_over() == 1:
                        bot_win = 1
                        # MESAJ CASTIGA BOT
                        joc_e_gata[0] = 1
        if semnal==0:
            for event in pygame.event.get():
                if semnal==1:
                    break
                ok2=0
                while (trebuie_timer[0] == 1):  # incepe timeru cand e nevoie de el
                    event2 = incepe_timer(al_cui_e_randul[0], trebuie_timer, nr_sec,0,0)
                    event = event2
                    if event == None:
                        if jucam_cu_bot[0]==1:
                            al_cui_e_randul[0]=1
                            ok2=1
                            break
                        else:
                            trebuie_timer[0] = 1
                            if al_cui_e_randul[0] == 0:
                                al_cui_e_randul[0] = 1
                            else:
                                al_cui_e_randul[0] = 0
                if ok2==1:
                    break
                #implementata pentru player
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if joc_e_gata[0]==0:
                        mouse_x, mouse_y = event.pos
                        if(semafor_start_game==0):
                            for i, (boat_x, boat_y) in enumerate(boats):
                                if boat_x <= mouse_x <= boat_x+boat_width_VECT[i]*cell_size and boat_y <= mouse_y <= boat_y+boat_height_VECT[i]*cell_size: # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                                    selected = i
                                    last_one_tho=selected
                                    offset_x = mouse_x - boat_x
                                    offset_y = mouse_y - boat_y
                            if rotate_button.collidepoint(event.pos):
                                rotate_boats(last_one_tho)
                            if start_button.collidepoint(event.pos):
                                if get_valid_pozitiei_barci()==1:
                                    merge[0]=1
                                    semafor_start_game=1
                                    trebuie_timer[0] = 1
                                else: merge[0]=0
                            if text_rect8.collidepoint(event.pos):
                                shift_right_icon()
                            if text_rect9.collidepoint(event.pos):
                                shift_left_icon()
                        else:
                            mouse_x, mouse_y = event.pos
                            # nu mai asteptam event poze daca jucam cu bot!
                            if jucam_cu_bot[0] == 1:
                                if al_cui_e_randul[0]==0:
                                    runda_bot(mouse_x, mouse_y,trebuie_timer)
                                    if check_if_game_over() == 2:
                                        joc_e_gata[0]=1
                                    if al_cui_e_randul[0]!=0:
                                        nr_sec[0]=30
                                    else:
                                        semnal=1
                                # si intra direct mutarea botului
                            # matricea adversarului
                            else:
                                if al_cui_e_randul[0] == 1:
                                    runda_player_main(mouse_x, mouse_y)
                                    trebuie_timer[0] = 1
                                    if al_cui_e_randul[0]!=1:
                                        nr_sec[0]=30
                                    else:
                                        semnal=1
                                    # matricea adversarului
                                else:
                                    runda_bot(mouse_x, mouse_y,trebuie_timer)
                                    trebuie_timer[0] = 1
                                    if al_cui_e_randul[0]!=0:
                                        nr_sec[0]=30
                                    else:
                                        semnal=1
                            for i, (boat_x, boat_y) in enumerate(boats):
                                # da aici trb sa verific daca intre alea se afla barca aici trb modificat:
                                # daca fac 1*cellsize si (i+2) imi iau pe verticala
                                #daca fac invers, imi ia pe orizontala
                                if boat_x <= mouse_x <= boat_x+boat_width_VECT[i]*cell_size and boat_y <= mouse_y <= boat_y+boat_height_VECT[i]*cell_size: # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                                    selected = i
                                    last_one_tho=selected
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
        screen.fill(Fundal)
        screen.blit(fundal,(0,0))
        show_background()
        draw_board()  # desenam
        for i, (boat_x, boat_y) in enumerate(boats):  # ok deci boats pentru desenare dar _VECT pt pozitionarea tragerii!!!
            if i == 0:
                if barci_rotite[0]==0:
                    screen.blit(dinghy, (boat_x - 3, boat_y ))
                else:
                    screen.blit(dinghy,(boat_x+2, boat_y-4 ))
            elif i == 1:
                if barci_rotite[1]==0:
                    screen.blit(barca2,(boat_x +2, boat_y ))
                else:
                    screen.blit(barca2, (boat_x+1, boat_y ))
            elif i == 2:
                if barci_rotite[2]==0:
                    screen.blit(barca3, (boat_x -22, boat_y-165))
                else:
                    screen.blit(barca3, (boat_x - 164, boat_y - 25))
            elif i == 3:
                if barci_rotite[3]==0:
                    screen.blit(barca, (boat_x , boat_y -2))
                else:
                    screen.blit(barca, (boat_x-2 , boat_y ))
        afisare_playeri()
        if (semafor_start_game == 0):
            afisare_barci()
        if semafor_start_game==1:
            show_level()
        if merge[0]==0:
            error_boats_not_in_correct_position()
        if merge[1] == 0:
            error_cannot_make_same_move()
            #merge[1] = 1
        if merge[2] == 0:
            error_not_your_turn()
        afisare_contur_timer()
        afisare_timer_default()
        if joc_e_gata[0] == 1 and bot_win == 0:
            castig_player = "WINNER"
            castig_player_surface = font_urias.render(castig_player, True, green)
            castig_player_rect = castig_player_surface.get_rect()
            castig_player_rect.center = (500, 200)
            screen.blit(castig_player_surface, castig_player_rect)
            trebuie_timer[0] = 0
            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

            class Confetti:
                def __init__(self):
                    self.x = random.randint(0, width)
                    self.y = random.randint(0, height)
                    self.color = random.choice(colors)
                    self.speed = random.randint(1, 5)
                    self.size = random.randint(5, 15)

                def move(self):
                    self.y += self.speed
                    if self.y > height:
                        self.y = 0
                        self.x = random.randint(0, width)

                def draw(self):
                    pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size * 1.5))

            confetti_pieces = [Confetti() for _ in range(100)]
            for confetti in confetti_pieces:
                confetti.move()
                confetti.draw()

        elif joc_e_gata[0] == 1 and bot_win == 1:
            castig_bot = "LOSER"
            castig_bot_surface = font_urias.render(castig_bot, True, red)
            castig_bot_rect = castig_bot_surface.get_rect()
            castig_bot_rect.center = (500, 200)
            screen.blit(castig_bot_surface, castig_bot_rect)
            trebuie_timer[0] = 0
        for uwu in range(0, nr_total_cercuri[0]):
            if tupla_ai_nimerit[uwu]:
                global explozie
                screen.blit(explozie, (tupla_cu_cercuri[uwu][0] - 30, tupla_cu_cercuri[uwu][1] - 30))
            else:
                screen.blit(x_mare, (tupla_cu_cercuri[uwu][0] - 20, tupla_cu_cercuri[uwu][1] - 20))
        pygame.time.Clock().tick(24)
        pygame.display.flip()
        if semnal==1:
            semnal=0
            simulate_mouse_motion()
    pygame.quit()
