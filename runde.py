import pygame
from Importuri import *
import numpy as np
from importuri_bgd import *
from Functii import *
from Importuri import *
import pygame
import numpy as np

from importuri_bgd import error_cannot_make_same_move

global al_cui_e_randul
def runda_player_main(mouse_x,mouse_y):
    global nr_sec
    #asta e de facpt ce face botul
    ok=1;
    global al_cui_e_randul
    for x in range(15, 120, 10):
        for q in range(75, 180, 10):
            x = float(x / 10)
            q = float(q / 10)
            if x <= mouse_x / cell_size and mouse_x / cell_size <= x + 1 and q <= mouse_y / cell_size and mouse_y / cell_size <= q + 1:
                # a gasit poz in matrice si e pozitia
                if mat[int(q - 7.5)][int(x - 1.5)] == 2:
                    print("ai facut deja asta, fa altceva!")
                else:
                    nu=0
                    if mat[int(q - 7.5)][int(x - 1.5)] == 1: # am nimerit barca
                        tupla_ai_nimerit[nr_total_cercuri[0]] = 1
                        nu=1
                    mat[int(q - 7.5)][int(x - 1.5)] = 2
                    # a m intervalul dat de variabilele x si x+1 deci
                    tupla_cu_cercuri[nr_total_cercuri[0]][0] = (2 * x + 1) / 2 * cell_size
                    tupla_cu_cercuri[nr_total_cercuri[0]][1] = (2 * q + 1) / 2 * cell_size
                    nr_total_cercuri[0] += 1  # ca sa iau range
                    al_cui_e_randul[0]=nu # mai da o data
            x = x * 10
            q = q * 10
def runda_adversar(mouse_x,mouse_y):
    global nr_sec
    global al_cui_e_randul
    for x in range(130, 220, 10):
        for q in range(75, 180, 10):
            x = float(x / 10)
            q = float(q / 10)
            if x <= mouse_x / cell_size and mouse_x / cell_size <= x + 1 and q <= mouse_y / cell_size and mouse_y / cell_size <= q + 1:
                # a gasit poz in matrice si e pozitia
                if mat_adversar[int(q - 7.5)][int(x - 13)] == 2:
                    error_cannot_make_same_move()
                else:
                    mat_adversar[int(q - 7.5)][int(x - 13)] = 2
                    # a m intervalul dat de variabilele x si x+1 deci
                    tupla_cu_cercuri[nr_total_cercuri[0]][0]=(2 * x + 1) / 2 * cell_size
                    tupla_cu_cercuri[nr_total_cercuri[0]][1]=(2 * q + 1) / 2 * cell_size
                    nr_total_cercuri[0] += 1 # ca sa iau range
                    al_cui_e_randul[0]= 1
                    nr_sec[0]=30
            x = x * 10
            q = q * 10

def runda_bot(mouse_x,mouse_y,trebuie_timer):
    print(mouse_x / cell_size)
    print(mouse_y / cell_size)
    #if(mouse_x / cell_size>17.5):
     #   return
    if(mouse_y/cell_size>17.5):
        trebuie_timer[0] = 1
        return
    if (mouse_x / cell_size > 23.5):
        trebuie_timer[0] = 1
        return
    global nr_sec
    #var=0
    for x in range(130, 230, 10):
        for q in range(75, 180, 10):
            x = float(x / 10)
            q = float(q / 10)
            if x <= mouse_x / cell_size and mouse_x / cell_size <= x + 1 and q <= mouse_y / cell_size and mouse_y / cell_size <= q + 1:
                # a gasit poz in matrice si e pozitia
                if mat_adversar[int(q - 7.5)][int(x - 13)] == 2:
                    merge[1] = 0
                    trebuie_timer[0]=1
                else:
                    merge[1] = 1
                    nu=1
                    if mat_adversar[int(q - 7.5)][int(x - 13)] == 1:
                        tupla_ai_nimerit[nr_total_cercuri[0]] = 1
                        # daca a nimerit ii dau mai mult xp
                        if e_guest[0]==0:
                            adauga_xp_lovire_buna()
                        nu=0#modificat era 0
                    # a ratat
                    else:
                        if e_guest[0] == 0:
                            adauga_xp_ratare()
                    mat_adversar[int(q - 7.5)][int(x - 13)] = 2
                    # a m intervalul dat de variabilele x si x+1 deci
                    tupla_cu_cercuri[nr_total_cercuri[0]][0]=(2 * x + 1) / 2 * cell_size
                    tupla_cu_cercuri[nr_total_cercuri[0]][1]=(2 * q + 1) / 2 * cell_size
                    nr_total_cercuri[0] += 1 # ca sa iau range
                    al_cui_e_randul[0]= nu
                return
            x = x * 10
            q = q * 10
    if al_cui_e_randul[0]==0:
        trebuie_timer[0]=1
def check_if_game_over():
    # verific atat matricea pt bot cat si matricea pentru player
    var_1=1;# termina player
    var_2=2;#termina bot/inamic
    # daca nu mai sunt 1 in matrice
    for i in range(0,9):
        for j in range(0,9):
            if(mat[i][j]==1):
                var_1=0;
                # nu a terminat player_1
    for i in range(0, 9):
        for j in range(0, 9):
            if (mat_adversar[i][j] == 1):
                var_2= 0;
    if var_1==1:
        return var_1
    if var_2==2:
        return var_2
    return 0
    # 1 a terminat 1
    # 2 a terminat bot/adversar
    # 0 nu a temrinat nimeni
