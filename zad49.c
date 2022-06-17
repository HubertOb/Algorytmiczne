#include <stdio.h>

int czy(int n, int tab[][n],int a, int b, int c, int d){
    for (int i=a;i<b;i++){
        for (int j=c;j<d;j++){
            if (tab[i][j]==1){
                return 0;
            }
        }
    }
    return 1;
}

//void f(int n, int tab[][n],int a, int b, int c, int d){
//    if (a==b || c==d){
//        return;
//    }
//    if(czy(n,tab,a,b,c,d)==1){
//        if ((b-a)*(d-c)>pole){
//            pole=(b-a)*(d-c);
//        }
//    }
//    else{
//        f(n,tab,a+1,b,c,d);
//        f(n,tab,a,b-1,c,d);
//        f(n,tab,a,b,c+1,d);
//        f(n,tab,a,b,c,d-1);
//    }
//}

int main() {
    int n,pole=0;
    scanf("%d",&n);
    int t[n][n];
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            scanf("%d",&t[i][j]);
        }
    }
    for (int i=0;i<n;i++){
        for (int j=n;j>i;j--){
            for (int k=0;k<n;k++){
                for (int l=n;l>k;l--){
                    if (czy(n,t,i,j,k,l)==1){
                        if ((j-i)*(l-k)>pole){
                            pole=(j-i)*(l-k);
                        }
                        break;
                    }
                }
            }
        }
    }
    //f(n,t,0,n,0,n);
    printf("%d",pole);

    return 0;
}
