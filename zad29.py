# Hubert Obarzanek
# najpierw sortuję tablice O i nastepnie wyliczam tablice P i Q gdzie P[i] - minimalny koszt
# dojechania do punktu i bez uzycia wyjątku z punktu 2 a Q[i] - minimalny koszt dojechania do punktu i z użyciem
# wyjątku z punktu 2 i nastepnie od L sprawdzam obie tablice wstecz aby punkt i był w zasięgu T od L lub 2T od L odpowiednio
# dla tablic P i Q i zwracam minimum z tego
# zlożoność: O(n^2)



def partition(A, p, r, C):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            C[i], C[j] = C[j], C[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    C[i + 1], C[r] = C[r], C[i + 1]
    return i + 1


def quick_sort(A, p, r, C):
    if p < r:
        q = partition(A, p, r, C)
        quick_sort(A, p, q - 1, C)
        quick_sort(A, q + 1, r, C)


def min_cost(O, C, T, L):
    n = len(O)
    quick_sort(O, 0, len(O) - 1, C)
    P = [float("inf")] * n  # minimalny koszt dojechania do punktu i bez uzycia wyjątku z punktu 2
    Q = [float("inf")] * n  # minimalny koszt dojechania do punktu i z użyciem wyjątku z punktu 2
    P[0] = C[0]
    Q[0] = C[0]
    for i in range(1, n):
        k = i - 1
        j = i - 1
        while O[i] - T <= O[k] and k >= 0:
            if O[i] - T <= 0:
                P[i] = C[i]
            if P[k] + C[i] < P[i]:
                P[i] = P[k] + C[i]
            if Q[k] + C[i] < Q[i]:
                Q[i] = Q[k] + C[i]
            k -= 1
        while O[i] - 2 * T <= O[j] and j >= 0:
            if O[i] - 2 * T <= 0:
                Q[i] = C[i]
            elif P[j] + C[i] < Q[i]:
                Q[i] = P[j] + C[i]
            j -= 1
    a = n - 1
    b = n - 1
    while L - T <= O[a]:
        a -= 1
    while L - 2 * T <= O[b]:
        b -= 1
    a += 1
    b += 1
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    return min(min(Q[a:]), min(P[b:]), min(P[a:]))


