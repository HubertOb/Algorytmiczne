#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int powerm(int a){
    return a*a;
}


int main(){
    int t,n,osie=0,a,b;
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        scanf("%d",&n);
        int tab[t][2*n][2];
        for (int j=0;j<2*n;j=j+2){
            scanf("%d",&a);
            scanf("%d",&b);
            tab[i][j][0]=a*100;
            tab[i][j][1]=b*100;
        }
        for(int j=1;j<2*n;j+=2){
            tab[i][j][0]=(tab[i][(j+1)%(2*n)][0]+tab[i][(j-1)%(2*n)][0])/2;
            tab[i][j][1]=(tab[i][(j+1)%(2*n)][1]+tab[i][(j-1)%(2*n)][1])/2;
        }
        osie=0;
        for(int j=0;j<n;j++){
            for(int k=1;k<n;k++){
                if ((powerm(tab[i][(2*n+j-k)%(2*n)][0]-tab[i][j][0])+powerm(tab[i][(2*n+j-k)%(2*n)][1]-tab[i][j][1]))!=(powerm(tab[i][(2*n+j+k)%(2*n)][0]-tab[i][j][0])+powerm(tab[i][(2*n+j+k)%(2*n)][1]-tab[i][j][1]))){
                    osie-=1;
                    break;
                }
            }
            osie+=1;
        }
        printf("%d\n",osie);

    }
    return 0;
}

