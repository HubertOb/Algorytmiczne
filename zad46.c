#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d",&n);
    int*tab=(int*)malloc(160*sizeof(int));
    for(int i=0;i<160;i++){
        tab[i]=0;
    }
    tab[159]=1;
    int a=0,reszta=0,k=0;
    for (int i=2;i<=n;i++){
        for (int j=159;j>=0;j--){
            tab[j]*=i;
            tab[j]+=reszta;
            reszta=tab[j]/10;
            tab[j]=tab[j]%10;
        }
    }
    while(tab[a]==0){
        a++;
    }
    for(int i=a;i<160;i++){
        printf("%d",tab[i]);
    }
    free(tab);
}
