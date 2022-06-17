def articulation_point(G):
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

    visited = [False] * n
    parent = [None] * n
    time = 0
    low = [float("inf")] * n
    d = [0] * n
    vertices = []
    start = 0
    DFSVisit(G, start)
    x = 0
    for i in range(n):
        if i == start:
            continue
        if parent[i] != start and low[i] >= d[parent[i]] and visited[parent[i]]:
            visited[parent[i]] = False
            vertices.append(parent[i])
        elif parent[i] == start:
            x += 1
    if x > 1:
        vertices.append(start)
    return sorted(vertices)


if __name__ == '__main__':
    T = [[0, 1, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 0]]

    print(articulation_point(T))
