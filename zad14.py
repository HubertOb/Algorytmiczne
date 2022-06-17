def Kruskal(G):
    G.sort()
    n = 0
    for w, a, b in G:
        n = max(n, a, b)
    n += 1
    set_1 = [i for i in range(n)]
    edges = []
    for w, a, b in G:
        if set_1[a] != set_1[b]:
            edges.append((a, b))
            for j in range(n):
                if j == b:
                    continue
                if set_1[j] == set_1[b]:
                    set_1[j] = set_1[a]
            set_1[b] = set_1[a]
    return edges


if __name__ == '__main__':
    G = [(1, 0, 1), (2, 0, 2), (1, 1, 3), (3, 1, 4), (3, 2, 3), (1, 3, 4), (2, 3, 5), (4, 4, 5), (1, 5, 6), (5, 5, 7),
         (2, 6, 7), (100, 6, 8)]
    print(Kruskal(G))
