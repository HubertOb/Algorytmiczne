#include <stdio.h>
#include <stdlib.h>

int main() {
    int n,z=1;
    scanf("%d",&n);
    int t[n][n];
    for(int k=0;k<=(n/2);k++)
    {
        for(int i=k; i<(n-k); i++){
            t[k][i]=z;
            z++;
        }
        for(int j=(k+1);j<(n-k);j++){
            t[j][n-k-1]=z;
            z++;
        }
        for(int i=(n-k-2); i>=k; i--){
            t[n-k-1][i]=z;
            z++;
        }
        for(int j=(n-k-2);j>=(k+1);j--){
            t[j][k]=z;
            z++;
        }
    }
    for (int a=0;a<n;a++){
        for (int b=0;b<n;b++){
            printf("%d ",t[a][b]);
        }
        printf("\n");
    }

    return 0;
}
