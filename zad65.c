#include <stdio.h>

int czy_ok(int n,int red[],int green[],int blue[]){
    int r=0,g=0,b=0;
    for (int i=0;i<n;i++){
        if(green[i]>0) g=1;
        if(red[i]>0) r=1;
        if(blue[i]>0) b=1;
    }
    return r+g+b;
}

int steps(int i,int red[],int green[],int blue[]){
    int suma=red[i]+green[i]+blue[i];
    int najw=red[i];
    if (green[i]>najw) najw=green[i];
    if (blue[i]>najw) najw=blue[i];
    return suma-najw;
}

int main() {
    int n;
    scanf("%d",&n);
    int red[n],green[n],blue[n],liczbakrokow=0;
    for (int i=0;i<n;i++){
        scanf("%d",&red[i]);
    }
    for (int j=0;j<n;j++){
        scanf("%d",&green[j]);
    }
    for (int k=0;k<n;k++){
        scanf("%d",&blue[k]);
    }
    for (int i=0;i<n;i++){
        if (n<3 && czy_ok(n,red,green,blue)>n){
            liczbakrokow=-1;
            break;
        }
        liczbakrokow+=steps(i,red,green,blue);
    }
    printf("%d",liczbakrokow);
    return 0;
}
