from math import floor


def bubblesort(T):
    n = len(T)
    for i in range(n, 0, -1):
        for j in range(i - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]


def BucketSort(T, a, b):  # a,b to przedział z którego należą liczby
    n = len(T)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        buckets[floor(((T[i] - a) / (b - a)) * n)].append(T[i])
    for i in range(n):
        bubblesort(buckets[i])
    j = 0
    for i in range(n):
        for k in range(len(buckets[i])):
            T[j] = buckets[i][k]
            j += 1


def SortTab(T, P):
    n = len(T)
    tab = [[] for _ in range(n)]
    for i in range(n):
        tab[floor(T[i])].append(T[i])
    for i in range(n):
        BucketSort(tab[i], i, i + 1)
    k = 0
    for i in range(n):
        for j in range(len(tab[i])):
            T[k] = tab[i][j]
            k += 1
    # T.sort()
    return T


