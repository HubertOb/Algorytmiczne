from queue import PriorityQueue


def Prima(G):
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    weight = [float("inf") for _ in range(n)]
    pq = PriorityQueue()
    pq.put((0, 0))
    while not pq.empty():
        a = pq.get()[1]
        if visited[a]:
            continue
        visited[a] = True
        for i in range(n):
            if G[a][i] != 0 and G[a][i] < weight[i] and not visited[i]:
                parent[i] = a
                weight[i] = G[a][i]
                pq.put((G[a][i], i))
    return parent


if __name__ == '__main__':
    G = [[0, 1, 2, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 3, 0, 0, 0, 0],
         [2, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 1, 3, 0, 1, 2, 0, 0, 0],
         [0, 3, 0, 1, 0, 4, 0, 0, 0],
         [0, 0, 0, 2, 4, 0, 1, 5, 0],
         [0, 0, 0, 0, 0, 1, 0, 2, 100],
         [0, 0, 0, 0, 0, 5, 2, 0, 0],
         [0, 0, 0, 0, 0, 0, 100, 0, 0]]

    T = [[0, 1, 0, 0, 0, 3],
         [1, 0, 2, 0, 4, 0],
         [0, 2, 0, 1, 0, 1],
         [0, 0, 1, 0, 3, 0],
         [0, 4, 0, 3, 0, 2],
         [3, 0, 1, 0, 2, 0]]

    print(Prima(G))
    print(Prima(T))
