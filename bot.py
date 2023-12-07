from asyncio import sleep
from random import random
import pygame
from Importuri import *
from runde import *
import numpy as np
from importuri_bgd import *

def functie_reapelata_pt_randomizare():
    ###print("aaaaaaaaaaaaaaa??")
    # folosim matrice adversar
    # cu random o sa imi aleg o linie de la 1 la 10:

    # asta in loop eventual:
    random_number_1 = random.randint(0, 9)
    random_number_2 = random.randint(0, 9)
    random_number_coloana = random.randint(0, 9)
    random_number_boat = random.randint(0, 3)
    # imi alege barca
    dimensiune = random_number_boat + 2  # 2 3 4 5 dimensiunile
    # imi caut dimensiune libera
    # mi.a genera o linie si o coloana, acum ma intereseaza daca e destul de mare
    # daca e destul cat sa se puna pe orizontala o sa adaug diferenta daca nu, ramane asa si testam:
    # verific coloana
    ###print("wtf?")
    for v in range(0,4):
        if dimensiune==tin_randomizarea[v]:
            return 0
    if random_number_coloana+dimensiune > 9: #fixed bug
        random_number_coloana = 9 - dimensiune
    ###print("wtf?")
    #var_finala = random.randint(random_number_2, random_number_1)
    for i in range(0, dimensiune):
        # ca sa ma asigur ca e random random
        if mat_adversar[random_number_1][random_number_coloana+i]==1:
            return 0
    ###print("wtf?")
    for i in range(0, dimensiune):
        mat_adversar[random_number_1][random_number_coloana + i] = 1
    # ok urmatoarea vreau sa fie pe verticala
    variabila=0
    for i in range(0,4):
        if tin_randomizarea[i]==-1:
            tin_randomizarea[i] = dimensiune
            break
    ##print("-----------------------------")
    ###print(mat_adversar)
    return 1 # a mers
def creare_matrice_barci_poz():
    var=0
    for i in range(0,4):
        while(functie_reapelata_pt_randomizare()==0):
            var=0 #nimic
    # generaza pana merge generarea deci e bine
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    #functie_reapelata_pt_randomizare
    ##print(mat_adversar)
def bot_alege_pozitie():
    ok=0
    if alege_first_time[0]==1:
        #sleep(3)
        alege_first_time[0]=0
        # aleg random o pozitie de pe matrice
        var_x[0] = random.randint(0, 9)
        var_y[0] = random.randint(0,9)
        var_x[0]=(var_x[0]+1.5)*cell_size+0.2
        var_y[0]=(var_y[0]+7.5) * cell_size+0.2
        #runda_player_main(var_x*cell_size+v)
    else:
        while(ok==0):
            var_x[0] = random.randint(0, 9)
            var_y[0] = random.randint(0, 9)
            # practic vreau ca botul daca a nimerit random 1 sa ia toata barca, that tryhardd
            if mat[botul_nu_iarta[1]][botul_nu_iarta[0]]==1:
                var_y[0]=botul_nu_iarta[1]
                var_x[0]=botul_nu_iarta[0] # sa mearga mai bine botul
            if (mat[var_y[0]][var_x[0]]!=2):
                # nu am lovit.o deja
                ok=1
            if (mat[var_y[0]][var_x[0]]==1):
                # sa nu iasa
                if var_y[0]+1<9 and mat[var_y[0]+1][var_x[0]]==1:
                    botul_nu_iarta[1]=var_y[0]+1
                    botul_nu_iarta[0] = var_x[0]
                if var_y[0]-1>0 and mat[var_y[0]-1][var_x[0]]==1:
                    botul_nu_iarta[1]=var_y[0]-1
                    botul_nu_iarta[0] = var_x[0]
                if var_x[0] + 1 < 9 and mat[var_y[0]][var_x[0]+1] == 1:
                    botul_nu_iarta[1] = var_y[0]
                    botul_nu_iarta[0] = var_x[0]+1
                if var_x[0] - 1 > 0 and mat[var_y[0]][var_x[0]-1] == 1:
                    botul_nu_iarta[1] = var_y[0]
                    botul_nu_iarta[0] = var_x[0]-1
            var_x[0] = (var_x[0] + 1.5) * cell_size + 0.2
            var_y[0] = (var_y[0] + 7.5) * cell_size + 0.2
