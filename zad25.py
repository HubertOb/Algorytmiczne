def knapsack(W,P,B):
    n=len(W)
    F=[[0 for _ in range(B+1)] for _ in range(n)]
    for b in range(W[0],B+1):
        F[0][b]=P[0]
    for l in range(B+1):
        for i in range(1,n):
            F[i][l]=F[i-1][l]
            if l-W[i]>=0:
                F[i][l]=max(F[i][l],F[i-1][l-W[i]]+P[i])
    return F[n-1][B],F

def getsolution(F,W,P,i,w):
    if i==0:
        if w>=W[0]: return [0]
        return[]
    if w>=W[i] and F[i][w]==F[i-1][w-W[i]]+P[i]:
        return getsolution(F,W,P,i-1,w-W[i])+[i]
    return getsolution(F,W,P,i-1,w)

P=[10,8,4,5,3,7]
W=[4,5,12,9,1,13]
maxW=24

wynik=knapsack(W,P,maxW)
for i in range(len(wynik[1])):
    print(wynik[1][i])
print(getsolution(wynik[1],W,P,len(P)-1,maxW))