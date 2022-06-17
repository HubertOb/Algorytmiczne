from queue import Queue


def BFS(G, s):
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if G[u][i] > 0 and visited[i] is False:
                visited[i] = True
                parent[i] = u
                Q.put(i)
    return visited, parent


def Edmonds_Karp(G, s, t):
    maxflow = 0
    v, p = BFS(G, s)
    while v[t]:
        curr_flow = float("inf")
        z = t
        while z != s:
            curr_flow = min(curr_flow, G[p[z]][z])
            z = p[z]
        maxflow += curr_flow
        z=t
        while z!=s:
            G[p[z]][z]-=curr_flow
            G[z][p[z]]+=curr_flow
            z=p[z]
        v, p = BFS(G, s)
    return maxflow
