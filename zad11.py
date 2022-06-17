from queue import PriorityQueue


def Dijkstry(G, s=0):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    distance = [float("inf") for _ in range(n)]
    pq = PriorityQueue()
    distance[s] = 0
    pq.put((distance[s], s))
    while not pq.empty():
        d, a = pq.get()
        if visited[a]:
            continue
        visited[a] = True
        for i in range(n):
            if G[a][i] != 0 and not visited[i]:
                if distance[i] > distance[a] + G[a][i]:
                    distance[i] = distance[a] + G[a][i]
                    parent[i] = a
                    pq.put((distance[i], i))
    return distance, parent


if __name__ == '__main__':
    G = [[0, 1, 0, 0, 0, 0, 0, 0, 2],
         [1, 0, 2, 0, 0, 0, 0, 3, 0],
         [0, 2, 0, 5, 0, 0, 0, 0, 0],
         [0, 0, 5, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 4, 8, 0, 0],
         [0, 0, 0, 0, 4, 0, 1, 0, 7],
         [0, 0, 0, 0, 8, 1, 0, 3, 0],
         [0, 3, 0, 0, 0, 0, 3, 0, 1],
         [2, 0, 0, 0, 0, 7, 0, 1, 0]]

    print(Dijkstry(G, 0))
