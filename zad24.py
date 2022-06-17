def lis(A):
    n = len(A)
    maxi = 0
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    return maxi, F, P


def printSol(A, P, i):
    if P[i] != -1:
        printSol(A, P, P[i])
    print(A[i])


if __name__ == '__main__':
    T = [2, 1, 4, 3, 4, 8, 5, 7, 2, 0]
    a = lis(T)
    print(a)
    printSol(T, a[2], a[0])
