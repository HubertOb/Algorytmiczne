#include <stdio.h>

int main() {
    int n,a=0,b=1,c=0;
    scanf("%d",&n);
    while(b<=n)
    {
        if (a*b==n)
        {printf("YES");
        c=1;
        break;}
        b+=a;
        a=b-a;
    }
    if(c==0) printf("NO");
    return 0;
}
