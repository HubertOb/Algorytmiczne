#include <stdio.h>

int main() {
    int t[15]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
    char s[50];
    scanf("%s",&s);
    int n=0;
    while(s[n]!=0){
        n++;
    }
    char napis[n];
    for (int i=0;i<n;i++){
        for(int j=0;t[j]<n;j++){
            char napis[n];

            for (int l=0;l<n;l++){
                char * strcat(char* napis,const char* s[(i+l*t[j])%n]);
            }
            printf("%s\n",napis);
        }
    }
    return 0;
}
