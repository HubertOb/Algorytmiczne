def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


def binary_insertion_sort(A):
    n=len(A)
    for i in range(1,n):
        a=0
        b=i-1
        m=(a+b)//2
        while a+1<b:
            if A[i]>A[m]:
                a=m
                m = (a + b) // 2
            elif A[i]<=A[m]:
                b=m
                m = (a + b) // 2
        if A[i]<A[a]:
            tmp=A[i]
            for k in range(i-1,-1,-1):
                A[k+1]=A[k]
            A[0]=tmp
        elif A[i]<A[b]:
            tmp=A[i]
            for k in range(i-1,b-1,-1):
                A[k+1]=A[k]
            A[b]=tmp

def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        minimum = i
        for j in range(i + 1, n):
            if A[minimum] > A[j]:
                minimum = j
        A[i], A[minimum] = A[minimum], A[i]


if __name__ == '__main__':
    tab = [2, 8, 5, 3, 9, 4, 1]
    print(tab)
    bubble_sort(tab)
    print(tab)

    tab = [2, 8, 5, 3, 9, 4, 1]
    print(tab)
    insertion_sort(tab)
    print(tab)

    tab = [2, 8, 5, 3, 9, 4, 1]
    print(tab)
    selection_sort(tab)
    print(tab)

    tab = [2, 8, 5, 3, 9, 4, 1]
    print(tab)
    binary_insertion_sort(tab)
    print(tab)
