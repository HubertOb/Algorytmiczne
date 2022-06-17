# Hubert Obarzanek
# najpierw sortuję listę budynków po współrzędnych b, gdy sa równe to po współrzędnych a. Następnie
# dla każdego budynku po kolei obliczam maksymalną liczbę studentów które można uzyskać budując budynki po kolei do
# danego budynku włącznie. złożoność: O(nlogn +np)


def partition(A, p, r, tab):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][2] == x[2]:
            if A[j][1] <= x[1]:
                i += 1
                A[i], A[j] = A[j], A[i]
                tab[i], tab[j] = tab[j], tab[i]
        elif A[j][2] < x[2]:
            i += 1
            A[i], A[j] = A[j], A[i]
            tab[i], tab[j] = tab[j], tab[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quick_sort(A, p, r, tab):
    if p < r:
        q = partition(A, p, r, tab)
        quick_sort(A, p, q - 1, tab)
        quick_sort(A, q + 1, r, tab)


def k(T, DP, i, j):  # funkcja pomocnicza, która oblicza wartość największej liczby studentów
    a = T[i][0] * (T[i][2] - T[i][1])
    koszt = j - T[i][3]
    b = i
    maxim = 0
    b -= 1
    while b >= 0:
        if T[i][1] > T[b][2] and DP[b][koszt] > maxim:
            maxim = DP[b][koszt]
        b -= 1
    return a + maxim


def v(a):  # zwraca pojemność budynku
    return a[0] * (a[2] - a[1])


def getSol(DP, T, n, p, tab):  # zwraca liste budynków które należy wybudować
    maxval = 0
    maxind = 0
    wynik = []
    for i in range(n):
        if DP[i][p] > maxval:
            maxval = DP[i][p]
            maxind = i
    a = T[maxind][1]
    flag = False
    while maxind >= 0:
        if DP[maxind][p] != maxval:
            maxind -= 1
            continue
        elif T[maxind][2] >= a and flag:
            maxind -= 1
            continue
        flag = True
        wynik.append(maxind)
        maxval -= v(T[maxind])
        p -= T[maxind][3]
        a = T[maxind][1]
        maxind -= 1
        if maxval == 0:
            break
    for i in range(len(wynik)):
        wynik[i] = tab[wynik[i]]
    return wynik


def select_buildings(T, p):
    n = len(T)
    tab = [0] * n
    for i in range(n):
        tab[i] = i
    quick_sort(T, 0, n - 1, tab)
    DP = [[0] * (p + 1) for _ in range(n)]
    for i in range(p + 1):
        if i >= T[0][3]:
            DP[0][i] = T[0][0] * (T[0][2] - T[0][1])
    for i in range(1, n):
        if T[i][3] > p:
            continue
        DP[i][T[i][3]] = T[i][0] * (T[i][2] - T[i][1])
        for j in range(T[i][3] + 1, p + 1):
            DP[i][j] = k(T, DP, i, j)
    return getSol(DP, T, n, p, tab)


