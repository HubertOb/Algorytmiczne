T = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]


def DFS1(G):
    n = len(G)

    def DFSVisit(G, u):
        nonlocal time
        visited[u] = True
        for i in range(n):
            if G[u][i] == 1 and not visited[i]:
                # parent[i] = u
                DFSVisit(G, i)
                czas[i] = time
                time += 1

    visited = [False for _ in range(n)]
    czas = [None for _ in range(n)]
    # parent = [None for _ in range(n)]
    time = 1
    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)
            czas[i] = time
    print(czas)
    return czas


def DFS2visit(G, u, visited):
    n = len(G)
    visited[u] = True
    for i in range(n):
        if G[i][u] == 1 and not visited[i]:
            # visited[i]=True
            DFS2visit(G, i, visited)
            print(i, end=' ')


def silnie_spojne_skladowe(T):
    n = len(T)
    czas = DFS1(T)
    visited = [False for _ in range(n)]
    c = None
    index = None
    check = True
    while check:
        check = False
        c = -1
        for i in range(n):
            if not visited[i]:
                check = True
            if not visited[i] and (c is None or c < czas[i]):
                index = i
                c = czas[i]
        visited[index] = True
        DFS2visit(T, index, visited)
        if check:
            print(index)


silnie_spojne_skladowe(T)
