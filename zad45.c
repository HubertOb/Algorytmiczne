#include <stdio.h>

int funkcja(int liczba){
    int liczba2;
    while (liczba!=1 && liczba!=4){
        liczba2=liczba;
        liczba=0;
        while(liczba2!=0){
            liczba+=(liczba2%10)*(liczba2%10);
            liczba2/=10;
        }
    }
    if (liczba==1) return 1;
    return 0;
}

int is_prime(int liczba){
    if (liczba==1) return 0;
    if (liczba==2 || liczba==3) return 1;
    if (liczba%2==0) return 0;
    for (int i=3;i*i<liczba;i+=2){
        if (liczba%i==0) return 0;
    }
    return 1;
}

int main() {
    int l,u,k,licznik=0,b=0;
    scanf("%d",&l);
    scanf("%d",&u);
    scanf("%d",&k);
    for (int i=l;i<=u;i++){
        if (funkcja(i)==1 && is_prime(i)){
            licznik++;
        }
        if (licznik==k){
            printf("%d",i);
            b=1;
            break;
        }
    }
    if (b==0) printf("-1");

    return 0;
}
