Marius:

Runde.py:
	Aici am implementat toate  functionalitatile specifice unei runde cat si identificarea matricei de ex:
Daca functia mea primeste ca parametru mouse_x si mouse_y si in matricea mea sunt indexate pe numere tip naturale
matrice[0][0] unde 0 0 reprezinta pozitia de coordonate cu offsetul corespunzatr, eu trebuie sa convertesc aceste numere la pozitia lor 
din matricea de joc.
Dupa ce idientific impartind la cellsize si scazand offsetul in functie de matrice(player sau bot) pot sa verific in matricea mea daca in locul ala
se afla sau nu barca.De asemenea, aici verific daca pozitia apasata este deja apasata pe tabla de joc, luand cazurile specifice si 
variabilele definite in importuri.py pentru a identifica daca am facut o mutare valida sau nu
 
Importuri.py:
	Functia in care mi.am declarat toate variabiile folosite pentru a identifica turele jucatorilor, matricea barcilor adversarului cat si
a botului.Dimensiunea barcilor, daca jugam guest, bot etc 

Functii.py / aka main
	Apelarea implementarilor din fiecare fisier.py apelarea functiilor pentru a ajunge la produsul final.
	--BOGDAN LEADERBOARD ETC INAINTE:--		
	Creearea gameplay.ului fiind inceput cu player.ul care isi alege pozitiile initiale ale barcilor, cazurilie speciale fiind tratate
	De asemenea, dupa apasarea butonului de start, barcile isi dau "lock" cu ajutorul var globlae in importuri.py si incepe jocul propriu-zis
Bot.py:
	Toate functiile specifice botului ca de ex: Randomizarea pe matrice a mutarii, luand cu random pe matrice un numar
si daca a fost deja mutarea asta, muta altceva randomizand iar, also pentru optimizarea botului daca nimereste o barca, se va duce in directia in 
care mai vede tot 1 pe matrice (adica continuarea barcii) pana ajunge la 2 sau 0 (lovit deja sau e gol)
	Aici am implementat si randomizarea barcilor pe matrice:
Se alege random o barca ded orice dimensiune si se baga intr.un vector,(daca a fost aleasa, se randomizeaza iar pana se ia o barca care nu a fost pusa pana acum
pe matrice) dupa ce s.a alez barca se elge randomm orientarea barcii (verticala orizontala) dupa, aleg o pozitie random de pe matrice, iterez pe viitoare "barca"care 
ar urma sa vina, daca e totul liber, o pun si o marchez folosita pentru urmatoarele randomizari altfel, reintru in while.ul infinit care se opreste doar cand am 4 randomizari
corecte, 4 returnuri de true adica 4 barci pe matrice cu pozitii validie 

Full_database.py:
	Toate functiile legate de baza de date, de la conectare pana la clasament, verificare login, create account si restul functiilor
necesare. Implementare xp in baza de date si hashuirea parolei.