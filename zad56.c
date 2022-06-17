#include <stdio.h>

int bezwzgl(int a,int b){
    int x=a-b;
    if (x<0){
        return -x;
    }
    return x;
}

int main() {
    int n,k,suma=0,najsum=-2147483648;
    scanf("%d",&n);
    scanf("%d",&k);
    int t[n][n];
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            scanf("%d",&t[i][j]);
        }
    }
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            for (int a=0;a<k;a++){
                suma+=t[(i+a)%n][j%n];
            }
            if (suma>najsum){
                najsum=suma;
            }
            suma=0;
            for (int a=0;a<k;a++){
                suma+=t[i%n][(j+a)%n];
            }
            if (suma>najsum){
                najsum=suma;
            }
            suma=0;
            for (int a=0;a<k;a++){
                suma+=t[(i+a)%n][(j+a)%n];
            }
            if (suma>najsum){
                najsum=suma;
            }
            suma=0;
            for (int a=0;a<k;a++){
                suma+=t[(i+a)%n][n-1-(bezwzgl(j,a)%n)];
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
