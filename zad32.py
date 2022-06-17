# Na początku porównuje 2 elementy z tablicy i mniejszy porównuje z minimum, a większy porównuję z maximum.

def min_max_elements(A):
    n = len(A)
    if n == 0:
        return None, None
    if n == 1:
        return A[0], A[0]
    if A[0] > A[1]:
        minimum = A[1]
        maximum = A[0]
    else:
        minimum = A[0]
        maximum = A[1]
    for i in range(2, n - 1, 2):
        if A[i] > A[i + 1]:
            if A[i + 1] < minimum:
                minimum = A[i + 1]
            if A[i] > maximum:
                maximum = A[i]
        else:
            if A[i] < minimum:
                minimum = A[i]
            if A[i + 1] > maximum:
                maximum = A[i + 1]
    if n % 2 == 1:
        if A[n - 1] > maximum:
            maximum = A[n - 1]
        elif A[n - 1] < minimum:
            minimum = A[n - 1]
    return minimum, maximum


if __name__ == '__main__':
    T = [4, 2, 1, 5, 6, 0, 7]
    print(min_max_elements(T))
