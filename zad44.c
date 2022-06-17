#include <stdio.h>
#include <stdlib.h>

int my_compare (const void * a, const void * b)
{
    int _a = *(int*)a;
    int _b = *(int*)b;
    if(_a < _b) return -1;
    else if(_a == _b) return 0;
    else return 1;
}

int main() {
    int n=0,k=0,licznik=0;
    scanf("%d",&n);
    scanf("%d",&k);
    int*a=(int*)malloc(n*sizeof(int));
    int*b=(int*)malloc(n*sizeof(int));
    for (int i=0;i<n;i++){
        scanf("%d",&a[i]);
        b[i]=0;
    }
    qsort(a, n, sizeof(int), my_compare);
    for(int i=0;i<n-1;i++){
        for (int j=i+1;j<n;j++){
            if (a[j]>(a[i]+k)) break;
            if (a[j]>=(a[i]-k) && a[j]<=(a[i]+k) && a[j]!=a[i]){
                if (b[i]==0){
                    licznik++;
                    b[i]=1;
                }
                if (b[j]==0){
                    licznik++;
                    b[j]=1;
                }
            }
        }
    }
    //for (int i=0;i<n;i++){
    //    if(b[i]==1) licznik++;
    //}
    printf("%d",licznik);
    free(a);
    free(b);
    return 0;
}
