#include <stdio.h>

unsigned long mystery(unsigned long x);

int main() {
    unsigned long x = 6;
    unsigned long result = mystery(x);
    printf("%lu\n", result);

}

unsigned long mystery(unsigned long x) {
    long temp = (long) x;
    temp = temp ^ (temp >> 1);
    return (unsigned long) temp;
}