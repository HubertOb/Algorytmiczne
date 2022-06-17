#include <stdio.h>

int digits(unsigned long long int a){
    int licznik=0;
    while(a>0){
        licznik+=1;
        a/=10;
    }
    return licznik;
}

unsigned long long int sprawdz(unsigned long long int a){
    unsigned long long int suma=0;
    while(a>0){
        suma+=a;
        a/=10;
    }
    return suma;
}

int main() {
    unsigned long long int s,n=1,a=1,b=-1,liczba;
    long double k,n1,a1;
    scanf("%lld",&s);
    int ile_cyfr= digits(s);
    for (int i=1;i<ile_cyfr;i++){
        n*=10;
        a=(a*10)+1;
    }
    n1=n;
    a1=a;
    k=(n1/a1);
    liczba=s*k;
    for (unsigned long long int i=liczba;i<=liczba+ile_cyfr;i++){
        if(sprawdz(i)==s){
            printf("%lld",i);
            b=1;
            break;
        }
    }
    if(b==-1){
        printf("%lld",b);
    }
    return 0;
}
