#include <stdio.h>

int czy_doskonala(int liczba)
{
    int suma=1;
    if (liczba==1)
    {
        return 0;
    }
    for (int i=2; i*i<=liczba; i++)
    {
        if(i*i==liczba)
        {
            suma+=i;
        }
        else if(liczba%i==0)
        {
            suma+=i;
            suma+=liczba/i;
        }
    }
    if(suma==liczba)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int m,n,licznik=0,tab[10];
    scanf("%i",&m);
    scanf("%i",&n);
    for (int i=m; i<=n; i++)
    {
        if(czy_doskonala(i)==1)
        {
            tab[licznik]=i;
            licznik++;
        }
    }
    printf("%i\n",licznik);
    for(int i=0; i<licznik; i++)
    {
        printf("%i ",tab[i]);
    }
    return 0;
}
