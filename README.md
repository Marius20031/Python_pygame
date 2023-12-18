Marius:

Runde.py:
	Aici am implementat toate  functionalitatile specifice unei runde cat si identificarea matricei de ex:
Daca functia mea primeste ca parametru mouse_x si mouse_y si in matricea mea sunt indexate pe numere tip naturale
matrice[0][0] unde 0 0 reprezinta pozitia de coordonate cu offsetul corespunzatr, eu trebuie sa convertesc aceste numere la pozitia lor 
din matricea de joc.
Dupa ce idientific impartind la cellsize si scazand offsetul in functie de matrice(player sau bot) pot sa verific in matricea mea daca in locul ala
se afla sau nu barca.De asemenea, aici verific daca pozitia apasata este deja apasata pe tabla de joc, luand cazurile specifice si 
variabilele definite in importuri.py pentru a identifica daca am facut o mutare valida sau nu.
 
Importuri.py:
	Functia in care mi.am declarat toate variabiile folosite pentru a identifica turele jucatorilor, matricea barcilor adversarului cat si
a botului.Dimensiunea barcilor, daca jugam guest, bot etc.

Functii.py / aka main
	Apelarea implementarilor din fiecare fisier.py apelarea functiilor pentru a ajunge la produsul final.
	--BOGDAN LEADERBOARD ETC INAINTE:--		
	Creearea gameplay.ului fiind inceput cu player.ul care isi alege pozitiile initiale ale barcilor, cazurilie speciale fiind tratate.
	De asemenea, dupa apasarea butonului de start, barcile isi dau "lock" cu ajutorul var globlae in importuri.py si incepe jocul propriu-zis.
 
Bot.py:
	Toate functiile specifice botului ca de ex: Randomizarea pe matrice a mutarii, luand cu random pe matrice un numar
si daca a fost deja mutarea asta, muta altceva randomizand iar, also pentru optimizarea botului daca nimereste o barca, se va duce in directia in 
care mai vede tot 1 pe matrice (adica continuarea barcii) pana ajunge la 2 sau 0 (lovit deja sau e gol).
	Aici am implementat si randomizarea barcilor pe matrice:
Se alege random o barca ded orice dimensiune si se baga intr.un vector,(daca a fost aleasa, se randomizeaza iar pana se ia o barca care nu a fost pusa pana acum
pe matrice) dupa ce s.a alez barca se elge randomm orientarea barcii (verticala orizontala) dupa, aleg o pozitie random de pe matrice, iterez pe viitoare "barca"care 
ar urma sa vina, daca e totul liber, o pun si o marchez folosita pentru urmatoarele randomizari altfel, reintru in while.ul infinit care se opreste doar cand am 4 randomizari
corecte, 4 returnuri de true adica 4 barci pe matrice cu pozitii validie.

Full_database.py:
	Toate functiile legate de baza de date, de la conectare pana la clasament, verificare login, create account si restul functiilor
necesare. Implementare xp in baza de date si hashuirea parolei.


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
		
 
		
