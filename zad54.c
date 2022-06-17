#include <stdio.h>

int czy(int m, int t[m][2],int a, int b){
    for (int i=0;i<m;i++){
        if(t[i][0]==a && t[i][1]==b) return 1;
    }
    return 0;
}

int main() {
    int n,m,c=0;
    scanf("%d",&n);
    scanf("%d",&m);
    int t[m][2];
    for (int i=0;i<m;i++){
        scanf("%d",&t[i][0]);
        scanf("%d",&t[i][1]);
    }
    int licznik=0;
    for (int i=1;i<=n;i++){
        for(int j=i+1;j<=n;j++){
            for (int k=j+1;k<=n;k++){
                c=czy(m,t,i,j)+czy(m,t,i,k)+czy(m,t,j,k);
                if(c==0 || c==3){
                    licznik++;
                }
                c=0;
            }
        }
    }
    printf("%d",licznik);

    return 0;
}
