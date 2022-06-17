#include <stdio.h>
#include <time.h>

long long int kw(long long int a){
    return a*a;
}

long long int suma(long long int n){
    if (n==0){
        return 0;
    }
    if (n%2==1){
        return (kw((n+1)/2)+suma(n/2));
    }
    else{
        return (kw(n/2)+suma(n/2));
    }
}

int main() {
    unsigned long long int n,k,s=0,z;
    scanf("%lld",&n);
    s=suma(n);
    printf("%lld\n",s);
    return 0;
}
