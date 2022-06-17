def binary_search(A, x):
    n = len(A)
    i = 0
    j = n - 1
    m = (i + j) // 2
    if A[0] == x:
        return 0
    while i < j and i != m:
        if x <= A[m]:
            j = m
        else:
            i = m
        m = (i + j) // 2
    if A[j] == x:
        return j
    return None


if __name__ == '__main__':
    T = [2, 3, 4, 5, 5]
    x = 5
    print(binary_search(T, x))
