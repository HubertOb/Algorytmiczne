#include <stdio.h>
#include <stdlib.h>

int czy_mozna_zwazyc(int masa,int szalka2,int n,int tab[])
{
    if(masa==szalka2) return 1;
    if (n==0) return 0;
    return czy_mozna_zwazyc(masa,szalka2+tab[n-1],n-1,tab) || czy_mozna_zwazyc(masa,szalka2-tab[n-1],n-1,tab) || czy_mozna_zwazyc(masa,szalka2,n-1,tab);
}

int main()
{
    int n,w,suma=0;
    scanf("%d",&n);
    scanf("%d",&w);
    int*tab=(int*)malloc(n*sizeof(int));
    for (int i=0; i<n; i++)
    {
        scanf("%d",&tab[i]);
        suma+=tab[i];
    }
    if (suma<w) printf("NO");
    else
    {
        if(czy_mozna_zwazyc(w,0,n,tab)==1)
        {
            printf("YES");
        }
        else
        {
            printf("NO");
        }
    }
    free(tab);
    return 0;
}
