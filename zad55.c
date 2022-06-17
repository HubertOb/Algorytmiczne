#include <stdio.h>

int is_ok(int t[],int n){
    for (int i=n-1;i>0;i--){
        if (t[i]==1 && t[i-1]==1){
            return 0;
        }
    }
    return 1;
}

void naprawa(int t[],int n){
    for (int i=n-1;i>0;i--){
        if (t[i]<=1){
            break;
        }
        t[i-1]+=(t[i]/2);
        t[i]=(t[i]%2);
    }
}

void wypisz(int t[], int n){
    for (int i=0;i<n;i++){
        printf("%d",t[i]);
    }
}

int main() {
    int n,k,z=-1;
    scanf("%d",&n);
    scanf("%d",&k);
    int t[n];
    for (int i=0;i<n;i++){
        t[i]=0;
    }
    while(t[0]<2){
        if (is_ok(t,n)==1){
            k-=1;
        }
        if (k==0){
            wypisz(t,n);
            break;
        }
        t[n-1]+=1;
        naprawa(t,n);
    }
    if (k!=0){
        printf("%d",z);
    }

    return 0;
}
