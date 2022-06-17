from queue import Queue

# V - ilosc wierzchołków, E - ilość krawędzi
# złozoność: O(V^2) - reprezentacja macierzowa, O(V+E) - reprezentacja listowa


G = [[0, 1, 0, 1, 1, 1],
     [1, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 1, 0],
     [1, 1, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0],
     [1, 1, 0, 0, 0, 0]]


def BFS(G, s):
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    dist = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    dist[s] = 0
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if G[u][i] == 1 and visited[i] is False:
                visited[i] = True
                dist[i] = dist[u] + 1
                parent[i] = u
                Q.put(i)
    return visited, dist, parent


print(BFS(G, 0))
