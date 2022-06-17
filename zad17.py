
#Złożoność: O(V+E)

T = [[0, 1, 0, 0, 1, 0],
     [1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 1, 1],
     [0, 0, 1, 0, 0, 1],
     [1, 1, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]


def DFS(G):
    n = len(G)

    def DFSVisit(G, u):
        for i in range(n):
            if G[u][i] == 1:
                parent[i] = u
                G[u][i] = 0
                G[i][u] = 0
                DFSVisit(G, i)
                cycle.append(i)

    parent = [None for _ in range(n)]
    cycle = []
    DFSVisit(G, 0)
    cycle.append(0)  # (w grafie skierowanym trzeba zrobic cycle.reverse())
    return cycle


print(DFS(T))
