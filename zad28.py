#Hubert Obarzanek

#na początku sortuję listę po długości wyrazów. nastepnie tworze pomocniczą tablice (pomTab) długości n, kazda komórka tej tablicy 
# jest przyporzadkowana do wyrazu w tablicy T. Następnie przechodze po tablicy T i porównuję pierwszy element z kolejnymi w 
# tablicy. jesli kolejny wyraz jest dłuzszy przerywam działanie. Słowo z którym juz porównywałem oznaczam w pomTab jako 1. 
# Następnie działam tylko tam gdzie są 0 w pomTab
# po przejsciu całej tablicy zwracam najwieksza wartośc z tablicy pomTab.
# Złożoność: sortowanie O(nlogn) + O(n-n^2)(w zaleznosci od danych wejsciowych, gdy wszystkie wyrazy beda tej samej długości
# i zadne nie beda identyczne to bedzie n^2)
#Złożonośc pamięciowa: O(n), pomocnicza tablica



def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(A,n,i):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and len(A[l])>len(A[max_ind]):
        max_ind=l
    if r<n and len(A[r])>len(A[max_ind]):
        max_ind=r
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,n,max_ind)


def build_heap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,n,i)


def heap_sort(A):
    n=len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)



def partition(T, l, p):
    x = len(T[p])
    i = l - 1
    for j in range(l, p):
        if len(T[j]) <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[p] = T[p], T[i + 1]
    return i + 1


def quicksort(T, l, p):
    if l < p:
        q = partition(T, l, p)
        quicksort(T, l, q - 1)
        quicksort(T,q+1,p)


def g(T):
    n = len(T)
    heap_sort(T)
    # quicksort(T,0,len(T)-1)
    pomTab = [0] * n
    for i in range(n):
        if pomTab[i] != 0:
            continue
        for j in range(i + 1, n):
            if len(T[j]) > len(T[i]):
                break
            if T[i] == T[j] or T[i] == T[j][::-1]:
                pomTab[j]=1
                pomTab[i] += 1
        pomTab[i] += 1
    return max(pomTab)

