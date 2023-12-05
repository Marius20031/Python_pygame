import pygame
from Importuri import *
import numpy as np
from importuri_bgd import *
from Functii import *
from Importuri import *
import pygame
import numpy as np
global al_cui_e_randul
def runda_player_main(mouse_x,mouse_y):
    print("------------------------")
    ok=1;
    #global al_cui_e_randul
    for x in range(15, 120, 10):
        for q in range(75, 180, 10):
            x = float(x / 10)
            q = float(q / 10)
            if x <= mouse_x / cell_size and mouse_x / cell_size <= x + 1 and q <= mouse_y / cell_size and mouse_y / cell_size <= q + 1:
                print(x)
                print(q)
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
                    print("eok")
            x = x * 10
            q = q * 10
    print("adversar")
    if al_cui_e_randul[0]==1:
        print("mutare invalida aka apasa random ")
    #print(mat)
def runda_adversar(mouse_x,mouse_y):
    print("------------------------")
    #global al_cui_e_randul
    for x in range(130, 220, 10):
        for q in range(75, 180, 10):
            x = float(x / 10)
            q = float(q / 10)
            if x <= mouse_x / cell_size and mouse_x / cell_size <= x + 1 and q <= mouse_y / cell_size and mouse_y / cell_size <= q + 1:
                print(x)
                print(q)
                print("da")
                # a gasit poz in matrice si e pozitia
                if mat_adversar[int(q - 7.5)][int(x - 13)] == 2:
                    print("ai facut deja asta, fa altceva!")
                else:
                    mat_adversar[int(q - 7.5)][int(x - 13)] = 2
                    # a m intervalul dat de variabilele x si x+1 deci
                    tupla_cu_cercuri[nr_total_cercuri[0]][0]=(2 * x + 1) / 2 * cell_size
                    tupla_cu_cercuri[nr_total_cercuri[0]][1]=(2 * q + 1) / 2 * cell_size
                    nr_total_cercuri[0] += 1 # ca sa iau range
                    al_cui_e_randul[0]= 1
            x = x * 10
            q = q * 10
    print("player")
    if al_cui_e_randul[0]==0:
        print("mutare invalida aka apasa random ")
    #print(mat_adversar)

def runda_bot(mouse_x,mouse_y):
    print("------------------------")
    #global al_cui_e_randul
    for x in range(130, 230, 10):
        for q in range(75, 180, 10):
            x = float(x / 10)
            q = float(q / 10)
            if x <= mouse_x / cell_size and mouse_x / cell_size <= x + 1 and q <= mouse_y / cell_size and mouse_y / cell_size <= q + 1:
                print(x)
                print(q)
                print("da")
                # a gasit poz in matrice si e pozitia
                if mat_adversar[int(q - 7.5)][int(x - 13)] == 2:
                    print("ai facut deja asta, fa altceva!")
                else:
                    nu=1
                    if mat_adversar[int(q - 7.5)][int(x - 13)] == 1:
                        tupla_ai_nimerit[nr_total_cercuri[0]] = 1
                        nu=0
                    mat_adversar[int(q - 7.5)][int(x - 13)] = 2
                    # a m intervalul dat de variabilele x si x+1 deci
                    tupla_cu_cercuri[nr_total_cercuri[0]][0]=(2 * x + 1) / 2 * cell_size
                    tupla_cu_cercuri[nr_total_cercuri[0]][1]=(2 * q + 1) / 2 * cell_size
                    nr_total_cercuri[0] += 1 # ca sa iau range
                    al_cui_e_randul[0]= nu
            x = x * 10
            q = q * 10
    print("player")
    if al_cui_e_randul[0]==0:
        print("mutare invalida aka apasa random ")
    #print(mat_adversar)