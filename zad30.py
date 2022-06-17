# Hubert Obarzanek
# na początku funkcja foo() przekształca liste krawędzi E na liste sąsiedztwa tab, gdzie znajdują sie
# krotki (w,t), gdzie w to wierzchołek z którym sąsiaduje, a t to czas dolecenia między tymi wierzchołkami.Następnie
# dorzucam do tab sąsiedztwa z czasem 0 z tablicy S(każdy element z S łącze z każdym z S krawędzią o czasie 0).
# Następnie algorytmem Dijkstry szukam najkrótszej ścieżki z a do b.
# k - ilość elementów S
# funkcja foo ma złożoność O(E+k^2) a dijkstry ma złożoność O(ElogV), zatem cała złożoność wynosi O(E+k^2+ElogV)


from queue import PriorityQueue


def foo(E, n, S):
    tab = [[] for _ in range(n)]
    for u, v, t in E:
        tab[u].append((v, t))
        tab[v].append((u, t))
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            tab[S[i]].append((S[j], 0))
            tab[S[j]].append((S[i], 0))
    return tab


def Dijkstry(tab, n, a, b, S):
    przetworzony = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    dist = [None for _ in range(n)]
    dist[a] = 0
    pq = PriorityQueue()
    pq.put((dist[a], a))
    while not pq.empty():
        _, u = pq.get()
        if przetworzony[u]:
            continue
        przetworzony[u] = True
        for w, t in tab[u]:
            if dist[w] is None or dist[w] > dist[u] + t:
                dist[w] = dist[u] + t
                parent[w] = u
                pq.put((dist[w], w))
    return dist[b]


def spacetravel(n, E, S, a, b):
    tab = foo(E, n, S)
    return Dijkstry(tab, n, a, b, S)

