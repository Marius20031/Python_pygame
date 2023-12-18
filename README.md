CIOCHINA MARIUS + CONSTANTIN ROBERT-MIHAI + SAVU BOGDAN (322CB)

GITHUB: https://github.com/Marius20031/Python_pygame
Am folosit Pycharm cu regula de rulare build in main.(Run 'Main')
(TO SEE: Poze_Proiect)
De precizat faptul ca jocul la inceput se conecteaza la baza de date MongoDB motiv pentru care
jocul poate sa fie jucat doar pe calculatoarele conectate la baza de date.

Ca biblioteci am folosit:
-pentru gameplay-ul dezvoltat - pygame.
-pentru randomizare - random.
-pentru baza de date - pymongo.server_api.
-pentru matrice - numpy.
-pentru functia de hash - hashlib.
-pentru sleep - asyncio.

O dificultate intampinata a fost accea cand jocul incepea chiar daca barcile nu erau puse cum trebuie in matrice, am  rezolvat aceasta problema
iterand prin toata matricea si daca numarul de 1.uri(numarul de puncte din matrice care formeaza barcile) este egal cu numarul de casute pe care
le ocupa barcile, in seamna ca toate barcile sunt asezate cum trebuie, aceasta soltuie rezolvand ATAT problema barcilor care nu erau puse in matrice
CAT SI problema barcilor suprapuse in matrice.

De asemenea, am intampinat probleme si la randomizarea barcilor pe matrice, am tot cautat metode optime de generare.
Marius:

Runde.py:
	Aici am implementat toate  functionalitatile specifice unei runde cat si identificarea matricei de ex:
Daca functia mea primeste ca parametru mouse_x si mouse_y si in matricea mea sunt indexate pe numere tip naturale
matrice[0][0] unde 0 0 reprezinta pozitia de coordonate cu offsetul corespunzator, eu trebuie sa convertesc aceste numere la pozitia lor 
din matricea de joc.
Dupa ce identific impartind la cellsize si scazand offsetul in functie de matrice(player sau bot) pot sa verific in matricea mea daca in locul ala
se afla sau nu barca.De asemenea, aici verific daca pozitia apasata este deja apasata pe tabla de joc, luand cazurile specifice si 
variabilele definite in importuri.py pentru a identifica daca am facut o mutare valida sau nu.
 
Importuri.py:
	Functia in care mi.am declarat toate variabilele folosite pentru a identifica turele jucatorilor, matricea barcilor adversarului cat si
a botului.Dimensiunea barcilor, daca jucam guest, bot etc.

Functii.py / aka (shadow)main
	Apelarea implementarilor din fiecare fisier.py apelarea functiilor pentru a ajunge la produsul final.		
	Crearea gameplay.ului fiind inceput cu player.ul care isi alege pozitiile initiale ale barcilor, cazurile speciale fiind tratate.
	De asemenea, dupa apasarea butonului de start, barcile isi dau "lock" cu ajutorul var globlae in importuri.py si incepe jocul propriu-zis.
 
Bot.py:
	Toate functiile specifice botului ca de ex: Randomizarea pe matrice a mutarii, luand cu random pe matrice un numar
si daca a fost deja mutarea asta, muta altceva randomizand iar, also pentru optimizarea botului daca nimereste o barca, se va duce in directia in 
care mai vede tot 1 pe matrice (adica continuarea barcii) pana ajunge la 2 sau 0 (lovit deja sau e gol).
	Aici am implementat si randomizarea barcilor pe matrice:
Se alege random o barca de orice dimensiune si se baga intr.un vector,(daca a fost aleasa, se randomizeaza iar pana se ia o barca care nu a fost pusa pana acum
pe matrice) dupa ce s.a aleg barca se elge randomm orientarea barcii (verticala orizontala) dupa, aleg o pozitie random de pe matrice, iterez pe viitoare "barca"care 
ar urma sa vina, daca e totul liber, o pun si o marchez folosita pentru urmatoarele randomizari altfel, reintru in while.ul infinit care se opreste doar cand am 4 randomizari
corecte, 4 returnuri de true adica 4 barci pe matrice cu pozitii validie.

Full_database.py:
	Toate functiile legate de baza de date, de la conectare pana la clasament, verificare login, create account si restul functiilor
necesare. Implementare xp in baza de date si hashuirea parolei.Am folosit conectarea la MongoDB Atlas dat fiind faptul ca am mai avut interactiuni
cu acest tip de baza de date.XP.ul este implementat la modul, daca nimeresti o barca adversa ai +15 daca nu nimeresti ai +5, Lv.ul fiind dar de impartirea
la 10


Bogdan:

Importuri bgd: 	
		Am implementat timerul pentru playeri care incepe in momentul in care se da start la joc, avand 30 de secunde pentru fiecare runda in parte.
  Acesta este facut cu ajutorul mai multor dreptunghiuri de diverse marimi peste care este afisat un text cu numarul secundelor ramase atunci cand merge, actualizand la fiecare
  secunda doar suprafata din ecran peste care apare scrisul in fucntie. Timerul este conceput astfel incat sa fie intrerupt de un un input de mouse, insa fara sa fie intrerupt de simpla
  miscare a mouseului. De asemenea atunci cand merge pentru bot se opreste automat dupa un numar aleator de secunde fara sa astepte vreun input. Atunci cand se depaseste limita de 30
  de secunde este afisat un mesaj si incepe automat timerul pentru oponent, iar daca lovitura a avut succes atunci timerul va relua de unde a ramas pentru acelasi player, pana cand 
  va rata o lovitura. Pentru a face implementarea completa am avut nevoie de diferite variabile pe care a trebuit sa le integrez astfel incat sa fie modificate si in alte functii
  cum ar fi cele in care sunt verificate loviturile playerilor din runde.py.
  
Tot aici am facut si functia in care este afisat primul meniu, cel in care apar optiunile de log in, create account, etc., functie ce este apelata in run_game inainte
sa fie afisat orice altceva. Aici am incercat sa creez un meniu cat mai responsive cu optiunile principale, care apar in aproape orice alt joc. Astfel fiecare buton apasat deschide
mai departe un alt meniu unde apar diferite optiuni, avand si un buton cu care se poate reveni in meniul prinicpal. De exemplu pentru leaderboard va fi afisat un tabel cu primele 5
locuri din clasament orodnate dupa nivel. Pentru create account se va deschide un meniu unde trebuie furnizate credentialele pentru crearea unui nou cont, cu acestea apelandu-se mai
departe functiile din fisierul "full_database", iar in functie de ce intorc acestea sunt afisate diferite mesaje pe ecran. Pentru optiunea log in se intampla cam acelasi lucru. In plus
in urma unei operatii reusite de create account respectiv log in vor aparea direct butoane in aceste meniuri pentru a avansa mai departe catre log in/ inceperea jocului, fara a mai fi
nevoie sa te intorci in meniul principal. Exista si optiunea "play as guest" ce va duce direct la inceperea jocului fara a mai fi nevoie sa te autentifici inainte, insa astfel
nu iti va fi salvat progresul.

In plus am contribuit prin munca de echipa si la diferite alte aspecte cum ar fi idei pt joc, gasit poze, si alte aspecte ce tin de design.


Robert:

importuri_bgd:
	Am realizat design-ul si implementarea meniului principal de joc, fie dupa selectarea optiunii de "PLAY AS GUEST", fie dupa autentificarea cu credientiale valide.
 Am adaugat o poza de fundal cu marea pentru matricile in care se desfasoara jocul, precum si o poza pentru fundalul intregului joc. Numele utilizatorului autentificat(sau Guest 
 urmat de un numar random in cazul in care utilizatorul a ales optiunea de "PLAY AS GUEST") si al botului sunt afisate in partea de mijloc sus a ecranului, in dreptul timer-ului 
 si alaturi de pozele de profil ale acestora. Utilizatorul isi poate schimba poza de profil cu ajutorul sagetilor de sub poza, cicland prin toate pozele disponibile.De asemenea, 
 am pozitionat pe ecran in pozitii favorabile diferitele mesaje menite sa usureze utilizarea jocului chiar si de un utilizator nou, precum "Press this to start the gamne", 
 "Place the boats as you wish", etc. Tot aici am implementat si butoanele pentru startul jocului si pentru rotitul barcilor. Functia de start verifica mai intai daca toate barcile 
 se afla in pozitii valide, iar, in caz contrar, afiseaza un mesaj de eroare. Barcile player-ului sunt asezate sub matricea sa, ordonate de la cea mai mica la cea mai mare. Acestea
 au fiecare cate un cod ("A", "B", "C" si "D"), in functie de dimensiune. Fiecare barca are o poza cu o barca de razboi, reprezentativa pentru dimensiunea sa, vazuta de sus.
 Dupa ce sunt plasate pe matrice, barcile pot fi rotite la 90 de grade, apasand pe butonul de "ROTATE".

 Functii.py:
 	Am implementat mesajul de la finalul jocului(fie de winner, fie de loser) ce este determinat de rezultatul jocului. In plus, in cazul in care castiga player-ul, pe
  ecran vor fi afisate confetti. Confetti-urile au fost implementate cu ajutorul unei clase numite Confetti, care genereaza dreptunghiuri ce au dimensiuni si culori random
  peste tot pe ecran.
  De asemenea, am contribuit la partea de logistica, idei pentru joc si cautat poze la o rezolutie buna care sa contribuie la un design consistent.

 
		
