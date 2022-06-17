
#Złożoność: taka jak DFS czyli O(V^2) - reprezentacja macierzowa, O(V+E) - reprezentacja listowa

T = [[0, 1, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]


def DFS(G):
    n = len(G)

    def DFSVisit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        for i in range(n):
            if G[u][i] == 1 and visited[i] == False:
                parent[i] = u
                DFSVisit(G, i)
                tasks.append(i)
        time += 1

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    tasks = []
    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)
            tasks.append(i)
    print(tasks)
    return visited, parent


DFS(T)
