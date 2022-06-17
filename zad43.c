#include <stdio.h>
#include <stdlib.h>


int najwieksza(int a[], int n){
    int index=0,max=a[0];
    for (int i=0;i<n;i++){
        if (a[i]>max){
            index=i;
            max=a[i];
        }
    }
    return index;
}



int main() {
    int n=0,k=0,suma=0,x=0;
    scanf("%d",&n);
    scanf("%d",&k);
    int*a=(int*)malloc(n*sizeof(int));
    for (int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    x=najwieksza(a,n);
    while (a[x]>0 && k>0){
        a[x]/=2;
        k--;
        x=najwieksza(a,n);
    }

    for (int i=0;i<n;i++) {
        suma += a[i];
    }

    printf("%d",suma);

    free(a);
    return 0;
}
