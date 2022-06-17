# Hubert Obarzanek
# algorytmem DFS przeszukuje graf w poszukiwaniu cyklu hamiltona, uwazajac aby z wierzchołka wyjsc
# inna brama niz sie weszło (służy do tego funkcja foo). Zlożoność: O(n!) bo sprawdza wszystkie mozliwe sciezki z
# punktu 0



def foo(G, v, parent):
    n = len(G[v][0])
    for i in range(n):
        if G[v][0][i] == parent:
            return 0
    return 1


def droga( G ):
    n = len(G)
    visited = [False] * n
    stos = [None] * n
    stos_wsk = 0

    def DFS(v, parent_v):
        nonlocal stos_wsk
        stos[stos_wsk] = v
        stos_wsk += 1
        if stos_wsk == n:
            return stos
        else:
            visited[v] = True
            k = (foo(G, v, parent_v) + 1) % 2
            for i in range(len(G[v][k])):
                if not visited[G[v][k][i]]:
                    z = DFS(G[v][k][i], v)
                    if z is not None:
                        return z
            visited[v] = False
        stos_wsk -= 1

    return DFS(0, 0)
