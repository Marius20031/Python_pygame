import pygame
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
    (2 * cell_size, 1 * cell_size),
    (3 * cell_size, 2 * cell_size),
    (4 * cell_size, 3 * cell_size),
    (5 * cell_size, 4 * cell_size)
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

