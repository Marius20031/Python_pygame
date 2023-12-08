import pygame
from Functii import *
import random

from full_database import *

# Inceputul
pygame.init()
pygame.display.set_caption('Ship Wars')
#scris de mn
white = (255, 255, 255)
black=(0,0,0)
red=(255,0,0)
gri=(53,60,64)
albastru=(0,66,66)
green=(0,255,0)
x=1

fontnormal=pygame.font.Font(None,40)
font=pygame.font.Font("JumboSale Trial.otf",40)
font_urias=pygame.font.Font("JumboSale Trial.otf",100)
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


fundal=pygame.image.load("Photos/fundal.jpg")
fundal=fundal.convert_alpha()
fundal=pygame.transform.smoothscale(fundal,(1000,1000))

x_mare=pygame.image.load("Photos/2048px-Red_x.svg.png")
x_mare=x_mare.convert_alpha()
x_mare=pygame.transform.smoothscale(x_mare,(45,40))

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
def incepe_timer(idx,trebuie_timer,nr_sec,wait_time,bot):
    sec=nr_sec[0]
    afisare_contur_timer()
    if (idx == 0):
        text17 = "00"
        text_surface17 = fontnormal.render(text17, True, white)
        text_rect17 = text_surface17.get_rect()
        text_rect17.center = (542, 27)
        screen.blit(text_surface17, text_rect17)
        pygame.display.update(text_rect17)
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
        if bot==1:
            if wait_time==-1:
                sec=-2
            wait_time-=1
        if(sec==-1):
            trebuie_timer[0]=0
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


back = pygame.image.load("Photos/fundal turcoa.jpg")
back = back.convert_alpha()
back = pygame.transform.smoothscale(back, (1000,1000))

text_menu = "Main Menu"
text_surface_menu = font_urias.render(text_menu, True, white)
text_rect_menu = text_surface_menu.get_rect()
text_rect_menu.center = (500, 70)

font_meniu=pygame.font.Font("JumboSale Trial.otf",60)


text_22 = "->    Leaderboard"
text_surface_22 = font_meniu.render(text_22, True, white)
text_rect_22 = text_surface_22.get_rect()
text_rect_22.center = (390, 300)

text_23 = "~~Ship Wars~~"
text_surface_23 = font_meniu.render(text_23, True, white)
text_rect_23 = text_surface_23.get_rect()
text_rect_23.center = (500, 150)

text_24 = "->     Login"
text_surface_24 = font_meniu.render(text_24, True, white)
text_rect_24 = text_surface_24.get_rect()
text_rect_24.center = (290, 700)


text_25 = "->     Play as guest"
text_surface_25 = font_meniu.render(text_25, True, white)
text_rect_25 = text_surface_25.get_rect()
text_rect_25.center = (413, 900)
text_rect_25.inflate(30,20)

text_26 = "->     Create Account"
text_surface_26 = font_meniu.render(text_26, True, white)
text_rect_26 = text_surface_26.get_rect()
text_rect_26.center = (440, 500)

text_27 = "Create Account"
text_surface_27 = font_urias.render(text_27, True, white)
text_rect_27 = text_surface_27.get_rect()
text_rect_27.center = (500, 60)

text_28 = "Please create your credentials:"
text_surface_28 = font_meniu.render(text_28, True, white)
text_rect_28 = text_surface_28.get_rect()
text_rect_28.center = (500, 250)

text_29 = "Username:"
text_surface_29 = font.render(text_29, True, white)
text_rect_29 = text_surface_29.get_rect()
text_rect_29.center = (200, 400)

text_30 = "Password:"
text_surface_30 = font.render(text_30, True, white)
text_rect_30 = text_surface_30.get_rect()
text_rect_30.center = (210, 600)

text_31 = "Login to your account"
text_surface_31 = pygame.font.Font("JumboSale Trial.otf",90).render(text_31, True, white)
text_rect_31 = text_surface_31.get_rect()
text_rect_31.center = (500, 60)

text_32 = "Please input your credentials:"
text_surface_32 = font_meniu.render(text_32, True, white)
text_rect_32 = text_surface_32.get_rect()
text_rect_32.center = (500, 200)

text_33 = "Go back"
text_surface_33 = font.render(text_33, True, white)
text_rect_33 = text_surface_33.get_rect()
text_rect_33.center = (150,965)

text_34 = "Create"
text_surface_34 = font.render(text_34, True, white)
text_rect_34 = text_surface_34.get_rect()
text_rect_34.center = (490,700)

text_35 = "Login"
text_surface_35 = font.render(text_35, True, white)
text_rect_35 = text_surface_35.get_rect()
text_rect_35.center = (490,700)

text_36 = "Username already exists !!!"
text_surface_36 = font_meniu.render(text_36, True, red)
text_rect_36 = text_surface_36.get_rect()
text_rect_36.center = (500,800)

text_37 = "Credentials are wrong !!!"
text_surface_37 = font_meniu.render(text_37, True, red)
text_rect_37 = text_surface_37.get_rect()
text_rect_37.center = (500,800)

text_38 = "Account created !!!"
text_surface_38 = font_meniu.render(text_38, True, green)
text_rect_38 = text_surface_38.get_rect()
text_rect_38.center = (500,800)

text_39 = "Logged in succesfully !!!"
text_surface_39 = font_meniu.render(text_39, True, green)
text_rect_39 = text_surface_39.get_rect()
text_rect_39.center = (500,800)

leaderboard = pygame.image.load("Photos/leaderboard_4489663.png")
leaderboard = leaderboard.convert_alpha()
leaderboard = pygame.transform.smoothscale(leaderboard, (100,100))

create_account = pygame.image.load("Photos/create-account-icon.png")
create_account = create_account.convert_alpha()
create_account = pygame.transform.smoothscale(create_account, (100,100))

login = pygame.image.load("Photos/login_152533.png")
login = login.convert_alpha()
login= pygame.transform.smoothscale(login, (100,100))

guest = pygame.image.load("Photos/guest-512 (1).png")
guest = guest.convert_alpha()
guest= pygame.transform.smoothscale(guest, (80,80))

lacat = pygame.image.load("Photos/pngwing.com.png")
lacat = lacat.convert_alpha()
lacat= pygame.transform.smoothscale(lacat, (70,80))

goback = pygame.image.load("Photos/go-back-arrow-svgrepo-com (1).png")
goback = goback.convert_alpha()
goback= pygame.transform.smoothscale(goback, (50,50))

hide = pygame.image.load("Photos/action-hide-password-512.png")
hide = hide.convert_alpha()
hide= pygame.transform.smoothscale(hide, (70,70))
hide_rect=hide.get_rect()
hide_rect.topleft=(770,565)

username_input = pygame.Rect(320, 370, 450, 60)  # Username input box rectangle (x, y, width, height)
password_input = pygame.Rect(320, 570, 450, 60)  # Password input box rectangle (x, y, width, height)
ellipse_rect = pygame.Rect(425,650,200,100)

def enter_menu(mai_continua):
    stai_in_meniu=True
    show_credentials=0
    show_password=0
    in_ce_scrii=0
    username_text=""
    password_text=""
    password_text_secret=""
    x=-1
    global username_conectat
    while(stai_in_meniu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mai_continua[0] = 0
                stai_in_meniu=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if text_rect_25.collidepoint(event.pos):
                    #setat variabila
                    print("plm")
                    stai_in_meniu=False
                if text_rect_26.collidepoint(event.pos):
                    show_credentials=1
                    x=-1
                if text_rect_24.collidepoint(event.pos):
                    x=-1
                    show_credentials=2
                if username_input.collidepoint(event.pos):
                    in_ce_scrii=1
                if password_input.collidepoint(event.pos):
                    in_ce_scrii = 2
                if hide_rect.collidepoint(event.pos):
                    if show_password==0:
                        show_password=1
                    else:
                        show_password=0
                    print(show_password)
                if ellipse_rect.collidepoint(event.pos):
                    print("apas")
                    if show_credentials==1:
                        x=create_try(username_text,password_text)  #aici am apleat functia, x ar trebui sa aiba valoarea de return buna
                        if x==0:
                            username_conectat=username_text
                    else:
                        x=login_try(username_text,password_text)
                        if x==0:
                            username_conectat=username_text

                if text_rect_22.collidepoint(event.pos):
                    show_credentials=3
                if text_rect_33.collidepoint(event.pos):
                    x=-1
                    show_credentials=0
                    password_text=""
                    password_text_secret=""
                    username_text=""
            if event.type==pygame.KEYDOWN:
                if in_ce_scrii==1:
                    if event.key== pygame.K_BACKSPACE:
                        username_text=username_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        #inseamna ca s a terminat citirea userului desi idk
                        print("mere")
                    else:
                        if len(username_text)<20:
                            username_text+=event.unicode
                elif in_ce_scrii==2:
                    if event.key== pygame.K_BACKSPACE:
                        password_text=password_text[:-1]
                        password_text_secret=password_text_secret[:-1]
                    elif event.key == pygame.K_RETURN:
                        #inseamna ca s a terminat citirea userului desi idk
                        print("mere")
                    else:
                        if len(password_text)<15:
                            password_text+=event.unicode
                            password_text_secret+="*"

        screen.blit(back,(0,0))
        if show_credentials==0:
            screen.blit(text_surface_menu,text_rect_menu)
            screen.blit(leaderboard,(30,230))
            screen.blit(create_account,(30,440))
            screen.blit(login,(30,645))
            screen.blit(guest,(30,840))
            screen.blit(text_surface_23,text_rect_23)
            screen.blit(text_surface_22,text_rect_22)
            screen.blit(text_surface_24,text_rect_24)
            screen.blit(text_surface_25,text_rect_25)
            screen.blit(text_surface_26,text_rect_26)
        elif show_credentials==3:
            screen.blit(goback, (20, 930))
            screen.blit(text_surface_33, text_rect_33)
        elif show_credentials==1:
            screen.blit(text_surface_27,text_rect_27)
            screen.blit(text_surface_28,text_rect_28)
            screen.blit(guest,(30,350))
            screen.blit(lacat,(30,550))
            screen.blit(text_surface_29,text_rect_29)
            screen.blit(text_surface_30,text_rect_30)
            pygame.draw.rect(screen, black, username_input, 4)
            pygame.draw.rect(screen, black, password_input, 4)
            screen.blit(goback, (20, 930))
            screen.blit(text_surface_33, text_rect_33)
            screen.blit(hide,hide_rect)
            pygame.draw.ellipse(screen,albastru,(390, 650, 200, 100))
            pygame.draw.ellipse(screen, white, (390, 650, 200, 100),5)
            screen.blit(text_surface_34,text_rect_34)
            if x==1: #nu are succes
                screen.blit(text_surface_36,text_rect_36)
            elif x==0:
                screen.blit(text_surface_38,text_rect_38)
            username_surface = font.render(username_text, True, black)
            if show_password==0:
                password_surface = pygame.font.Font("JumboSale Trial.otf",55).render(password_text_secret, True, black)
            else:
                password_surface = pygame.font.Font("JumboSale Trial.otf",55).render(password_text, True, black)
            screen.blit(username_surface, (username_input.x + 5, username_input.y + 10))
            if show_password == 0:
                screen.blit(password_surface, (password_input.x + 5, password_input.y + 15))
            else:
                screen.blit(password_surface, (password_input.x + 5, password_input.y + 6))
        elif show_credentials==2:
            screen.blit(text_surface_31, text_rect_31)
            screen.blit(text_surface_32, text_rect_32)
            screen.blit(guest, (30, 350))
            screen.blit(lacat, (30, 550))
            screen.blit(text_surface_29, text_rect_29)
            screen.blit(text_surface_30, text_rect_30)
            pygame.draw.rect(screen, black, username_input, 4)
            pygame.draw.rect(screen, black, password_input, 4)
            screen.blit(goback,(20,930))
            screen.blit(hide,hide_rect)
            screen.blit(text_surface_33,text_rect_33)
            pygame.draw.ellipse(screen, albastru, (390, 650, 200, 100))
            pygame.draw.ellipse(screen, white, (390, 650, 200, 100),5)
            screen.blit(text_surface_35, text_rect_35)
            if x==1: #nu are succes
                screen.blit(text_surface_37,text_rect_37)
            elif x==0:
                screen.blit(text_surface_39,text_rect_39)
            username_surface = font.render(username_text, True, black)
            if show_password==0:
                password_surface = pygame.font.Font("JumboSale Trial.otf",55).render(password_text_secret, True, black)
            else:
                password_surface = pygame.font.Font("JumboSale Trial.otf",55).render(password_text, True, black)
            screen.blit(username_surface, (username_input.x + 5, username_input.y + 10))
            if show_password==0:
                screen.blit(password_surface, (password_input.x + 5, password_input.y + 15))
            else:
                screen.blit(password_surface, (password_input.x + 5, password_input.y + 6))
        pygame.display.flip()

#pana aici scris de mn