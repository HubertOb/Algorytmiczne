#include <stdio.h>

int main() {
    char l1[20],l2[20];
    int liczba1=0,liczba2=0,p1=0,p2=0,liczba3=0;
    int liczba;
    scanf("%s",&l1);
    scanf("%s",&l2);
    //printf("%s",l1[8]);
    for (int i=19;i>=0;i--) {
        if (l1[i] == 0) {
            liczba1 += 0;
        } else if (l1[i] == 73) {
            if (p1 <= 1) {
                liczba1 += 1;
                p1 = 1;
            } else {
                liczba1 -= 1;
                p1 = 1;
            }
        } else if (l1[i] == 86) {
            if (p1 <= 5) {
                liczba1 += 5;
                p1 = 5;
            } else {
                liczba1 -= 5;
                p1 = 5;
            }
        } else if (l1[i] == 88) {
            if (p1 <= 10) {
                liczba1 += 10;
                p1 = 10;
            } else {
                liczba1 -= 10;
                p1 = 10;
            }
        } else if (l1[i] == 76) {
            if (p1 <= 50) {
                liczba1 += 50;
                p1 = 50;
            } else {
                liczba1 -= 50;
                p1 = 50;
            }
        } else if (l1[i] == 67) {
            if (p1 <= 100) {
                liczba1 += 100;
                p1 = 100;
            } else {
                liczba1 -= 100;
                p1 = 100;
            }
        } else if (l1[i] == 68) {
            if (p1 <= 500) {
                liczba1 += 500;
                p1 = 500;
            } else {
                liczba1 -= 500;
                p1 = 500;
            }
        } else if (l1[i] == 77) {
            if (p1 <= 1000) {
                liczba1 += 1000;
                p1 = 1000;
            } else {
                liczba1 -= 1000;
                p1 = 1000;
            }
        }
    }
    for (int i=19;i>=0;i--) {
        if (l2[i] == 0) {
            liczba2 += 0;
        } else if (l2[i] == 73) {
            if (p2 <= 1) {
                liczba2 += 1;
                p2 = 1;
            } else {
                liczba2 -= 1;
                p2 = 1;
            }
        } else if (l2[i] == 86) {
            if (p2 <= 5) {
                liczba2 += 5;
                p2 = 5;
            } else {
                liczba2 -= 5;
                p2 = 5;
            }
        } else if (l2[i] == 88) {
            if (p2 <= 10) {
                liczba2 += 10;
                p2 = 10;
            } else {
                liczba2 -= 10;
                p2 = 10;
            }
        } else if (l2[i] == 76) {
            if (p2 <= 50) {
                liczba2 += 50;
                p2 = 50;
            } else {
                liczba2 -= 50;
                p2 = 50;
            }
        } else if (l2[i] == 67) {
            if (p2 <= 100) {
                liczba2 += 100;
                p2 = 100;
            } else {
                liczba2 -= 100;
                p2 = 100;
            }
        } else if (l2[i] == 68) {
            if (p2 <= 500) {
                liczba2 += 500;
                p2 = 500;
            } else {
                liczba2 -= 500;
                p2 = 500;
            }
        } else if (l2[i] == 77) {
            if (p2 <= 1000) {
                liczba2 += 1000;
                p2 = 1000;
            } else {
                liczba2 -= 1000;
                p2 = 1000;
            }
        }
    }
    //printf("%d\n",liczba1);
    //printf("%d\n",liczba2);
    liczba3=liczba1+liczba2;
    while(liczba3!=0){
        if(liczba3>=1000){
            printf("M");
            liczba3-=1000;
        }
        else if(liczba3>=900){
            printf("CM");
            liczba3-=900;
        }
        else if(liczba3>=500){
            printf("D");
            liczba3-=500;
        }
        else if(liczba3>=400){
            printf("CD");
            liczba3-=400;
        }
        else if(liczba3>=100){
            printf("C");
            liczba3-=100;
        }
        else if(liczba3>=90){
            printf("XC");
            liczba3-=90;
        }
        else if(liczba3>=50){
            printf("L");
            liczba3-=50;
        }
        else if(liczba3>=40){
            printf("XL");
            liczba3-=40;
        }
        else if(liczba3>=10){
            printf("X");
            liczba3-=10;
        }
        else if(liczba3>=9){
            printf("IX");
            liczba3-=9;
        }
        else if(liczba3>=5){
            printf("V");
            liczba3-=5;
        }
        else if(liczba3>=4){
            printf("IV");
            liczba3-=4;
        }
        else if(liczba3>=1){
            printf("I");
            liczba3-=1;
        }
    }

    return 0;
}
