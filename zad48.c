#include <stdio.h>
#include <stdlib.h>

int main() {
    int n,r;
    scanf("%d",&n);
    scanf("%d",&r);
    int F[n][n];
    int W[n][n];
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&F[i][j]);
            W[i][j]=0;
        }
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            for(int k=i-r;k<=i+r;k++){
                for (int l=j-r;l<=j+r;l++){
                    if (k>=0 && k<n && l>=0 && l<n){
                        W[i][j]+=F[k][l];
                    }
                }
            }
        }
    }
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d ",W[i][j]);
        }
        printf("\n");
    }
    return 0;
}
