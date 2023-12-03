import pygame
from Functii import *
from PIL import Image
# Inceputul
pygame.init()

#scris de mn
white = (255, 255, 255)
font=pygame.font.Font("JumboSale Trial.otf",36)
text = "Player"
text_surface = font.render(text, True, white)
text_rect = text_surface.get_rect()
text_rect.center = (400, 30)

text2="Bot"
text_surface2=font.render(text2,True,white)
text_rect2=text_surface2.get_rect()
text_rect2.center=(600,30)


def afisare_playeri():
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)

#pana aici scris de mn
