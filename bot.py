from asyncio import sleep
from random import random
import pygame
from Importuri import *
from runde import *
import numpy as np
from importuri_bgd import *

def functie_reapelata_pt_randomizare():
    # folosim matrice adversar
    # cu random o sa imi aleg o linie de la 1 la 10:

    # asta in loop eventual:
    random_number_1 = random.randint(0, 9)
    random_number_2 = random.randint(0, 9)
    random_number_coloana = random.randint(0, 9)
    random_number_line = random.randint(0, 9)
    random_number_boat = random.randint(0, 3)
    # imi alege barca
    dimensiune = random_number_boat + 2  # 2 3 4 5 dimensiunile
    # imi caut dimensiune libera
    # mi.a genera o linie si o coloana, acum ma intereseaza daca e destul de mare
    # daca e destul cat sa se puna pe orizontala o sa adaug diferenta daca nu, ramane asa si testam:
    # verific coloana
    rotatie=random.randint(0,1); # pentru vertical si orziontal
    if(rotatie==1):
        for v in range(0,4):
            if dimensiune==tin_randomizarea[v]:
                return 0

        if random_number_coloana+dimensiune > 9:
            random_number_coloana = 9 - dimensiune
        for i in range(0, dimensiune):
            # ca sa ma asigur ca e random random
            if mat_adversar[random_number_1][random_number_coloana+i]==1:
                return 0
        for i in range(0, dimensiune):
            mat_adversar[random_number_1][random_number_coloana + i] = 1
        # ok urmatoarea vreau sa fie pe verticala
        for i in range(0,4):
            if tin_randomizarea[i]==-1:
                tin_randomizarea[i] = dimensiune
                break
        return 1 # a mers
    else:
        for v in range(0, 4):
            if dimensiune == tin_randomizarea[v]:
                return 0

        if random_number_line + dimensiune > 9:
            random_number_line = 9 - dimensiune
        for i in range(0, dimensiune):
            # ca sa ma asigur ca e random random
            if mat_adversar[random_number_line+i][random_number_coloana] == 1:
                return 0
        for i in range(0, dimensiune):
            mat_adversar[random_number_line+i][random_number_coloana] = 1
        for i in range(0, 4):
            if tin_randomizarea[i] == -1:
                tin_randomizarea[i] = dimensiune
                break
        return 1  # a mers

def creare_matrice_barci_poz():
    var=0
    for i in range(0,4):
        while(functie_reapelata_pt_randomizare()==0):
            var=0 #nimic
    print(mat_adversar)
    # generaza pana merge generarea deci e bine
    #functie_reapelata_pt_randomizare
def bot_alege_pozitie():
    ok=0
    if alege_first_time[0]==1:
        alege_first_time[0]=0
        # aleg random o pozitie de pe matrice
        var_x[0] = random.randint(0, 9)
        var_y[0] = random.randint(0,9)
        var_x[0]=(var_x[0]+1.5)*cell_size+0.2
        var_y[0]=(var_y[0]+7.5) * cell_size+0.2
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