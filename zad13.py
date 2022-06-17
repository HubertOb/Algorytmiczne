def FloydWarshall(G):
    n = len(G)
    D = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
    for i in range(n):
        for j in range(n):
            if G[i][j]!=0:
                D[i][j]=G[i][j]
    for k in range(1, n + 1):
        for u in range(n):
            for v in range(n):
                D[u][v] = min(D[u][v], D[u][k-1] + D[k-1][v])
    return D


if __name__=='__main__':
    G = [[0, 1, 0, 0, 0, 0, 0, 0, 2],
         [1, 0, 2, 0, 0, 0, 0, 3, 0],
         [0, 2, 0, 5, 0, 0, 0, 0, 0],
         [0, 0, 5, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 4, 8, 0, 0],
         [0, 0, 0, 0, 4, 0, 1, 0, 7],
         [0, 0, 0, 0, 8, 1, 0, 3, 0],
         [0, 3, 0, 0, 0, 0, 3, 0, 1],
         [2, 0, 0, 0, 0, 7, 0, 1, 0]]
    print(FloydWarshall(G))
