from queue import Queue

def list_to_matrix(G):
    n = 0
    for i in G:
        n = max(n, i[0], i[1])
    n += 1
    tab = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in G:
        tab[i[0]][i[1]] = i[2]
    return n, tab


def deep_copy(T):
    n = len(T)
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            G[i][j] = T[i][j]
    return G


def BFS(G, s):
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if G[u][i] > 0 and visited[i] is False:
                visited[i] = True
                parent[i] = u
                Q.put(i)
    return visited, parent


def Edmonds_Karp(G, s, t):
    maxflow = 0
    v, p = BFS(G, s)
    while v[t]:
        curr_flow = float("inf")
        z = t
        while z != s:
            curr_flow = min(curr_flow, G[p[z]][z])
            z = p[z]
        maxflow += curr_flow
        u = t
        while u != s:
            G[p[u]][u] -= curr_flow
            G[u][p[u]] += curr_flow
            u = p[u]
        v, p = BFS(G, s)
    return maxflow


def maxflow(G, s):
    n, tab_G = list_to_matrix(G)
    max_flow = 0
    k = deep_copy(tab_G)
    for i in range(n):
        if i == s:
            continue
        k[i][n] = float("inf")
    Edmonds_Karp(k, s, n)
    max_val = -1
    max_ind = 0
    for i in range(n):
        if k[n][i] >= max_val:
            max_ind = i
            max_val = k[n][i]
    tab_G[max_ind][n] = float("inf")
    for j in range(n):
        if j == s or j == max_ind:
            continue
        tab_G[j][n] = float("inf")
        max_flow = max(max_flow, Edmonds_Karp(deep_copy(tab_G), s, n))
        tab_G[j][n] = 0
        tab_G[n][j] = 0
        tab_G[n][i] = 0

    return max_flow

