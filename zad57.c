#include <stdio.h>

int main() {
    int n,k,l,suma=0,najsum=0;
    scanf("%d",&n);
    scanf("%d",&k);
    scanf("%d",&l);
    int t[n][n],tab[k][l];
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&t[i][j]);
        }
    }
    for (int i=0;i<k;i++){
        for (int j=0;j<l;j++){
            scanf("%d",&tab[i][j]);
        }
    }
    for (int i=0;i<n-k;i++){
        for (int j=0;j<n-l;j++){
            for (int a=0;a<k;a++){
                for (int b=0;b<l;b++){
                    if (tab[a][b]==1){
                        suma+=t[i+a][j+b];
                    }
                }
            }
            if (suma>najsum){
                najsum=suma;
            }
            suma=0;
        }
    }
    printf("%d",najsum);
    return 0;
}
