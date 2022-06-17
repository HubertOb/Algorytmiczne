from queue import Queue


def BFS(G, s, a, b):
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    dist[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if not visited[G[u][i]] and ((u != a or G[u][i] != b) and (u != b or G[u][i] != a)):
                visited[G[u][i]] = True
                dist[G[u][i]] = dist[u] + 1
                parent[G[u][i]] = u
                Q.put(G[u][i])
    return dist, parent


def longer(G, s, t):
    dist, parent = BFS(G, s, None, None)
    min_dist = dist[t]
    edges = []
    z = t
    while z != s:
        a = (parent[z], z)
        edges.append(a)
        z = parent[z]
    print(edges)
    for k in edges:
        dist, parent = BFS(G, s, k[0], k[1])
        if dist[t] > min_dist:
            return k
    return None

