#include <stdio.h>

int f(int n, int t[][n], int k, int a, int b){
    int licznik=0,i=1,suma=0;
    while(a-i>=0 && a+i<n && b-i>=0 && b+i<n){
        for (int j=b-i;j<=b+i;j++){
            suma+=t[a-i][j];
            suma+=t[a+i][j];
        }
        for (int j=a-i+1;j<=a+i-1;j++){
            suma+=t[j][b-i];
            suma+=t[j][b+i];
        }
        if (suma==k){
            licznik++;
        }
        i++;
    }
    return licznik;
}

int main() {
    int n,k,licznik=0,z,wsk=0;
    scanf("%d",&n);
    scanf("%d",&k);
    int t[n][n],s[n][2];
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            scanf("%d",&t[i][j]);
        }
    }
    for (int i=1;i<n-1;i++){
        for (int j=1;j<n-1;j++){
            z=f(n,t,k,i,j);
            licznik+=z;
            if (z!=0){
                s[wsk][0]=i;
                s[wsk][1]=j;
                wsk++;
            }
        }
    }
    printf("%d\n",licznik);
    for (int i=0;i<wsk;i++){
        printf("%d %d\n",s[i][0],s[i][1]);
    }
    return 0;
}
