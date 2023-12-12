import pygame
from Importuri import *
from full_database import *
from Functii import *
import random



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
gold=(255,223,0)
bronze=(205,127,50)
silver=(165,169,180)
x=1

fontnormal=pygame.font.Font(None,40)
fontnormal2=pygame.font.Font(None,70)
font=pygame.font.Font("JumboSale Trial.otf",40)
font_urias=pygame.font.Font("JumboSale Trial.otf",100)
font_mediu=pygame.font.Font("JumboSale Trial.otf",27)
font_mic=pygame.font.Font("JumboSale Trial.otf",25)
font_meniu=pygame.font.Font("JumboSale Trial.otf",60)

global nume_player
nume_player=""


text2="Bot"
text_surface2=fontnormal2.render(text2,True,gri)
text_rect2=text_surface2.get_rect()
text_rect2.center=(630,30)

text3="Place the boats as you wish:"
text_surface3=font_mediu.render(text3,True,white)
text_rect3=text_surface3.get_rect()
text_rect3.center=(247,740)

text71="Press this to rotate the"
text_surface71=font_mediu.render(text71,True,white)
text_rect_71=text_surface71.get_rect()
text_rect_71.center=(720,740)

text73="Press this to start the game:"
text_surface73=font_mediu.render(text73,True,gri)
text_rect_73=text_surface73.get_rect()
text_rect_73.center=(200,110)

text72="selected boat:"
text_surface72=font_mediu.render(text72,True,white)
text_rect_72=text_surface72.get_rect()
text_rect_72.center=(720,780)

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
text_rect8.center=(180,61)

text_surface9 = font_mediu.render('<', True, black)
text_rect9 = text_surface9.get_rect()
text_rect9.center=(160,61)


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
    screen.blit(text_surface71,text_rect_71)
    screen.blit(text_surface72, text_rect_72)
    rotate_button = pygame.Rect(660, 800, 120, 50)
    pygame.draw.rect(screen, albastru, rotate_button)
    button_text = button_font.render("Rotate", True, (255, 255, 255))
    screen.blit(button_text, (682, 813))
    screen.blit(text_surface73,text_rect_73)

    start_button = pygame.Rect(430, 80, 120, 50)
    pygame.draw.rect(screen, albastru, start_button)
    button_text_1 = button_font.render("Start", True, (255, 255, 255))
    screen.blit(button_text_1, (460, 92))



def show_background():
    screen.blit(background,(60,300))
    screen.blit(background2,(525,300))
def afisare_playeri():
    text = nume_player
    text_surface = fontnormal2.render(text, True, gri)
    text_rect = text_surface.get_rect()
    text_rect.center = (315, 30)
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    screen.blit(icon1,(150,4))
    screen.blit(icon2,(680,4))
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
                nr_sec[0]=sec
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
text_rect_33.center = (155,965)

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

text_40 = "Start Game"
text_surface_40 = font.render(text_40, True, white)
text_rect_40 = text_surface_40.get_rect()
text_rect_40.center = (800,965)

text_41 = "Login"
text_surface_41 = font.render(text_41, True, white)
text_rect_41 = text_surface_41.get_rect()
text_rect_41.center = (870,965)

text_42 = "Leaderboard"
text_surface_42 = font_urias.render(text_42, True, white)
text_rect_42 = text_surface_42.get_rect()
text_rect_42.center = (500,60)

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

gof = pygame.image.load("Photos/go-back-arrow-svgrepo-com (3).png")
gof = gof.convert_alpha()
gof= pygame.transform.smoothscale(gof, (50,50))

hide = pygame.image.load("Photos/action-hide-password-512.png")
hide = hide.convert_alpha()
hide= pygame.transform.smoothscale(hide, (70,70))
hide_rect=hide.get_rect()
hide_rect.topleft=(770,565)

text_43 = "Username"
text_surface_43 = font_meniu.render(text_43, True, white)
text_rect_43 = text_surface_43.get_rect()
text_rect_43.center = (370,200)

text_44 = "Level"
text_surface_44 = font_meniu.render(text_44, True, white)
text_rect_44 = text_surface_44.get_rect()
text_rect_44.center = (675,200)

text_45 = "XP"
text_surface_45 = font_meniu.render(text_45, True, white)
text_rect_45 = text_surface_45.get_rect()
text_rect_45.center = (860,200)

text_46 = "Pos."
text_surface_46 = font_meniu.render(text_46, True, white)
text_rect_46 = text_surface_46.get_rect()
text_rect_46.center = (117,200)

text_47 = "1"
text_surface_47 = fontnormal2.render(text_47, True, gold)
text_rect_47 = text_surface_47.get_rect()
text_rect_47.center = (117,280)

text_48 = "2"
text_surface_48 = fontnormal2.render(text_48, True, silver)
text_rect_48 = text_surface_48.get_rect()
text_rect_48.center = (117,380)

text_49 = "3"
text_surface_49 = fontnormal2.render(text_49, True, bronze)
text_rect_49 = text_surface_49.get_rect()
text_rect_49.center = (117,480)

text_50 = "4"
text_surface_50 = fontnormal2.render(text_50, True, white)
text_rect_50 = text_surface_50.get_rect()
text_rect_50.center = (117,580)

text_51 = "5"
text_surface_51 = fontnormal2.render(text_51, True, white)
text_rect_51 = text_surface_51.get_rect()
text_rect_51.center = (117,680)

text_52 = ".."
text_surface_52 = font_meniu.render(text_52, True, white)
text_rect_52 = text_surface_52.get_rect()
text_rect_52.center = (117,780)

text_53 = ".........."
text_surface_53 = font_meniu.render(text_53, True, white)
text_rect_53 = text_surface_53.get_rect()
text_rect_53.center = (370,780)

text_54 = "...."
text_surface_54 = font_meniu.render(text_54, True, white)
text_rect_54 = text_surface_54.get_rect()
text_rect_54.center = (675,780)

text_55 = "Game starts in:"
text_surface_55 = font_urias.render(text_55, True, black)
text_rect_55 = text_surface_55.get_rect()
text_rect_55.center = (500,100)
def show_text_timer():
    screen.blit(text_surface_55,text_rect_55)

username_input = pygame.Rect(320, 370, 450, 60)  # Username input box rectangle (x, y, width, height)
password_input = pygame.Rect(320, 570, 450, 60)  # Password input box rectangle (x, y, width, height)
ellipse_rect = pygame.Rect(425,650,200,100)

def enter_menu(mai_continua):
    date_leaderboard = [
        ["Andrei", "3", "650"],
        ["Rares", "2", "550"],
        ["Ana", "1", "500"],
        ["Andreea", "0", "300"],
        ["Gabi", "0", "200"]
    ]
    stai_in_meniu=True
    show_credentials=0
    show_password=0
    in_ce_scrii=0
    username_text=""
    password_text=""
    password_text_secret=""
    x=-1
    global e_guest
    global username_conectat
    global nume_player
    while(stai_in_meniu):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mai_continua[0] = 0
                stai_in_meniu=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if text_rect_25.collidepoint(event.pos):
                    #setat variabila
                    e_guest[0]=1
                    nume_player=random_guest_name()
                    stai_in_meniu=False
                if x==0:
                    if show_credentials==2:
                        if text_rect_40.collidepoint(event.pos):
                            nume_player=username_conectat[0]
                            stai_in_meniu=False
                    else:
                        if text_rect_41.collidepoint(event.pos):
                            show_credentials=2
                            x=-1
                            password_text = ""
                            password_text_secret = ""
                            username_text = ""
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
                            username_conectat[0]=username_text
                        #x=0 #asta trb sters, e doar pt ca n am baza de date
                    else:
                        x=login_try(username_text,password_text)   ####trb decomentat
                        if x==0:
                            username_conectat[0]=username_text
                        #x=0# trb sters,pus ca n am baza de date

                if text_rect_22.collidepoint(event.pos):
                    show_credentials=3

                    ## !!! aici trb apelata functia care modifica matricea de leaderboard sau o returneaza idk, nu conteaza !!!  ##
                    # cv gen get_leaderboad(date_leaderboard)
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
                    else:
                        if len(username_text)<20:
                            username_text+=event.unicode
                elif in_ce_scrii==2:
                    if event.key== pygame.K_BACKSPACE:
                        password_text=password_text[:-1]
                        password_text_secret=password_text_secret[:-1]
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
        elif show_credentials==3:                       #leaderboard
            screen.blit(goback, (20, 930))
            screen.blit(text_surface_33, text_rect_33)
            screen.blit(text_surface_42,text_rect_42)
            pygame.draw.line(screen, WHITE, (50,150),(50,830), 5)
            pygame.draw.line(screen, WHITE, (180,150),(180,830), 5)
            pygame.draw.line(screen, WHITE, (580,150),(580,830), 5)
            pygame.draw.line(screen, WHITE, (770,150),(770,830), 5)
            pygame.draw.line(screen, WHITE, (950,150),(950,830), 5)
            pygame.draw.line(screen, WHITE, (48,150),(952,150), 5)
            pygame.draw.line(screen, WHITE, (48,230),(952,230), 5)
            pygame.draw.line(screen, WHITE, (48,330),(952,330), 5)
            pygame.draw.line(screen, WHITE, (48,430),(952,430), 5)
            pygame.draw.line(screen, WHITE, (48,530),(952,530), 5)
            pygame.draw.line(screen, WHITE, (48,630),(952,630), 5)
            pygame.draw.line(screen, WHITE, (48,730),(952,730), 5)
            pygame.draw.line(screen, WHITE, (48,830),(952,830), 5)
            screen.blit(text_surface_43,text_rect_43)
            screen.blit(text_surface_44,text_rect_44)
            screen.blit(text_surface_45,text_rect_45)
            screen.blit(text_surface_46,text_rect_46)
            screen.blit(text_surface_47,text_rect_47)
            screen.blit(text_surface_48, text_rect_48)
            screen.blit(text_surface_49, text_rect_49)
            screen.blit(text_surface_50, text_rect_50)
            screen.blit(text_surface_51, text_rect_51)
            screen.blit(text_surface_52,text_rect_52)
            screen.blit(text_surface_53,text_rect_53)
            screen.blit(text_surface_54,text_rect_54)
            screen.blit(text_surface_54,(830,750))
            # aici trb sa fie modificata matricea date_leaderboard deja
            #
            text_56 = date_leaderboard[0][0]
            text_surface_56 = font_meniu.render(text_56, True, gold)
            text_rect_56 = text_surface_56.get_rect()
            text_rect_56.center = (375, 280)

            text_57= date_leaderboard[1][0]
            text_surface_57 = font_meniu.render(text_57, True, silver)
            text_rect_57 = text_surface_57.get_rect()
            text_rect_57.center = (375, 380)

            text_58 = date_leaderboard[2][0]
            text_surface_58 = font_meniu.render(text_58, True, bronze)
            text_rect_58 = text_surface_58.get_rect()
            text_rect_58.center = (375, 480)

            text_59 = date_leaderboard[2][0]
            text_surface_59 = font_meniu.render(text_59, True, white)
            text_rect_59 = text_surface_59.get_rect()
            text_rect_59.center = (375, 580)

            text_60 = date_leaderboard[4][0]
            text_surface_60 = font_meniu.render(text_60, True, white)
            text_rect_60 = text_surface_60.get_rect()
            text_rect_60.center = (370, 680)
            screen.blit(text_surface_56,text_rect_56)
            screen.blit(text_surface_57,text_rect_57)
            screen.blit(text_surface_58,text_rect_58)
            screen.blit(text_surface_59,text_rect_59)
            screen.blit(text_surface_60,text_rect_60)

            text_61 = date_leaderboard[0][1]
            text_surface_61 = fontnormal2.render(text_61, True, gold)
            text_rect_61 = text_surface_61.get_rect()
            text_rect_61.center = (680, 280)

            text_62 = date_leaderboard[1][1]
            text_surface_62 = fontnormal2.render(text_62, True, silver)
            text_rect_62 = text_surface_62.get_rect()
            text_rect_62.center = (680, 380)

            text_63 = date_leaderboard[2][1]
            text_surface_63 = fontnormal2.render(text_63, True, bronze)
            text_rect_63 = text_surface_63.get_rect()
            text_rect_63.center = (680, 480)

            text_64 = date_leaderboard[3][1]
            text_surface_64 = fontnormal2.render(text_64, True, white)
            text_rect_64 = text_surface_64.get_rect()
            text_rect_64.center = (680, 580)

            text_65 = date_leaderboard[4][1]
            text_surface_65 = fontnormal2.render(text_65, True, white)
            text_rect_65 = text_surface_65.get_rect()
            text_rect_65.center = (680, 680)

            screen.blit(text_surface_61, text_rect_61)
            screen.blit(text_surface_62, text_rect_62)
            screen.blit(text_surface_63, text_rect_63)
            screen.blit(text_surface_64, text_rect_64)
            screen.blit(text_surface_65, text_rect_65)

            text_66 = date_leaderboard[0][2]
            text_surface_66 = fontnormal2.render(text_66, True, gold)
            text_rect_66 = text_surface_66.get_rect()
            text_rect_66.center = (860, 280)

            text_67 = date_leaderboard[1][2]
            text_surface_67 = fontnormal2.render(text_67, True, silver)
            text_rect_67 = text_surface_67.get_rect()
            text_rect_67.center = (860, 380)

            text_68 = date_leaderboard[2][2]
            text_surface_68 = fontnormal2.render(text_68, True, bronze)
            text_rect_68 = text_surface_68.get_rect()
            text_rect_68.center = (860, 480)

            text_69 = date_leaderboard[3][2]
            text_surface_69 = fontnormal2.render(text_69, True, white)
            text_rect_69 = text_surface_69.get_rect()
            text_rect_69.center = (860, 580)

            text_70 = date_leaderboard[4][2]
            text_surface_70 = fontnormal2.render(text_70, True, white)
            text_rect_70 = text_surface_70.get_rect()
            text_rect_70.center = (860, 680)

            screen.blit(text_surface_66, text_rect_66)
            screen.blit(text_surface_67, text_rect_67)
            screen.blit(text_surface_68, text_rect_68)
            screen.blit(text_surface_69, text_rect_69)
            screen.blit(text_surface_70, text_rect_70)
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
                screen.blit(gof,(930,930))
                screen.blit(text_surface_41,text_rect_41)
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
                screen.blit(gof, (930, 930))
                screen.blit(text_surface_40, text_rect_40)
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