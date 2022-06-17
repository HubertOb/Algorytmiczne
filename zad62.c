#include <stdio.h>

int main() {
    long long int liczba1,liczba2;
    int wynik1[100],wynik2[100],k=0;
    for (int i=0;i<100;i++){
        wynik1[i]=0;
        wynik2[i]=0;
    }
    scanf("%lld",&liczba1);
    liczba2=-liczba1;
    while (liczba1!=0){
        if (liczba1%(-2)==-1){
            liczba1=liczba1/(-2)+1;
            wynik1[k]=1;
        }
        else{
            wynik1[k]=liczba1%(-2);
            liczba1/=(-2);
        }
        k++;
    }
    k=0;
    while (liczba2!=0){
        if (liczba2%(-2)==-1){
            liczba2=liczba2/(-2)+1;
            wynik2[k]=1;
        }
        else{
            wynik2[k]=liczba2%(-2);
            liczba2/=(-2);
        }
        k++;
    }
    for (int l=0;l<100;l++){
        if (wynik1[l]==1){
            printf("%d ",l);
        }
    }
    printf("\n");
    for (int l=0;l<100;l++){
        if (wynik2[l]==1){
            printf("%d ",l);
        }
    }
    return 0;
}
