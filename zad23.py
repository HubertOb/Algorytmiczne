def DFSBridge(G):
    n = len(G)

    def DFSVisit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time
        low[u] = time
        for i in range(n):
            if G[u][i] == 1 and not visited[i]:
                parent[i] = u
                DFSVisit(G, i)
        for j in range(n):
            if j != parent[u] and G[u][j] == 1 and low[j] < low[u]:
                low[u] = low[j]

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    low = [float("inf")] * n
    d = [0] * n
    bridges = []
    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)
    for j in range(n):
        if d[j] == low[j] and parent[j] is not None:
            bridges.append((parent[j], j))
    return bridges


if __name__ == '__main__':
    T = [[0, 1, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]

    print(DFSBridge(T))
