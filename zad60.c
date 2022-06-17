#include <stdio.h>
#include <string.h>

void funkc(char napis[50],int start){
    char najw=napis[start];
    //printf("%c",najw);
    int naji=start;
    for (int i=start+1;i<50;i++){
        if(napis[i]==0){
            break;
        }
        if(napis[i]>najw){
            najw=napis[i];
            naji=i;
        }

    }
    printf("%c",najw);
    if(napis[naji+1]!=0){
    funkc(napis,naji+1);}
}

int main() {
    char napis[50];
    scanf("%s",&napis);
    //printf("%s",napis);
    funkc(napis,0);
    return 0;
}
