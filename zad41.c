#include <stdio.h>
#include <stdlib.h>

int glob=0;


int potega(int podstawa,int wykladnik){
    int a=podstawa;
    wykladnik--;
    if (wykladnik==0) return 1;
    for (int i=0;i<wykladnik;i++){
        podstawa=podstawa*a;
    }
    return podstawa;
}

int zamiana_na_dec(int liczba,int podstawa){
    int a=0,i=0;
    while (liczba!=0){
        a+=(liczba%10)*potega(podstawa,i);
        i++;
        liczba/=10;
    }
    return a;
}

void wypisz(int liczba,int podstawa)
{
    char *tab="0123456789ABCDEF";
    if(liczba>0)
    {
        wypisz(liczba/podstawa,podstawa);
        printf( "%c",tab[liczba%podstawa]);
    }
}


void zamiana(int liczba,int podstawa, int ilosc_cyfr){
    int suma=0,liczba2=liczba,x=0;
    while (liczba2!=0){
        //x=potega(liczba2%podstawa,ilosc_cyfr);
        suma+=potega(liczba2%podstawa,ilosc_cyfr);
        liczba2/=podstawa;
        //printf("%d    %d    %d\n",suma,liczba2,x);
    }
    //printf("|--%d --suma-- %d--|\n",suma,liczba);
    if (suma==liczba){
        //printf("a");
        wypisz(liczba,podstawa);
        glob=1;
        printf(" ");
    }
}



int main()
{
    int b,m,liczba=0,poczatek=0,koniec=0;   //b-podstawa, m-cyfry
    scanf("%d",&m);
    scanf("%d",&b);
    poczatek=potega(10,m-1);
    koniec=poczatek*10;
    //printf("%d     ", poczatek);
    //printf("%d      ",koniec);
    for (int i=zamiana_na_dec(poczatek,b);i<zamiana_na_dec(koniec,b);i++){
        //printf("n%d ",i);
        zamiana(i,b,m);
    }
    if (glob==0) printf("NO");

    //zamiana(126,11,3);
    //zamiana(17,3,3);
    //printf("%d",potega(3,3));
    return 0;
}
