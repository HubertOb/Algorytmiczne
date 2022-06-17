#include <stdio.h>


int czy_potega(int a) {
    if (a == 0) {
        return 0;
    }
    while (a % 2 == 0) {
        a /= 2;
    }
    if (a == 1) {
        return 1;
    } else return 0;
}

int jaka_potega(int a) {
    int i = 0;
    while (a != 1) {
        a /= 2;
        i++;
    }
    return i;
}


int main() {
    int s, t, b = 0, a, liczs = 0, licz2 = 0;
    scanf("%d", &s);
    scanf("%d", &t);
    if (t == 0) {
        printf("-");
        return 0;
    } else if (czy_potega(s) == 0 && czy_potega(t) == 1) {
        s = 1;
        printf("/");
        //goto m;
    }
    while (t % s == 0 && s != 1) {
        t /= s;
        liczs++;
    }
    while (t % 2 == 0) {
        t /= 2;
        licz2++;
    }
    if ((t != 1 || czy_potega(liczs) == 0)&& czy_potega(t)!=1) {
        printf("NO");
    } else if (licz2 < liczs) {
        for (int i = 0; i < jaka_potega(liczs); i++) {
            printf("*");
        }
        for (int i = 0; i < licz2; i++) {
            printf("+");
        }
    } else if (licz2 >= liczs) {
        int licznik = licz2 / liczs;
        licz2 = licz2 - licznik * liczs;
        for (int i = 0; i < licznik; i++) {
            printf("+");
        }
        for (int i = 0; i < jaka_potega(liczs); i++) {
            printf("*");
        }
        for (int i = 0; i < licz2; i++) {
            printf("+");
        }
    }


    return 0;
}
