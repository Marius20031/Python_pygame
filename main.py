import pygame
from Importuri import *
from Functii import *
from full_database import *
# import tot ce am scris in importuri.py
# functia main care appeleaza restul:
if __name__ == "__main__":
    # imi scriu in local host datele
    # cum faceam in type json
    nume_guest=random_guest_name()
    print(nume_guest)
    login=0
    create=1
    username = "Mariuxs"
    password = "123"
    # daca incerc sa ma loghez
    if login==1:
        login_try(username,password)
        # trb sa verifice daca sunt corecte datele
    if create==1:
        create_try(username,password)
    #vedem quest si astea mai tarziu...
    username_conectat[0]=username
    run_game()
