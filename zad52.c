#include <stdio.h>
#include <stdlib.h>

int main() {
    int n,t[201][201],x1,y1,x2,y2,licznik=0,l=0;        //0 białe   1 czarne
    for (int i=0;i<201;i++){
        for (int j=0;j<201;j++){
            t[i][j]=0;
        }
    }
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        scanf("%d",&x1);
        scanf("%d",&y1);
        scanf("%d",&x2);
        scanf("%d",&y2);
        for(int j=x1;j<x2;j++){
            for(int k=y1;k<y2;k++){
                if(t[j+100][k+100]==0){
                    t[j+100][k+100]=1;
                    l++;
                }
                else{
                    t[j+100][k+100]=0;
                    l--;
                }
            }
        }
    }
    printf("%d",l);
    return 0;
}
