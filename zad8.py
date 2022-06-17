# Hubert Obarzanek
# Tworze MST i wybieram te, które mają najmniejsza różnice miedzy pierwsza i ostatnią autostradą
# Zlożoność: O(V^2+E^2*logV)

import queue
from math import ceil, sqrt



def Kruskal(G, n):
    pq = queue.PriorityQueue()
    for e in G:
        pq.put((e[0], (e[1], e[2])))
    Z = [i for i in range(n)]
    edges = []
    while not pq.empty():
        w, e = pq.get()
        x, y = e
        if Z[x] != Z[y]:
            edges.append((w, e))
            tmpx, tmpy = Z[x], Z[y]
            for i in range(n):
                if Z[i] == tmpx:
                    Z[i] = tmpy
    return edges


def foo(T):
    n = len(T)
    tab = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            tab.append(((T[i][0] - T[j][0]) ** 2 + (T[i][1] - T[j][1]) ** 2, i, j))
    return sorted(tab)


def highway(A):
    n = len(A)
    k = (n * n - n) // 2
    t = foo(A)
    print(t)
    minimum = float("inf")
    for i in range(k - n + 1):
        z = Kruskal(t[i:], n)
        b = [0] * n
        for i in range(len(z)):
            w1 = z[i][1][0]
            w2 = z[i][1][1]
            b[w1] = 1
            b[w2] = 1
        if min(b) == 1 and ceil(sqrt(z[-1][0])) - ceil(sqrt(z[0][0])) < minimum:
            minimum = ceil(sqrt(z[-1][0])) - ceil(sqrt(z[0][0]))
    return minimum

