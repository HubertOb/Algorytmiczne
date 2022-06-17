# Hubert Obarzanek
# tworzę tablice długości k+1 i dodaje do niej pierwszych k+1 elementów z listy(tablica wskazników
# na elementy listy) a nastepnie wykonuje na liscie build_heap, przez co w pierwszej komórce mam najmniejsza liczbe.
# przepinam ten element i do tablicy na pierwsze miejsce dodaje kolejny element listy i wykonuje na tablicy heapify.
# powtarzam te kroki az skoncza sie elementy listy. zostanie wtedy tylko tablica którą sortuję heapsortem (nie
# wykonuję już w tym sortowaniu build heap bo tablica jest juz poprawnym kopcem)

# złożonośc pamięciowa: O(k) - tablica reprezentująca kopiec binarny
# złożonośc obliczeniowa: O(nlogk)

# złożonośc czasowa dla:
#   k=O(1) - O(n)
#   k=O(logn) - O(nlog(logn))
#   k=O(n) - O(nlogn)



def parent(i):
    return (i - 1) // 2


def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    max_ind = i
    if l < n and A[l].val < A[max_ind].val:
        max_ind = l
    if r < n and A[r].val < A[max_ind].val:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


def heapsort(A):
    n = len(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
        A[i].next = A[0]


def SortH(p, k):
    counter = 1  #
    a = p  #
    while a.next is not None:
        counter += 1  #
        a = a.next  #
    if k >= counter:  #
        k = counter - 1  #
    if k == 0:
        return p
    heap = [None for _ in range(k + 1)]
    for i in range(k + 1):
        heap[i] = p
        p = p.next
    build_heap(heap)
    first = heap[0]
    z = first
    while p is not None:
        heap[0] = p
        p = p.next
        heapify(heap, len(heap), 0)
        z.next = heap[0]
        z = z.next
    heapsort(heap)
    z.next = heap[k - 1]
    heap[0].next = None
    return first

