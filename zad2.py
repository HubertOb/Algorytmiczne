def partition(A, p, r):
    x = A[r][1] - A[r][0]
    i = p - 1
    for j in range(p, r):
        if A[j][1] - A[j][0] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def depth(L):
    n = len(L)
    quick_sort(L, 0, n - 1)
    tab = [0] * n
    maximum = 0
    for i in range(n - 1):
        if tab[i] != 0:
            continue
        for j in range(i + 1, n, 1):
            # if L[j][0]>L[i][1]:
            #     break
            if L[i][0] <= L[j][0] and L[i][1] >= L[j][1]:
                tab[i] += 1
                tab[j] = 1
                if tab[i] > maximum:
                    maximum = tab[i]
    return maximum


