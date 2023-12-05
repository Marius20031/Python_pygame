import pygame
from Functii import *
import random
# Inceputul
pygame.init()

#scris de mn
white = (255, 255, 255)
black=(0,0,0)
red=(255,0,0)
x=1

font=pygame.font.Font("JumboSale Trial.otf",40)
font_mediu=pygame.font.Font("JumboSale Trial.otf",27)
font_mic=pygame.font.Font("JumboSale Trial.otf",25)
text = "Player"
text_surface = font.render(text, True, white)
text_rect = text_surface.get_rect()
text_rect.center = (400, 30)

text2="Bot"
text_surface2=font.render(text2,True,white)
text_rect2=text_surface2.get_rect()
text_rect2.center=(600,30)

text3="Place the boats as you wish:"
text_surface3=font_mediu.render(text3,True,white)
text_rect3=text_surface3.get_rect()
text_rect3.center=(247,740)

text4="Boat A:"
text_surface4=font_mic.render(text4,True,white)
text_rect4=text_surface4.get_rect()
text_rect4.center=(105,790)

text5="Boat B:"
text_surface5=font_mic.render(text5,True,white)
text_rect5=text_surface5.get_rect()
text_rect5.center=(105,830)

text6="Boat C:"
text_surface6=font_mic.render(text6,True,white)
text_rect6=text_surface6.get_rect()
text_rect6.center=(105,870)

text7="Boat D:"
text_surface7=font_mic.render(text7,True,white)
text_rect7=text_surface7.get_rect()
text_rect7.center=(105,910)

icon1=pygame.image.load("828933_cartoon-animal-png.png")
icon1=icon1.convert_alpha()
icon1=pygame.transform.smoothscale(icon1,(43,43))

icon2=pygame.image.load("828933_cartoon-animal-png.png")
icon2=icon2.convert_alpha()
icon2=pygame.transform.smoothscale(icon1,(43,43))

text_surface8 = font_mediu.render('>', True, black)
text_rect8 = text_surface8.get_rect()
text_rect8.center=(307,61)

text_surface9 = font_mediu.render('<', True, black)
text_rect9 = text_surface9.get_rect()
text_rect9.center=(286,61)


text10="The boats are not in a valid position"
text_surface10=font.render(text10,True,red)
text_rect10=text_surface10.get_rect()
text_rect10.center=(500,200)
text11="to start the game yet !!!"
text_surface11=font.render(text11,True,red)
text_rect11=text_surface11.get_rect()
text_rect11.center=(500,230)



def afisare_barci():
    screen.blit(text_surface3, text_rect3)
    screen.blit(text_surface4, text_rect4)
    screen.blit(text_surface5, text_rect5)
    screen.blit(text_surface6, text_rect6)
    screen.blit(text_surface7, text_rect7)
    screen.blit(text_surface8,text_rect8)
    screen.blit(text_surface9,text_rect9)

def afisare_playeri():
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    screen.blit(icon1,(275,4))
    screen.blit(icon2,(650,4))
def afisare_icon_bot():
    nr = random.randint(1, 5)
    global icon2
    if nr==1:
        icon2 = pygame.image.load("828933_cartoon-animal-png.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==2:
        icon2 = pygame.image.load("robot-6187995.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==3:
        icon2 = pygame.image.load("crab-42880_1920.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==4:
        icon2 = pygame.image.load("sinterklaas.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==5:
        icon2 = pygame.image.load("eggplant-2924511_1920.png")
        icon2 = icon1.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
def shift_right_icon():
    global x
    global icon1
    if x<5:
        x+=1
    else:
        x=1
    if x==1:
        icon1 = pygame.image.load("828933_cartoon-animal-png.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==2:
        icon1 = pygame.image.load("robot-6187995.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==3:
        icon1 = pygame.image.load("crab-42880_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==4:
        icon1 = pygame.image.load("sinterklaas.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==5:
        icon1 = pygame.image.load("eggplant-2924511_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))

def shift_left_icon():
    global x
    global icon1
    if x>1:
        x-=1
    else:
        x=5
    if x==1:
        icon1 = pygame.image.load("828933_cartoon-animal-png.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==2:
        icon1 = pygame.image.load("robot-6187995.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==3:
        icon1 = pygame.image.load("crab-42880_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==4:
        icon1 = pygame.image.load("sinterklaas.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==5:
        icon1 = pygame.image.load("eggplant-2924511_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
def error_boats_not_in_correct_position():
    screen.blit(text_surface10,text_rect10)
    screen.blit(text_surface11,text_rect11)

#pana aici scris de mn