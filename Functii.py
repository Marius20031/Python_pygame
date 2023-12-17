import time

import pygame
from Importuri import *
from runde import *
import numpy as np

from bot import *
from importuri_bgd import *
circle_color_rosu = (255, 0, 0)
circle_color_verde = (0, 128, 0)


barca=pygame.image.load("Photos/aircraft-carrier-amphibious-warfare-ship-navy-fast-attack-craft-ship-65ee4dc1359d19cd881525eaf9a4c4bd.png")
barca=barca.convert_alpha()
barca=pygame.transform.smoothscale(barca,(235,180))

dinghy = pygame.image.load("Photos/dingy2.png.png")
dinghy = dinghy.convert_alpha()
dinghy = pygame.transform.smoothscale(dinghy,( 88, 40))
dinghy = pygame.transform.rotate(dinghy,180)

barca2 = pygame.image.load("Photos/Daco_2380481.png")
barca2 = barca2.convert_alpha()
barca2 = pygame.transform.smoothscale(barca2,( 140, 90))

barca3 = pygame.image.load("Photos/barca3.png")
barca3 = barca3.convert_alpha()
barca3 = pygame.transform.smoothscale(barca3,( 175, 70))

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
                dinghy=pygame.transform.rotate(dinghy,270)
                barci_rotite[0]=1
            else:
                dinghy = pygame.transform.rotate(dinghy, -270)
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
    show_text_timer()
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
def get_valid_pozitiei_barci():
    # TO DO:
    # iteresz prin fiecare pozitie din boats[i] (i=0:3)
    # daca e una sub alta, ERROR Boats not valid!!
    var=0;
    # iterez
    for i in range(2,12):
        for j in range(8,18):
            for w, (boat_x, boat_y) in enumerate(boats):
                if boat_x <= i*cell_size <= boat_x + boat_width_VECT[w] * cell_size and boat_y <= j*cell_size <= boat_y + boat_height_VECT[w] * cell_size:
                    var=var+1
                    mat[j-8][i-2]=1
                    break
    #print("barcile sunt vazute ca:")
    #print(var)
    if var == 14:
        #print(mat)
        return 1
    for i in range(0, 10):
        for j in range(0, 10):
            mat[i][j]=0
    #mat = np.zeros((10, 10))
    return 0

global trebuie_timer#adaugat de mn
trebuie_timer=[0]
meniu=0
# Main function to run the game
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
        #timer()
        print("")
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
        button_font = pygame.font.Font(None, 36)
        if joc_e_gata[0]==0:
            if jucam_cu_bot[0]==1:
                if al_cui_e_randul[0] == 1:
                    bot_alege_pozitie()
                    random_time_sleep=random.randint(1,2)
                    incepe_timer(1,trebuie_timer,nr_sec,random_time_sleep,1)
                    trebuie_timer[0] = 1
                    #nr_sec=[30]
                    # aici e botul de fapt
                    runda_player_main(var_x[0], var_y[0])
                    print(al_cui_e_randul[0])
                    print(nr_sec[0])
                    if al_cui_e_randul[0]!=1:
                        nr_sec[0]=30
                        semnal=1
                    else:
                        semnal=0
                    if check_if_game_over() == 1:
                        print("JOCUL E GATA!!! castiga BOTUL!!")
                        bot_win = 1
                        # MESAJ CASTIGA BOT
                        joc_e_gata[0] = 1
                   # semnal=1
        if semnal==0:
            for event in pygame.event.get():
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
                        #print(mouse_x / cell_size)
                        #print(mouse_y / cell_size)  # pentru coordonate in matrice
                        if(semafor_start_game==0):
                            #mouse_x, mouse_y = event.pos
                            # deci casuta stanga sus prima linie lrima coloana: 1,5-2,5| 7,5-8,5
                            # 1,5-2,5-3,5 pe x
                            #7,5-8,5 pe Y
                            ##print(mouse_x/cell_size)
                            ##print(mouse_y/cell_size) # pentru coordonate in matrice
                            for i, (boat_x, boat_y) in enumerate(boats):
                                # nu inteleg de ce functioneaza dar functioneaza efectiv....
                                # da aici trb sa verific daca intre alea se afla barca aici trb modificat:
                                # daca fac 1*cellsize si (i+2) imi iau pe verticala
                                #daca fac invers, imi ia pe orizontala
                                if boat_x <= mouse_x <= boat_x+boat_width_VECT[i]*cell_size and boat_y <= mouse_y <= boat_y+boat_height_VECT[i]*cell_size: # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                                    selected = i
                                    last_one_tho=selected
                                    #print("barca")
                                    #print(i)
                                    offset_x = mouse_x - boat_x
                                    offset_y = mouse_y - boat_y
                            if rotate_button.collidepoint(event.pos):
                                ##print("seapasa")
                                rotate_boats(last_one_tho)
                            if start_button.collidepoint(event.pos):
                                #print("NU E GATA")
                                if get_valid_pozitiei_barci()==1:
                                    merge[0]=1
                                    #print("E GATA")
                                    semafor_start_game=1
                                    trebuie_timer[0] = 1  # adaugat de mn
                                else: merge[0]=0
                            # adaugat de mn incepand de aici
                            if text_rect8.collidepoint(event.pos):
                                shift_right_icon()
                            if text_rect9.collidepoint(event.pos):
                                shift_left_icon()
                            # pana aici
                        else:
                            mouse_x, mouse_y = event.pos
                            # nu mai asteptam event poze daca jucam cu bot!
                            #if al_cui_e_randul[0]==1:
                            if jucam_cu_bot[0] == 1:
                                if al_cui_e_randul[0]==0:
                                    ##print(trebuie_timer[0])
                                    runda_bot(mouse_x, mouse_y,trebuie_timer)
                                    ##print(trebuie_timer[0])
                                    if check_if_game_over() == 2:
                                        print("JOCUL E GATA!!! castiga MARIUS!!!")

                                        #MESAJ CASTIGA PLAYERU
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
                                    trebuie_timer[0] = 1  # adaugat de mn
                                    if al_cui_e_randul[0]!=1:
                                        nr_sec[0]=30
                                    else:
                                        semnal=1
                                    # matricea adversarului
                                else:
                                    runda_bot(mouse_x, mouse_y,trebuie_timer)
                                    trebuie_timer[0] = 1  # adaugat de mn
                                    if al_cui_e_randul[0]!=0:
                                        nr_sec[0]=30
                                    else:
                                        semnal=1
                            #   if jucam_cu_bot[0]==1:
                                    #bot_alege_pozitie()
                                    ##print("ce plms")
                              #      runda_bot(mouse_x, mouse_y)
                                    #runda_adversar(mouse_x,mouse_y)

                            for i, (boat_x, boat_y) in enumerate(boats):
                                # nu inteleg de ce functioneaza dar functioneaza efectiv....
                                # da aici trb sa verific daca intre alea se afla barca aici trb modificat:
                                # daca fac 1*cellsize si (i+2) imi iau pe verticala
                                #daca fac invers, imi ia pe orizontala
                                if boat_x <= mouse_x <= boat_x+boat_width_VECT[i]*cell_size and boat_y <= mouse_y <= boat_y+boat_height_VECT[i]*cell_size: # ca sa ia toata barca DE RECITI ACII CONDITIILE PT CLICKURI
                                    selected = i
                                    last_one_tho=selected
                                    # cum convertesc din
                                    #print("BARCA A FOST LOVITA SI ESTE BARCA NR: ")
                                    #print(i)
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
                            #print(boat_x)
                            #print(boat_y)

                    # ...
        screen.fill(Fundal)  # funddalula
        screen.blit(fundal,(0,0))
        show_background() #bogdan
        draw_board()  # desenam
        #pygame.draw.rect(screen, (255, 0, 0), start_button)
        #button_text_1 = button_font.render("Start", True, (255, 255, 255))
        #screen.blit(button_text, (680, 810))
        #screen.blit(button_text_1, (360, 60))

        color_1=(65,84,178)
        color_2 = (58, 45, 240)
        color_3 = (232, 252, 56)
        color_4 = (48, 195, 126)
        for i, (boat_x, boat_y) in enumerate(boats):  # ok deci boats pentru desenare dar _VECT pt pozitionarea tragerii!!!
            if i == selected:
                color = (255, 0, 0)  # se face rosu cand ii dam drag
            else:
                color = (0, 0, 255)  # culoarea default
            if i == 0:
                # pygame.draw.rect(screen, color_1, (boat_x, boat_y, boat_width_1, boat_height_1))
                if barci_rotite[0]==0:
                    screen.blit(dinghy, (boat_x - 3, boat_y ))
                else:
                    screen.blit(dinghy,(boat_x+2, boat_y-4 ))
            elif i == 1:
                #pygame.draw.rect(screen, color_2, (boat_x, boat_y, boat_width_2, boat_height_2))
                if barci_rotite[1]==0:
                    screen.blit(barca2,(boat_x-10 , boat_y - 50))
                else:
                    screen.blit(barca2, (boat_x-51, boat_y - 7))
            elif i == 2:
                #pygame.draw.rect(screen, color_3, (boat_x, boat_y, boat_width_3, boat_height_3))
                if barci_rotite[2]==0:
                    screen.blit(barca3, (boat_x -8, boat_y - 30))
                else:
                    screen.blit(barca3, (boat_x - 30, boat_y - 9))
            elif i == 3:
                # pygame.draw.rect(screen, color_4, (boat_x, boat_y, boat_width_4, boat_height_4))
                if barci_rotite[3]==0:
                    screen.blit(barca, (boat_x - 18, boat_y - 70))
                else:
                    screen.blit(barca, (boat_x - 72, boat_y - 58))
        afisare_playeri()  # scris de mn
        if (semafor_start_game == 0): #scris de mn
            afisare_barci()
        if merge[0]==0:
            error_boats_not_in_correct_position()
        if merge[1] == 0:
            error_cannot_make_same_move()
            #merge[1] = 1
        if merge[2] == 0:
            error_not_your_turn()
            #merge[2] = 1
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
                #pygame.draw.circle(screen, circle_color_rosu, tupla_cu_cercuri[uwu], 5)
                #
            else:
                screen.blit(x_mare, (tupla_cu_cercuri[uwu][0] - 20, tupla_cu_cercuri[uwu][1] - 20))
                #pygame.draw.circle(screen, circle_color_rosu, tupla_cu_cercuri[uwu], 5)  # are prioritate mai mare
        pygame.time.Clock().tick(24) #max framerate
        pygame.display.flip()  # faceme update mere in running
        if semnal==1:
            semnal=0
            simulate_mouse_motion()
    pygame.quit()
