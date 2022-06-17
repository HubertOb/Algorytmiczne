Zad1. 
Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
def __init__(self):
self.val = None # przechowywana liczba rzeczywista
self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest 1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności. Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p. Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n listy oraz parametru k). Proszę skomentować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz k = Θ(n).

Zad2. 
Dany jest ciąg przedziałów domkniętych L = [[a1, b1], . . . , [an, bn]]. Początki i końce przedziałów są liczbami naturalnymi. Poziomem przedziału c ∈ L nazywamy liczbę przedziałów w L, które w całości zawierają się w c (nie licząc samego c). Proszę zaproponować i zaimplementować algorytm, który zwraca maksimum z poziomów przedziałów znajdujących się w L. Proszę uzasadnić poprawność algorytmu i oszacować jego złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję postaci:
def depth( L ):
...
która przyjmuje listę przedziałów L i zwraca maksimum z poziomów przedziałów w L.
Przykład. Dla listy przedziałów:
L = [ [1, 6],
[5, 6],
[2, 5],
[8, 9],
[1, 6]]
wynikiem jest liczba 3.

Zad3. 
Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego. Rozkład ten mamy zadany jako k przedziałów [a1, b1], [a2, b2], . . . , [ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci, a liczba z przedziału (x ∈ [ai, bi]) jest losowana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić. Liczby ai, bi są liczbami naturalnymi ze zbioru {1, . . . ,N}. Proszę zaimplementować funkcję SortTab(T, P) sortująca podaną tablicę i zwracająca posortowaną tablicę jako wynik. Pierwszy argument to tablica do posortowania a drugi to opis przedziałów
w postaci:
P = [(a_1,b_1,c_1), (a_2,b_2,c_2), ..., (a_k,b_k,c_k)]}.
Na przykład dla wejścia:
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P = [(1, 5, 0.75) , (4, 8, 0.25)]
po wywołaniu SortTab(T,P) tablica zwrócona w wyniku powinna mieć postaci:
T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową zaproponowanego algorytmu.

Zad4. 
Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków, z których inwestor musi wybrać podzbiór spełniając jego oczekiwania. Każdy budynek reprezentowany jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b, oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku może mieszkać h ⋅ (b − a) studentów. Proszę zaimplementować funkcję:
def select_buildings(T, p):
...
która przyjmuje:
• Tablicę T zawierająca opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie z oznaczeniami wprowadzonymi powyżej.
• Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych od 0), które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja może zwrócić dowolny z nich. Dwa budynki nie zachodzą na siebie, jeśli nie mają punktu wspólnego. Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo uzasadnić jej poprawność i oszacować złożoność obliczeniową.
Przykład. Dla argumentów:
T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5
wynikiem może być tablica: [ 0, 2 ]

Zad5.
W roku 2050 spokojny Maksymilian odbywa podróż przez pustynię z miasta A do miasta B. Droga pomiędzy miastami jest linią prostą na której w pewnych miejscach znajdują się plamy ropy. Maksymilian porusza się 24 kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy. Cysterna wyposażona jest w pompę pozwalającą zbierać ropę z plam. Aby dojechać z miasta A do miasta B Maksymilian będzie musiał zebrać ropę z niektórych plam (by nie zabrakło paliwa), co każdorazowo wymaga zatrzymania cysterny. Niestety, droga jest niebezpieczna. Maksymilian musi więc tak zaplanować trasę, by zatrzymać się jak najmniej razy. Na szczęście cysterna Maksymiliana jest ogromna - po zatrzymaniu zawsze może zebrać całą ropę z plamy (w cysternie zmieściłaby się cała ropa na trasie). Zaproponuj i zaimplementuj algorytm wskazujący, w których miejscach trasy Maksymilian powinien się zatrzymać i zebrać ropę. Algorytm powinien być możliwe jak najszybszy i zużywać jak najmniej pamięci. Uzasadnij jego poprawność i oszacuj złożoność obliczeniową. Dane wejściowe reprezentowane są jako tablica liczb naturalnych T, w której wartość T[i] to objętość ropy na polu numer i (objętość 0 oznacza brak ropy). Pola mają numery od 0 do n − 1 a odległość między kolejnymi polami to 1 kilometr. Miasto A znajduje się na polu 0 a miasto B na polu n − 1. Zakładamy, że początkowo cysterna jest pusta, ale pole 0 jest częścią plamy ropy, którą można zebrać przed wyruszeniem w drogę. Zakładamy również, że zadanie posiada rozwiązanie, t.j. da się dojechać z miasta A do miasta B. Algorytm należy zaimplementować w funkcji:
def plan(T):
...
która przyjmuje tablicę z opisem pół T[0], . . ., T[n-1] i zwraca listę pól, na których należy się zatrzymać w celu zebrania ropy. Lista powinna być posortowana w kolejności postojów. Postój na polu 0 również jest częścią rozwiązania.
Przykład. Dla wejścia:
# 0 1 2 3 4 5 6 7
T = [3,0,2,1,0,2,5,0]
wynikiem jest np. lista [0,2,5].

Zad6.
Dany jest graf nieskierowany G = (V,E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego poprawność i oszacować złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
def longer(G, s, t):
...
która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0. Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie nie było ścieżki z s do t to funkcja powinna zwrócić None.
Przykład. Dla argumentów:
G = [ [1, 2],
[0, 2],
[0, 1] ]
s = 0
t = 2
wynikiem jest np. krotka: (0, 2)

Zad7. 
Dane jest N miast, każde miasto jest otoczone murem, w którym znajdują się dwie bramy: północna i południowa. Jeżeli przyjedziemy do miasta jedną z bram musimy wyjechać z niego tą drugą. Wyjeżdżając każdą z bram można dojechać bezpośrednio do jednego lub więcej innych miast. Proszę zaproponować i zaimplementować algorytm który sprawdza czy wyruszając z jednego z miast można odwiedzić wszystkie miasta dokładnie jeden raz i powrócić do miasta, z którego się wyruszyło. Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego poprawność i oszacować złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
def droga(G):
...
która przyjmuje sieć połączeń G pomiędzy miastami i zwraca listę numerów odwiedzanych miast albo None jeśli takiej drogi nie ma. Sieć połączeń jest dana w postaci listy, która dla każdego miasta zawiera dwie listy: miast dostępnych z bramy północnej oraz miast dostępnych z bramy południowej. Miasta numerowane są od 0.
Przykład. Dla argumentów:
G = [ ([1],[2,3,4]),
([0],[2,5,6]),
([1,5,6],[0,3,4]),
([0,2,4],[5,7,8]),
([0,2,3],[6,7,9]),
([1,2,6],[3,7,8]),
([1,2,5],[4,7,9]),
([4,6,9],[3,5,8]),
([3,5,7],[9]),
([4,6,7],[8]) ]
wynikiem jest np. lista: ([ 0, 1, 5, 7, 9, 8, 3, 2, 6, 4 ])

Zad8.
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len = √(x1 − x2)2 + (y1 − y2)2. Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej. Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady. Przykład Dla tablicy A =[(10,10),(15,25),(20,20),(30,40)] wynikiem jest 7 (Autostrady pomiędzy miastami 0-1, 0-2, 1-3).

Zad9.
W pewnym państwie znajdują się miasta, połączone siecią jednokierunkowych rurociągów, każdy o określonej przepustowości. Złoża ropy zostały wyczerpane, jednak w jednym z miast odkryto niewyczerpane źródło nowego rodzaju paliwa. Postanowiono zbudować dwie fabryki w różnych miastach oczyszczające nowe paliwo. Z pewnych względów fabryki te nie mogą znajdować się w mieście, w którym odkryto nowe złoża i nowe paliwo będzie transportowane istniejącą siecią rurociągów. Należy wskazać dwa miasta w których należy zbudować fabryki aby zmaksymalizować produkcję
oczyszczonego paliwa. Proszę zaimplementować funkcję maxflow(G,s), która dla istniejącej sieci rurociągów G i miasta, w którym odkryto złoże s, zwróci maksymalną łączną przepustowość do dwóch miast w których należy zbudować fabryki. Miasta są ponumerowane kolejnymi liczbami 0, 1, 2, ... Sieć rurociągów opisuje lista trójek: (miasto w którym rozpoczyna się rurociąg, miasto w którym się kończy rurociąg, przepustowość rurociągu)
Przykład Dla sieci G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)] oraz miasta s=2 wynikiem jest 25 (miasta 4 i 5).

Zad10.
Implementacja algorytmu Bellmana-Forda

Zad11.
Implementacja algorytmu Dijkstry

Zad12.
Implementacja algorytmu Edmondsa-Karpa

Zad13. 
Implementacja algorytmu Floyda-Warshalla

Zad14. 
Implementacja algorytmu Kruskala

Zad15.
Implementacja algorytmu Prima

Zad16.
Implementacja algorytmu BFS

Zad17.
Implementacja algorytmu DFS

Zad18.
Implementacja algorytmu InsertionSort, SelectionSort, BubbleSort

Zad19.
Sortowanie topologiczne

Zad20.
Wykrywanie silnych spójnych składowych w grafie skierowanym

Zad21.
Implementacja QuickSorta

Zad22.
Znajdowanie punktów artykulacji w grafie

Zad23.
Znajdowanie mostów w grafie

Zad24.
Longest Increasing Subsequence

Zad25.
Problem plecakowy

Zad26.
Problem imprezy firmowej

Zad27.
Struktura Find-Union

Zad28.
Mówimy, że dwa napisy są sobie równoważne, jeśli albo są identyczne, albo byłyby identyczne, gdyby jeden z nich zapisac od tyłu. Na przykład napisy "kot" oraz "tok" są sobie równoważne, podobnie jak napisy "pies" i "pies". Dana jest tablica T zawierająca n napisów o łącznej długości N(każdy napis zawiera co najmniej jeden znak, więc N>=n; każdy napis składa się wyłącznie z małych liter alfabetu łacińskiego). Siłą napisu T[i] jest liczba indeksów j takich, że napisy T[i] oraz T[j] są sobie równoważne. Napis T[i] jest najsilniejszy, jeśli żaden inny napis nie ma większej siły. Proszę zaimplementować funkcję g(T), która zwraca siłę najsilniejszego napisu z tablicy T. Na przykład dla wejścia:
T=["pies","mysz","kot","kogut","tok","seip","kot"]
wywołanie g(T) powinno zwrócić 3. Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową zaproponowanego algorytmu.

zad29.
Kierowca ciężarówki przewozi towary z miasta A do miasta B. W pewnych miejscach trasy przejazdu znajdują się parkingi. Przejeżdżając obok parkingu kierowca może (ale nie musi) się na nim zatrzymać i odpocząć. Przepisy transportowe narzucają jednak pewne ograniczeniazwiązane z bezpieczeństwem:
1. Maksymalna liczba kilometrów, którą można przejechać bez zatrzymania wynosi T. Od zasady tej istnieje jeden wyjątek, opisany w punkcie 2.
2. W trakcie całego przejazdu z A do B kierowca może jeden raz przekroczyć limit T kilometrów jazdy bez zatrzymania. Może wówczas przejechać nie więcej niż 2T kilometrów bez zatrzymania.
Niestety, parkingi na trasie są płatne. Co więcej, opłaty za postój różnią się pomiędzy parkingami. Kierowca musi więc wybrać miejsca postoju w taki sposób, by przejechać trasę zgodnie z obowiązującymi przepisami i równocześnie zapłacić możliwie jak najmniej za postoje. Zaproponuj i zaimplementuj algorytm, który wylicza minimalny koszt przejechania z miasta A do miasta B zgodnie z opisanymi przepisami transportu towarów. Koszt przejazdu z A do B definiujemy jako sumę opłat za parkowanie w miejscach, w których kierowca się zatrzymał (nie liczymy ceny paliwa; nie bierzemy pod uwagę czasu postoju na parkingu). W miastach A i B opłata nie jest pobierana. Uzasadnij poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
def min_cost(O,C,T,L)
Argumentami funkcji są:
* Tablica O zawierająca pozycje parkingów na trasie z A do B. O[i] to liczba kilometrów (wzdłóż trasy przejazdu) od A do i-tego parkingu.
* Tablica C zawierająca ceny za postój na poszczególnych parkingach. C[i] to opłata za zatrzymanie na i-tym parkingu.
* Maksymalna liczba kilometrów T, którą można przejechać bez zatrzymywania (z zastrzeżeniem wyjątku opisanego powyzej).
* Długość L trasy (liczba kilometrów od A do B wzdłuż trasy przejazdu).
Wszystkie wartości przekazane w tablicach O i C oraz argumenty T i L to dodatnie liczby naturalne. Tablice nie muszą być posortowane. Funkcja min_cost powinna zwrócić jedną liczbę naturalną: minimalny koszt przejazdu z A do B. Można założyć, że parkingi są tak rozmieszczone, że da się przejechać z A do B zgodnie z obowiązującymi zasadami. Funkcja powinna być możliwie jak najszybsza.
Przykład. Dla danych:
O=[17,20,11,5,12]
C=[9,7,7,7,3]
T=7
L=25
wywołanie min_cost(O,C,T,L) powinno zwrócić wartość 10.

zad30.
Układ planetarny Algon składa się z n planet o numerach od 0 do n-1. Niestety własności fizyczne układu powodują, że nie da się łatwo przelecieć między dowolnymi dwiema planetami. Na szczęście mozolna eksploracja kosmosu doprowadziła do stworzenia listy E dopuszczalnych bezpośrednich przelotów. Każdy element listy E to trójka postaci (u,v,t), gdzie u i v to numery planet (można założyć, że u<v) a t to czas podróży między nimi (przelot z u do v trwa tyle samo co z v do u). Dodatkową nietypową własnością układu Algon jest to, że niektórw planety znajdują się w okolicy osobliwośći. Znajdując się przy takiej planecie możliwe jest zagięcie czasoprzestrzeni umożliwiające przedostanie się do dowolnej innej planety leżącej przy osobliwości w czasie zerowym. Zadanie polega na zaimplementowaniu funkji:
def spacetravel(n,E,S,a,b)
która zwraca nakrótszy czas podróży z planety a do planety b, mając do dyspozycji listę możliwych bezpośrednich przelotów E oraz listę S planet znajdujących się koło osobliwości. Jeśli trasa nie istnieje, to funkcja powinna zwrócić None.
Rozważmy następujące dane:
E=[(0,1,5),(1,2,21),(1,3,1),(2,4,7),(3,4,13),(3,5,16),(4,6,4),(5,6,1)]
S=[0,2,3]
a=1
b=5
n=7
Wywołanie spacetravel(n,E,S,a,b) powinno zwrócić liczbę 13. Odwiedzamy po kolei planety 1,3,2,4,6 i kończymy na planecie 5 (z planety 2 do 3 dostajemy się przez zagięcie czasoprzestrzeni). Gdyby a=1 a b=2 to wynikiem byłby czas przelotu 1.

Zad31.
Prosze zaimplementowac algorytm sortowania listy jednokierunkowej. W szczególnosci nalezy:
1. Zdefiniowac klase w Pythonie realizujaca liste jednokierunkowa.
2. Zaimplementowac wstawianie do posortowanej listy.
3. Zaimplementowac usuwanie maksimum z listy.
4. Zaimplementowac sortowanie przez wstawianie lub sortowanie przez wybieranie na podstawie powyzszych funkcji

Zad32.
Prosze zaimplementowac funkcje, która majac na wejsciu tablice n elementów oblicza jednoczesnie jej najwiekszy i najmniejszy element wykonujac 1.5n porównan.

zad33.
Prosze zaimplementowac funkcje odwracajaca liste jednokierunkowa.

Zad34.
Prosze zaimplementowac funkcje, która otrzymuje na wejsciu posortowana niemalejaco tablice A o rozmiarze n oraz liczbe x i sprawdza, czy x wystepuje w A. Jesli tak, to zwraca najmniejszy indeks, pod którym x wystepuje.

Zad35.
Dana jest posortowana tablica A[1...n] oraz liczba x. Prosze napisac program, który stwierdza czy istnieja indeksy i oraz j takie, ze A[i] + A[j] = x.

Zad36.
Prosze zaimplementowac:
1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.
3. Co sie stanie, jesli w powyzszym algorytmie bedziemy łaczyc poprzednio posortowana liste z kolejna, zamiast łaczenia dwóch kolejnych list?

Zad37.
Liczba doskonała jest to taka liczba naturalna, która jest suma wszystkich swych dzielników własciwych (to znaczy od niej mniejszych). Najmniejsza liczba doskonała jest 6, poniewaz jej dzielnikami własciwymi sa 1, 2, 3 i 1 + 2 + 3 = 6. Napisz program, który znajduje wszystkie liczby doskonałe w zadanym przedziale oraz ich liczbe.

Zad38.
Dana jest liczba całkowita dodatnia n. Napisz program, który znajduje wszystkie liczby pierwsze mniejsze od n, których cyfry tworza ciag niemalejacy.

Zad39.
Napisz program, który dla zadanej liczby naturalnej n odpowiada na pytanie, czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciagu Fibonacciego. Zakładamy, ze pierwsze dwa wyrazy ciagu Fibonacciego to 0 i 1.

Zad40.
Napisz program, który przyjmuje tablice liczb naturalnych i zwraca taki indeks, ze sumy wartosci elementów tablicy na lewo i na prawo od wyznaczonego miejsca sa równe. Mozna załozyc, ze rozwiazanie istnieje.

zad41.
Niech a =(suma od k=0 do m-1 z ak*b^k) bedzie m-cyfrowa liczba naturalna. Jej reprezentacja w układzie o podstawie b jest zatem am−1 . . . a0 (gdzie 0 <= ak < b dla k = 0, . . . ,m − 1). Jesli dla tej liczby zachodzi a =(suma od i=0 do m-1 z (ai)^m) to powiemy, ze a jest m-narcystyczna liczba w bazie b. Na przykład dla b = 10 liczba 153 jest liczba 3-narcystyczna, poniewaz
153 = 1^3 + 5^3 + 3^3 a dla b = 3 liczba 3-narcystyczna jest 122:
122(3) = 17(10) = 1^3 + 2^3 + 2^3  Napisz program, który znajduje wszystkie liczby m-narcystyczne o bazie b.

zad42.
Mamy dany zestaw n odwazników o masach danych liczbami naturalnymi. Napisz program, który sprawdza, czy zadany ciezar w mozna zwazyc przy pomocy wagi dwuszalkowej (czyli odwazniki moga byc po obu stronach wagi).

Zad43.
Mamy dana tablice A dodatnich liczb całkowitych o długosci N, na której mozemy wykonac co najwyzej K operacji. Operacja jest zdefiniowana nastepujaco:
1. Wybierz dowolny element tablicy A (A[i])
2. Zastap A[i] przez floor(A[i]/2)
Prosze napisac program wyznaczajacy minimalna sume elementów tablicy po wykonaniu na niej co najwyzej K operacji.

Zad44.
Mamy dana tablice A liczb całkowitych o długosci N oraz liczbe całkowita K. Element tablicy Ai ma pare, jezeli w tablicy znajduje sie inny element, Aj 6= Ai, o wartosci z przedziału [Ai − K, Ai + K] Prosze napisac program, który wylicza liczbe elementów, które maja pare.

zad45.
Majac dana dodatnia liczbe całkowita N, stwórzmy nowa liczbe dodajac kwadraty cyfr liczby N. Mozna udowodnic, ze postepujac w ten sposób wielokrotnie otrzymamy w koncu wynik 1 lub 4.
Przykład:
13 = 1^2 + 3^2 = 1 + 9 = 10 (Krok 1)
10 = 1^2 + 0^2 = 1 + 0 = 1 (Krok 2, konczymy iteracje poniewaz uzyskalismy liczbe 1)
Jezeli w opisanej powyzej procedurze uzyskamy wynik 1, to liczbe N nazywamy “jednokwadratowa”. Prosze napisac program, który znajduje K-ta liczbe w zadanym przedziale [L, U], która jest jednoczesnie jednokwadratowa i pierwsza.

zad46.
Napisz program, który dla danej liczby całkowitej, n, wylicza i drukuje wartosc jej silni, n!. Uwaga: Nalezy załozyc, ze wartosc n! nie miesci sie w zadnym z dostepnych w jezyku typów całkowitych.

zad47.
Dana jest tablica int t1[N][N]. W kazdym wierszu tablicy t1 znajduja sie uporzadkowane rosnaco (w obrebie wiersza) liczby naturalne. Prosze napisac program, który łaczy wiersze tablicy t1 i buduje liniowa tablice t2[N * N] tak, aby liczby w tablicy t2 były unikalne (nie powtarzały sie) i były uporzadkowane rosnaco. Uwaga: Poniewaz elementy w tablicy t1 moga sie powtarzac, faktyczna długosc tablicy t2 moze byc mniejsza niz N * N.

zad48.
Dana jest macierz kwadratowa F[n][n] wypełniona liczbami całkowitymi ze zbioru {0, 1}. Odległosc miedzy dwoma elementami tej macierzy definiujemy jako:
d(F[i][j], F[i'][j']) = max (|i − i'|, |j − j'|).
Prosze napisac program, który:
1. Wczyta ze standardowego wejscia liczby n, r, oraz macierz F,
2. Obliczy macierz W taka, ze W[i][j] jest suma wszystkich elementów F[i'][j'] macierzy F lezacych w odległosci co najwyzej r (r < n) od F[i][j], czyli takich, ze d(F[i][j], F[i'][j']) <=r.
3. Wypisze macierz W na standardowe wyjscie.

zad49.
Dane jest pole w kształcie kwadratu o boku n. Pole jest podzielone na n kwadratów o boku 1. Kazdy kwadrat jest albo uzytkowy, albo nieuzytkowy. Na polu wyznaczamy działke. Ma ona kształt prostokata i moze sie składac wyłacznie z kwadratów uzytkowych. Powierzchnia działki jest równa polu odpowiadajacego jej prostokata. Szukamy działki o jak najwiekszej powierzchni. Napisz program, który:
1. Wczyta ze standardowego wejscia opis pola,
2. Wyznaczy działke o najwiekszej powierzchni,
3. Wypisze na standardowe wyjscie powierzchnie wyznaczonej działki.

zad50.
Napisz program, który dla danej liczby całkowitej, n, alokuje tablice kwadratowa, T[n][n], wypełnia ja kolejnymi liczbami naturalnymi po spirali zaczynajac od lewego górnego rogu a nastepnie wypisuje ja na standardowe wyjscie.

zad51.
Dana jest tablica kwadratowa T[n][n] wypełniona liczbami naturalnymi oraz liczba naturalna k. Kwadratem zawartym w tablicy bedziemy nazywac kwadrat o bokach złozonych z nieparzystej i wiekszej od 1 liczby elementów całkowicie zawartych w tablicy. Prosze napisac program, który w poszukuje w tablicy T kwadratów w niej zawartych, których suma elementów na obwodzie wynosi k. Program powinien wypisac liczbe znalezionych kwadratów oraz współrzedne (indeks wiersza i kolumny) ich srodków. Uwaga: Dany element tablicy moze byc srodkiem kilku poszukiwanych kwadratów.

zad52.
Mamy płaszczyzne podzielona na kwadraciki 1×1. Kwadraciki maja boki równoległe do osi układu współrzednych, a ich wierzchołki maja współrzedne całkowite. Kwadraciki nie maja ze soba wspólnego wnetrza (nachodza na siebie jedynie bokami i wierzchołkami) i nie ma zadnej pustej przestrzeni miedzy nimi (tj. pokrywaja dokładnie cała płaszczyzne). Poczatkowo wszystkie kwadraciki sa koloru białego. Na płaszczyzne kładziemy serie prostokatów o wierzchołkach z całkowitymi współrzednymi i bokach równoległych do osi. Połozenie jednego takiego prostokata w praktyce oznacza negacje koloru wszystkich kwadracików w nim zawartych. Przez negacje rozumiemy zamiane koloru na czarny jesli aktualny kolor jest biały, albo na biały jesli kolor jest czarny. Dla podanej listy prostokatów program powinien wyliczyc ile kwadracików bedzie miało kolor czarny po połozeniu wszystkich tych prostokatów na płaszczyzne.

zad53.
Napisz program, który wczytuje dwie liczby w systemie rzymskim a nastepnie oblicza i drukuje ich sume (równiez w systemie rzymskim). W systemie rzymskim posługujemy sie znakami: I, V,X, L,C,D,M, gdzie: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000. Podczas zapisywania liczb w systemie rzymskim nalezy dazyc zawsze do tego, aby uzywac jak najmniejszej liczby znaków, pamietajac przy tym o zasadach:
1. Obok siebie moga stac co najwyzej trzy znaki sposród: I, X, C lub M.
2. Obok siebie nie moga stac dwa znaki: V , L, D.
3. Nie moze byc dwóch znaków oznaczajacych liczby mniejsze bezposrednio przed znakiem oznaczajacym liczbe wieksza.
4. Znakami poprzedzajacymi znak oznaczajacy wieksza liczbe moga byc tylko znaki: I, X, C.
5. I moze poprzedzac tylko V i X, X tylko L i C, a C tylko D i M (dlatego np. liczby 999 nie zapisuje sie jako IM).

zad54.
W przestrzeni rozmieszczono n punktów w taki sposób, ze zadne trzy z nich nie sa współliniowe. Nastepnie kazda pare tych punktów połaczono odcinkiem i kazdy odcinek pokolorowano na czarno albo na czerwono. Trójkatem jednobarwnym nazwiemy kazdy trójkat majacy wszystkie trzy boki tego samego koloru. Mamy dana liste wszystkich czerwonych odcinków. Chcemy znalezc liczbe wszystkich trójkatów jednobarwnych. Napisz program, który:
1. Wczyta ze standardowego wejscia: liczbe punktów, liczbe odcinków czerwonych oraz ich liste
2. Znajdzie liczbe trójkatów jednobarwnych,
3. Wypisze wynik na standardowe wyjscie.

zad55.
Rozwazamy wszystkie sekwencje o długosci N, składajace sie tylko z elementów 0 i 1, w których dwie jedynki nie moga ze soba sasiadowac (czyli 110 nie jest poprawna sekwencja o długosci 3, a 0101 jest poprawna sekwencja o długosci 4). Napisz program, który znajduje K-ta sekwencje w alfabetycznie posortowanym zbiorze sekwencji o długosci N.

zad56.
Dana jest tablica kwadratowa T o boku n zawierajaca wartosci całkowite. Szukamy w tablicy T takiego ciagu k sasiednich elementów (połozonych w wierszu, kolumnie lub na przekatnej - prawo lub lewoskosnie), których suma wartosci Tij jest najwieksza. Stosujemy zasade periodycznych warunków brzegowych: kazdy element tablicy ma dokładnie 8 najblizszych sasiadów. Na przykład sasiadami elementu T00 sa elementy T10, T11, T01, T(n−1)1, T(n−1)0, T(n−1)(n−1), T0(n−1), T1(n−1). W zwiazku z tym odcinek moze lezec czesciowo poza tablica: w tym przypadku tablica jest powielana w odpowiednim kierunku (kierunkach). Napisz program, który:
1. Wczyta rozmiar tablicy, n, długosc odcinka, k, i tablice T,
2. Wyznaczy optymalne połozenie odcinka,
3. Wypisze maksymalna sume k sasiednich elementów T.

zad57.
Dana jest tablica kwadratowa T o boku n zawierajaca wartosci całkowite oraz tablica prostokatna P o wymiarach k × l przechowujaca wartosci 0 lub 1. Tablice P mozemy “nałozyc” na tablice T tak, by przykryła ona pewien jej fragment (ale musi miescic sie całkowicie w obrebie T). Szukamy takiego połozenia tablicy P, ze suma elementów Tij przykrytych przez elementy P o wartosci 1 była najwieksza. Napisz program, który:
1. Wczyta rozmiar tablicy T, n, rozmiary tablicy P, k i l a nastepnie tablice T i P,
2. Wyznaczy optymalne połozenie P,
3. Wypisze maksymalna sume elementów T przykrytych przez elementy P równe 1.

zad58.
Wybieramy dodatnia liczbe całkowita X. Z liczby X wykreslamy ostatnia cyfre. Postepujemy tak, az usuniemy wszystkie cyfry liczby X. Nastepnie sumujemy wszystkie powstałe w ten sposób liczby, właczajac liczbe X. Na przykład, jezeli wybralismy X = 1234 to w kolejnych krokach otrzymamy odpowiednio liczby 1234, 123, 12, 1. Ich suma to 1370. Mamy dana liczbe całkowita dodatnia S. Prosze napisac program, który znajduje liczbe X taka, ze powyzej opisana procedura daje sume S. Mozna pokazac, ze dla dowolnej dodatniej liczby S istnieje co najwyzej jedna taka wartosc X. Jezeli nie ma takiego X program powinien wypisac -1.

zad59.
Niech f(x) bedzie najwiekszym nieparzystym podzielnikiem liczby całkowitej dodatniej x. Dana jest dodatnia liczba całkowita N. Napisz program znajdujacy f(1)+f(2)+. . .+ f(N).

zad60.
Dla dwóch stringów x i y, y jest substringiem x jezeli y da sie uzyskac z x przez usuniecie pewnej liczby znaków (mozliwe, ze zadnego lub wszystkich). Na przykład, “fmty” jest substringiem “informatyka”, ale “mro” nie jest. Napisz program, który wyznaczy i wypisze na standardowe wejscie leksykograficznie najwiekszy substring danego stringu s. Dla dwóch stringów x i y, x jest leksykograficznie wiekszy niz y jezeli y jest prefiksem x lub y ma mniejszy znak od x na pierwszej pozycji, na której oba stringi sie róznia.

zad61.
Dany jest string s, stanowiacy okres nieskonczonego periodycznego stringu t. Na przykład jezeli s = “abc” to t = “abcabcabc. . . ”. Niech n bedzie długoscia s. Tworzymy nowy string o długosci n w sposób nastepujacy: wybieramy przesuniecie o >= 0 i krok p < n, bedacy liczba pierwsza. Nowy string składa sie z pierwszych n znaków jakie mozemy przeczytac ze stringu t zaczynajac od indeksu o i nastepnie przesuwajac sie o p pozycji w prawo. Formalnie, nowy string bedzie sie składał z nastepujacych znaków (w tym porzadku): t[o], t[o + p], t[o + 2p], . . ., t[o + (n − 1)p]. Znajdz i wypisz na standardowe wyjscie najmniejszy leksykograficznie string, jaki mozna w ten sposób uzyskac. Dla danych dwóch róznych stringów, mniejszy leksykograficznie jest ten, który zawiera mniejszy znak na pierwszej pozycji, na której stringi sie róznia. Liczba 1 nie jest liczba pierwsza.

zad62.
W sali obsługi klientów banku kredytowego ustawiono 100 bankomatów ponumerowanych od 0 do 99. Kazdy bankomat wykonuje tylko jedna operacje: wypłaca albo przyjmuje ustalona kwote. Bankomat o numerze i wypłaca 2i złotych, jesli i jest parzyste, zas przyjmuje 2i złotych, jesli i jest nieparzyste. Gdy klient zamierza pozyczyc ustalona kwote, trzeba zbadac, czy bedzie mógł ja pobrac, korzystajac co najwyzej raz z kazdego z bankomatów i jesli tak, wyznaczyc numery bankomatów, z których nalezy skorzystac. Trzeba równiez zbadac, czy bedzie mógł ja zwrócic w podobny sposób i jesli tak, wyznaczyc numery bankomatów, z których nalezy skorzystac w celu wykonania tej operacji. Przykład:
Klient, który zamierza pozyczyc 7 złotych, pobiera najpierw 16 złotych w bankomacie nr 4 i 1 złoty w bankomacie nr 0, a nastepnie oddaje 8 złotych w bankomacie nr 3 i 2 złote w bankomacie nr 1. Zeby zwrócic pozyczona kwote 7 złotych, pobiera najpierw 1 złoty w bankomacie numer 0, a nastepnie oddaje 8 złotych w bankomacie nr 3. Napisz program, który:
• wczytuje ze standardowego wejscia wysokosc kwoty, jaka klient zamierza pozyczyc,
• sprawdza, czy klient bedzie mógł pobrac ustalona kwote korzystajac co najwyzej raz z kazdego bankomatu i jesli tak, wyznacza numery bankomatów, z których nalezy skorzystac, oraz czy bedzie mógł ja zwrócic w podobny sposób i jesli tak, wyznacza numery bankomatów, których nalezy uzyc w tym celu.

zad63.
Plansza do gry “Skok w bok” jest nieskonczona tasma pól, nieograniczona zarówno w lewo jak i w prawo. Na polach planszy stoja pionki. Ich liczba jest skonczona. Na jednym polu moze stac równoczesnie wiele pionków. Zakładamy, ze pierwsze od lewej pole, na którym jest przynajmniej jeden pionek, ma numer 0. Pola na prawo od niego sa oznaczone kolejno liczbami naturalnymi 1, 2, 3 itd., a pola w lewo liczbami ujemnymi: -1, -2, -3 itd. Ustawienie pionków na tasmie, które bedziemy takze nazywac konfiguracja, mozna opisac w ten sposób, ze dla kazdego pola, na którym jest co najmniej jeden pionek, podaje sie numer pola i liczbe pionków na tym polu. Sa dwa rodzaje ruchów, zmieniajacych konfiguracje: skok w prawo i skok w lewo. Skok w prawo polega na zabraniu po jednym pionku z wybranych dwóch sasiednich pól o numerach p oraz p + 1 i dodaniu jednego pionka na polu p + 2. Skok w lewo: zabieramy jeden pionek z pola p + 2, a dodajemy po jednym na polach p i p + 1. Mówimy, ze konfiguracja jest koncowa, jesli na dowolnych dwóch sasiednich polach znajduje sie co najwyzej jeden pionek. Dla kazdej konfiguracji istnieje dokładnie jedna konfiguracja koncowa, która mozna z niej otrzymac w wyniku skonczonej liczby skoków w prawo lub w lewo. Napisz program, który:
1. Wczytuje opis konfiguracji poczatkowej
2. Znajduje konfiguracje koncowa, do jakiej mozna doprowadzic dana konfiguracje poczatkowa

zad64.
Dane sa współrzedne kolejnych wierzchołków wielokata. Zadanie polega na wyznaczeniu liczby osi symetrii tego wielokata. Napisz program, który:
• wczyta ze standardowego wejscia opisy wielokatów,
• dla kazdego wielokata wyznaczy liczbe osi symetrii,
• wypisze wynik na standardowe wyjscie.

zad65.
Mamy n pudełek ponumerowanych 0, 1, . . . , n−1. i-te pudełko zawiera red[i] czerwonych kulek, green[i] zielonych kulek i blue[i] niebieskich kulek. Naszym zadaniem jest rozseparowanie kulek według kolorów tak, zeby w zadnym pudełku nie było kulek w wiecej niz jednym kolorze. W kazdym kroku mozna wybrac dowolna kulke i przeniesc ja do innego pudełka. Napisz program, który wyznaczy minimalna liczbe kroków jaka jest konieczna do rozdzielenia kulek. Jezeli jest to niemozliwe, program wypisuje -1.

zad66.
Mamy do dyspozycji jednorejestrowa maszyne cyfrowa, której jedyny rejestr moze przechowac dowolna liczbe całkowita nieujemna. Jezyk programowania maszyny ma cztery instrukcje: ’+’, ’-’, ’*’ i ’/’. Kazda z tych instrukcji wykonuje odpowiednia operacje uzywajac zawartosci rejestru jako obu swoich operandów. Po wykonaniu operacji wynik wpisywany jest z powrotem do rejestru (nadpisujac jego poprzednia zawartosc). Program dla naszej maszyny to napis składajacy sie z zera lub wiecej instrukcji. Majac dane dwie liczby całkowite s i t, utwórz najkrótszy program, po wykonaniu którego rejestr bedzie zawierał wartosc t, jezeli poczatkowa wartoscia rejestru było s. Jezeli istnieje wiecej niz jeden najkrótszy program, zwróc leksykograficznie najmniejszy. Jezeli z wartosci s nie da sie uzyskac t w skonczonej liczbie kroków, wypisz NO.




