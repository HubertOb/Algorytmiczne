# Hubert Obarzanek
# algorytm zachłanny, gdy bak ma pojemność b to dodaje b następnych punktów do kolejki
# priorytetowej, i gdy bak jest pusty wybieram z kolejki priorytetowej plamę o największej ilości ropy.Powtarzam te
# czynności dopóki nie znajde sie na ostatnim polu. złożoność: O(n)

from queue import PriorityQueue


def plan(T):
    n = len(T)
    pq = PriorityQueue()
    pq.put((0 - T[0], 0))
    i = 0
    wynik = []
    while i < n - 1:
        p = pq.get()
        wynik.append(p[1])
        k = 0
        for j in range(i + 1, i - p[0] + 1):
            if j == n:
                break
            pq.put((0 - T[j], j))
            k = j
        i = k
    return sorted(wynik)


def plan2(T):
    n = len(T)
    i = 1
    pq = PriorityQueue()
    bak = T[0] - 1
    wynik = [0]
    while i < n - 1:
        pq.put((0 - T[i], i))
        if bak == 0:
            p = pq.get()
            wynik.append(p[1])
            bak = 0 - p[0]
        i += 1
        bak -= 1
    return sorted(wynik)


