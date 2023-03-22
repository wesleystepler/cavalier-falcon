#include <stdio.h>

long mystery(long x);
long test(long x);

int main() {
    //Question 3
    /*int *p = (int *)0x200000;
    printf("%p\n", p);
    int array[1024];
    p = array;
    printf("%p\n", p);
    p = p + 10;
    printf("%p\n", p);
    p[4] = 300;
    printf("%p\n", p);

    printf("%p\n", p);*/
    //lng x = ;
    int done = 0;
    /*while (done != 1) {
        printf("x = %ld\n", x);
        //printf("%lu\n", mystery(x));
        printf("%ld\n", mystery(x));
        if (mystery(x) == -9) {
            done = 1;
            printf("%ld\n", x);
        }
        x++;
       
    }*/
    long z = 3377699720527872;
    //long z = 100000056;
    printf("%ld\n", mystery(z));
}

long mystery(long x) {
    long t = -x;
    return (t >> 48) + (x >> 50);
}

long test(long x) {
    return x >> 40;
}