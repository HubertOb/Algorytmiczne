def BellmanFord(G, s=0):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    parent = [None] * n
    distance[s] = 0
    for i in range(n - 1):
        for j in range(n):
            for k in range(n):
                if G[j][k] != 0 and distance[k] > distance[j] + G[j][k]:
                    distance[k] = distance[j] + G[j][k]
                    parent[k] = j
    for j in range(n):
        for k in range(n):
            if G[j][k] != 0 and distance[k] > distance[j] + G[j][k]:
                return None
    return parent, distance


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
    print(BellmanFord(G,0))