#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,x;
    scanf("%d",&n);
    int*tab=(int*)malloc(n*sizeof(int));
    for(int i=0;i<n;i++){
        scanf("%d",&x);
        tab[i]=x;
    }
    int suma_l=0,suma_r=0;
    for(int i=1;i<n;i++){
        suma_r+=tab[i];
    }
    int i=0;
    while(suma_l!=suma_r){
        i++;
        suma_l+=tab[i-1];
        suma_r-=tab[i];
    }
    printf("%d",i);
    free(tab);
    return 0;
}
