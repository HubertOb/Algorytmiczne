#include <stdio.h>
#include <stdlib.h>


int main() {
    int n;
    scanf("%d",&n);
    int t1[n][n];
    int t2[n*n];
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            scanf("%d",&t1[i][j]);
        }
    }
    int pom[n];
    for (int i=0;i<n;i++){
        pom[i]=0;
    }
    int k=0;
    int b=0,z=0;
    for (int i=0;i<n;i++){
        int c=pom[i];
        if (c<n){
            //printf("c");
            b=t1[i][pom[i]];
            z=i;
            break;
        }
    }
    for(int i=0;i<n;i++){
        if(pom[i]<n){
            if(t1[i][pom[i]]<b){
                b=t1[i][pom[i]];
                z=i;
            }
        }
    }
    t2[0]=t1[z][0];
    pom[z]++;
    for(int p=1;p<n*n;p++){
        for (int i=0;i<n;i++){
            if (pom[i]<n){
                b=t1[i][pom[i]];
                z=i;
                break;
            }
        }
        for(int i=0;i<n;i++){
            if(pom[i]<n){
                if(t1[i][pom[i]]<b){
                    b=t1[i][pom[i]];
                    z=i;
                }
            }
        }
        if(t2[k]<t1[z][pom[z]]){
            t2[k+1]=t1[z][pom[z]];
            k++;
        }
        pom[z]++;
    }
    for (int i=0;i<=k;i++){
        printf("%d ",t2[i]);
    }
    return 0;
}
