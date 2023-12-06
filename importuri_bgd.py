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

fontnormal=pygame.font.Font(None,40)
font=pygame.font.Font("JumboSale Trial.otf",40)
font_mediu=pygame.font.Font("JumboSale Trial.otf",27)
font_mic=pygame.font.Font("JumboSale Trial.otf",25)
text = "Player"
text_surface = font.render(text, True, white)
text_rect = text_surface.get_rect()
text_rect.center = (370, 30)

text2="Bot"
text_surface2=font.render(text2,True,white)
text_rect2=text_surface2.get_rect()
text_rect2.center=(630,30)

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

icon1=pygame.image.load("Photos/828933_cartoon-animal-png.png")
icon1=icon1.convert_alpha()
icon1=pygame.transform.smoothscale(icon1,(43,43))

icon2=pygame.image.load("Photos/828933_cartoon-animal-png.png")
icon2=icon2.convert_alpha()
icon2=pygame.transform.smoothscale(icon1,(43,43))

explozie=pygame.image.load("Photos/Explosion-RED-Graphic-style05_prev_lg.png")
explozie=explozie.convert_alpha()
explozie=pygame.transform.smoothscale(explozie,(70,70))

background=pygame.image.load("Photos/peakpx.jpg")
background=background.convert_alpha()
background=pygame.transform.smoothscale(background,(400, 400))

background2=pygame.image.load("Photos/background2.jpg")
background2=background2.convert_alpha()
background2=pygame.transform.smoothscale(background2,(400, 400))

text_surface8 = font_mediu.render('>', True, black)
text_rect8 = text_surface8.get_rect()
text_rect8.center=(286,61)

text_surface9 = font_mediu.render('<', True, black)
text_rect9 = text_surface9.get_rect()
text_rect9.center=(266,61)


text10="The boats are not in a valid position"
text_surface10=font.render(text10,True,red)
text_rect10=text_surface10.get_rect()
text_rect10.center=(500,200)

text11="to start the game yet !!!"
text_surface11=font.render(text11,True,red)
text_rect11=text_surface11.get_rect()
text_rect11.center=(500,230)

text12="Please wait for your turn !!!"
text_surface12=font.render(text12,True,red)
text_rect12=text_surface12.get_rect()
text_rect12.center=(500,230)

text13="You can`t make the same move twice !!!"
text_surface13=font.render(text13,True,red)
text_rect13=text_surface13.get_rect()
text_rect13.center=(500,200)
text14="Think of a better one !"
text_surface14=font.render(text14,True,red)
text_rect14=text_surface14.get_rect()
text_rect14.center=(500,230)

text15="00"
text_surface15=fontnormal.render(text15,True,white)
text_rect15=text_surface15.get_rect()
text_rect15.center=(480,27)

text16="00"
text_surface16=fontnormal.render(text16,True,white)
text_rect16=text_surface16.get_rect()
text_rect16.center=(542,27)

text18="Your time to make a move has expired !!!"
text_surface18=font.render(text18,True,red)
text_rect18=text_surface18.get_rect()
text_rect18.center=(500,200)
text19="It`s next player`s turn !!!"
text_surface19=font.render(text19,True,red)
text_rect19=text_surface19.get_rect()
text_rect19.center=(500,235)
text20="                                        "
text_surface20=font.render(text20,True,red)
text_rect20=text_surface20.get_rect()
text_rect20.center=(500,200)
text21="                           "
text_surface21=font.render(text21,True,red)
text_rect21=text_surface21.get_rect()
text_rect21.center=(500,235)

def afisare_barci():
    screen.blit(text_surface3, text_rect3)
    screen.blit(text_surface4, text_rect4)
    screen.blit(text_surface5, text_rect5)
    screen.blit(text_surface6, text_rect6)
    screen.blit(text_surface7, text_rect7)
    screen.blit(text_surface8,text_rect8)
    screen.blit(text_surface9,text_rect9)
def show_background():
    screen.blit(background,(60,300))
    screen.blit(background2,(525,300))
def afisare_playeri():
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    screen.blit(icon1,(255,4))
    screen.blit(icon2,(667,4))
def afisare_icon_bot():
    nr = random.randint(1, 5)
    global icon2
    if nr==1:
        icon2 = pygame.image.load("Photos/828933_cartoon-animal-png.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==2:
        icon2 = pygame.image.load("Photos/robot-6187995.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==3:
        icon2 = pygame.image.load("Photos/crab-42880_1920.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==4:
        icon2 = pygame.image.load("Photos/sinterklaas.png")
        icon2 = icon2.convert_alpha()
        icon2 = pygame.transform.smoothscale(icon2, (43, 43))
    elif nr==5:
        icon2 = pygame.image.load("Photos/eggplant-2924511_1920.png")
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
        icon1 = pygame.image.load("Photos/828933_cartoon-animal-png.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==2:
        icon1 = pygame.image.load("Photos/robot-6187995.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==3:
        icon1 = pygame.image.load("Photos/crab-42880_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==4:
        icon1 = pygame.image.load("Photos/sinterklaas.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==5:
        icon1 = pygame.image.load("Photos/eggplant-2924511_1920.png")
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
        icon1 = pygame.image.load("Photos/828933_cartoon-animal-png.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==2:
        icon1 = pygame.image.load("Photos/robot-6187995.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==3:
        icon1 = pygame.image.load("Photos/crab-42880_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==4:
        icon1 = pygame.image.load("Photos/sinterklaas.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
    elif x==5:
        icon1 = pygame.image.load("Photos/eggplant-2924511_1920.png")
        icon1 = icon1.convert_alpha()
        icon1 = pygame.transform.smoothscale(icon1, (43, 43))
def error_boats_not_in_correct_position():
    screen.blit(text_surface10,text_rect10)
    screen.blit(text_surface11,text_rect11)
def error_not_your_turn():   # afiseaza eroarea pt atunci cand nu e randul tau
    screen.blit(text_surface12, text_rect12)
def error_cannot_make_same_move(): # afiseaza eroare daca lovesti in acelasi loc
    screen.blit(text_surface13, text_rect13)
    screen.blit(text_surface14, text_rect14)
def afisare_contur_timer():
    pygame.draw.rect(screen, (0, 0, 0), (450, 2, 125, 50), )
    pygame.draw.rect(screen, (255, 255, 255), (450, 2, 125, 50), 3)
    pygame.draw.rect(screen, (255, 255, 255), (450, 2, 63, 50), 3)
def afisare_timer_default():
    screen.blit(text_surface15,text_rect15)
    screen.blit(text_surface16, text_rect16)
global nr_sec
nr_sec=[30]
def incepe_timer(idx,trebuie_timer,nr_sec):
    sec=nr_sec[0]
    while sec>=0:
        text17 = str(sec)
        if(sec<10):
            text17="0"+text17
        text_surface17 = fontnormal.render(text17, True, white)
        text_rect17 = text_surface17.get_rect()
        if idx==0:
            text_rect17.center = (480, 27)
        else:
            text_rect17.center = (542, 27)
        afisare_contur_timer()
        screen.blit(text_surface17,text_rect17)
        pygame.display.update(text_rect17)
        sec-=1
        pygame.time.delay(1000)
        if(sec==-1):
            screen.blit(text_surface18,text_rect18)
            screen.blit(text_surface19,text_rect19)
            pygame.display.update(text_rect18)
            pygame.display.update(text_rect19)
            pygame.time.delay(2500)
            pygame.draw.rect(screen, (44,62,80), (100,180, 800, 90) )
            pygame.display.update((100,180, 800, 90))
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type== pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                trebuie_timer[0]=0
                nr_sec[0]=sec
                return event
#pana aici scris de mn
