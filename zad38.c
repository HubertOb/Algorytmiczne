#include <stdio.h>

int czy_pierwsza(int liczba)
{
    if (liczba==2 || liczba==3) return 1;
    if (liczba%2==0 || liczba%3==0) return 0;
    for(int i=3;i*i<=liczba;i+=2)
    {
        if (liczba%i==0) return 0;
    }
    return 1;
}

int czy_rosnaca(int liczba)
{
    int a=0,b=0;
    if (liczba<10) return 1;
    while(liczba!=0){
        if (a<b) {return 0;}
        a=liczba%10;
        liczba=liczba/10;
        b=liczba%10;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d",&n);
    for (int i=2;i<n;i++)
    {
        if (czy_pierwsza(i)==1){
            if (czy_rosnaca(i)==1) printf("%d\n", i);
        }
    }
    return 0;
}
