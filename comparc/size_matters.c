#include <stdio.h>

int main() {
    long ptr;
    int x = sizeof(ptr);
    printf("%d\n", x);

    long y = -5;
    printf("%ld", y);
    return 0;
}