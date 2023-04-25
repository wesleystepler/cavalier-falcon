/*
While I was not able to complete this lab, I did spend over the expected 75 minutes working on it.
*/

#include <stdlib.h>
#include <limits.h>  /* for USHRT_MAX */

#include <immintrin.h>

#include "min.h"
/* reference implementation in C */
short min_C(long size, short * a) {
    short result = SHRT_MAX;
    for (int i = 0; i < size; ++i) {
        if (a[i] < result)
            result = a[i];
    }
    return result;
}

short vectorized_min_C(long size, short *a) {
    short result = SHRT_MAX;
    for (int i = 0; i < size; i += 32) {
    __m256i partial_min = _mm256_setzero_si256();
     __m256i first =  _mm256_setr_epi16(a[i], a[i+1], a[i+2], a[i+3], a[i+4], a[i+5], a[i+6], a[i+7], a[i+8], a[i+9], a[i+10], a[i+11], a[i+12], a[i+13], a[i+14], a[i+15]);
    __m256i second = _mm256_setr_epi16(a[i+16], a[i+17], a[i+18], a[i+19], a[i+20], a[i+21], a[i+22], a[i+23], a[i+24], a[i+25], a[i+26], a[i+27], a[i+28], a[i+29], a[i+30], a[i+31]);
    __m256i cur_min = _mm256_min_epi16(first, second);
    }

}


/* This is the list of functions to test */
function_info functions[] = {
    {min_C, "C (local)"},
    // add entries here!
    {NULL, NULL},
};
