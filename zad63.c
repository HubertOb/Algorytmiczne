#include <stdio.h>

int main() {
    int n,p,m,tab[20000],i=19999;
    for (int l=0;l<20000;l++){
        tab[l]=0;
    }
    scanf("%d",&n);
    for (int k=0;k<n;k++){
        scanf("%d",&p);
        scanf("%d",&tab[p+10000]);
    }
    while(i>0){
        if (tab[i]==0){
            i--;
            continue;
        }
        if (tab[i]>=1 && tab[i-1]>0){
            tab[i]--;
            tab[i-1]--;
            tab[i+1]++;
            i+=2;
            continue;
        }
        else if(tab[i]>1 && tab[i-1]==0){
            tab[i]--;
            tab[i-1]++;
            tab[i-2]++;
            i+=2;
            continue;
        }
        i--;
    }
    for (int j=0;j<20000;j++){
        if(tab[j]>0){
            printf("%d ",j-10000);
        }
    }
    return 0;
}
