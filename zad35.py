# w poleceniu powinno być A[i]-A[j]=x
# ustawiam 2 wskazniki i oraz j na 2 pierwsze elementy i jesli róznica jest za mała to zwiekszam j, a jesli za duza to zwiekszam i
# złożoność: O(n)

# jeśli miało by być A[i]+A[j]=x to wtedy ustawiam i na pierwszy element a drugiego elementu szukam binary_searchem, jeśli nie znajdzie takiej sumy to i ustawiam na kolejny element
# złożoność: O(nlogn)

def find_sum(A, x):
    n = len(A)
    j = 0
    i = 1
    if n == 1 and A[0] * 2 == x:
        return True
    if n == 1:
        return False
    while i != n - 1 and j != n - 1:
        if A[i] - A[j] == x:
            print(j, i)
            return True
        if A[i] - A[j] < x:
            i += 1
        else:
            j += 1
    return False


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
        return True
    return False


def find_sum_with_plus(A, x):
    n = len(A)
    for i in range(n - 1):
        j = i + 1
        if j == n - 1:
            if A[i] + A[j] == x:
                return True
            return False
        if binary_search(A[i:], x - A[i]):
            return True
    return False


if __name__ == '__main__':
    T = [-5, 0, 1, 2, 3, 4, 5, 7, 8, 9]
    x = 18
    print(find_sum_with_plus(T, x))
