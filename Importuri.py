import pygame
import numpy as np
# Inceputul
pygame.init()


width, height = 1000, 1000
#Dimensiunea ^^
screen = pygame.display.set_mode((width, height))


Fundal = (44,62,80)
WHITE = (255, 255, 255)
#Vreau sa facfundalul^

#creearea dimensiuniulor pentru barci
board_width, board_height = 400, 400
board_x, board_y = (width - board_width) // 10, (height - board_height) // 2
cell_size = board_width // 10

board2_width, board2_height = 400, 400
board2_x, board2_y = (width - board2_width) // 4 , (height - board2_height) // 2
cell2_size = board2_width // 10
# dimensiunea 2 pentru barci
# Functia de desinare
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Start", True, (255, 255, 255))
button_rect = pygame.Rect(50, 50, 100, 50)

mat = np.zeros((10, 10))
mat_adversar = np.zeros((10, 10))
#--------------------------------

boat_width_1 = 2 * cell_size
boat_height_1 = 1 * cell_size

boat_width_2= 3 * cell_size
boat_height_2 = 1 * cell_size

boat_width_3 = 4 * cell_size
boat_height_3 = 1 * cell_size

boat_width_4 = 5 * cell_size
boat_height_4 = 1 * cell_size

# pozitia initialal a barcilor !!! deci nu aici modific pentru a modifica size.ul barcilor
boats = [
    (4 * cell_size, 19 * cell_size),
    (4 * cell_size, 20 * cell_size),
    (4 * cell_size, 21 * cell_size),
    (4 * cell_size, 22 * cell_size)
]

# boats_size e aia importanta
boats_size = [
    (1 * cell_size, 2 * cell_size),
    (1 * cell_size, 3 * cell_size),
    (1 * cell_size, 4 * cell_size),
    (1 * cell_size, 5 * cell_size)
]

boat_width_VECT=[2,3,4,5]
boat_height_VECT=[1,1,1,1]
# Dvarialbilele follsite pentru drag and drop
selected = None
offset_x = 0
offset_y = 0
# vreau sa implementez sa stie adversarul ca a lovit 2 boat-uri
# variabile reprezentative entru frunctioneara corecta
al_cui_e_randul=[0]  # incepe playerul
nr_total_cercuri=[0]
tupla_cu_cercuri = np.zeros((551, 2))
tupla_ai_nimerit=np.zeros(551)
# afisare eroare
merge=[1,1,1]
jucam_cu_bot=[0]
tin_randomizarea=[-1,-1,-1,-1]
alege_first_time=[1]
var_x=[0]
var_y=[0]
joc_e_gata=[0]
botul_nu_iarta=[0,0]
e_guest=[0]
username_conectat=[""]