from random import random
import pygame
from Importuri import *
from runde import *
import numpy as np
from importuri_bgd import *

def functie_reapelata_pt_randomizare():
    #print("aaaaaaaaaaaaaaa??")
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
    #print("wtf?")
    for v in range(0,4):
        if dimensiune==tin_randomizarea[v]:
            return 0
    if 9 - random_number_coloana < dimensiune:
        random_number_coloana = 9 - dimensiune
    #print("wtf?")
    #var_finala = random.randint(random_number_2, random_number_1)
    for i in range(0, dimensiune):
        # ca sa ma asigur ca e random random
        if mat_adversar[random_number_1][random_number_coloana-i]==1:
            return 0
    #print("wtf?")
    for i in range(0, dimensiune):
        mat_adversar[random_number_1][random_number_coloana - i] = 1
    # ok urmatoarea vreau sa fie pe verticala
    variabila=0
    for i in range(0,4):
        if tin_randomizarea[i]==-1:
            tin_randomizarea[i] = dimensiune
            break
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
    print(mat_adversar)