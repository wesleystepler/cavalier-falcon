#include <stdio.h>
#include <stdlib.h>
#include "defs.h"
#include <immintrin.h>

/* 
 * Please fill in the following team struct 
 */
who_t who = {
    "I still have the high ground",           /* Scoreboard name */

    "Wesley Stepler",      /* First member full name */
    "pws3ms@virginia.edu",     /* First member email address */
};

/*** UTILITY FUNCTIONS ***/

/* You are free to use these utility functions, or write your own versions
 * of them. */

/* A struct used to compute averaged pixel value */
typedef struct {
    unsigned short red;
    unsigned short green;
    unsigned short blue;
    unsigned short alpha;
    unsigned short num;
} pixel_sum;

/* Compute min and max of two integers, respectively */
static int min(int a, int b) { return (a < b ? a : b); }
static int max(int a, int b) { return (a > b ? a : b); }

/* 
 * initialize_pixel_sum - Initializes all fields of sum to 0 
 */
static void initialize_pixel_sum(pixel_sum *sum) 
{
    sum->red = sum->green = sum->blue = sum->alpha = 0;
    sum->num = 0;
    return;
}

/* 
 * accumulate_sum - Accumulates field values of p in corresponding 
 * fields of sum 
 */
static void accumulate_sum(pixel_sum *sum, pixel p) 
{
    sum->red += (int) p.red;
    sum->green += (int) p.green;
    sum->blue += (int) p.blue;
    sum->alpha += (int) p.alpha;
    sum->num++;
    return;
}

/* 
 * assign_sum_to_pixel - Computes averaged pixel value in current_pixel 
 */
static void assign_sum_to_pixel(pixel *current_pixel, pixel_sum sum) 
{
    current_pixel->red = (unsigned short) (sum.red/sum.num);
    current_pixel->green = (unsigned short) (sum.green/sum.num);
    current_pixel->blue = (unsigned short) (sum.blue/sum.num);
    current_pixel->alpha = (unsigned short) (sum.alpha/sum.num);
    return;
}

/* 
 * avg - Returns averaged pixel value at (i,j) 
 */
static pixel avg(int dim, int i, int j, pixel *src) 
{
    pixel_sum sum;
    pixel current_pixel;

    initialize_pixel_sum(&sum);
    for(int jj=max(j-1, 0); jj <= min(j+1, dim-1); jj++) 
	for(int ii=max(i-1, 0); ii <= min(i+1, dim-1); ii++) 
	    accumulate_sum(&sum, src[RIDX(ii,jj,dim)]);

    assign_sum_to_pixel(&current_pixel, sum);
 
    return current_pixel;
}



/******************************************************
 * Your different versions of the smooth go here
 ******************************************************/

char better_smooth_descr[] = "better_smooth: A better implementation";
void better_smooth(int dim, pixel *src, pixel *dst)
{
    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
            if (i != 0 && j != 0 && i != dim-1 && j != dim-1) {
                pixel_sum sum;
                pixel current_pixel;

                initialize_pixel_sum(&sum);
                //accumulate_sum(&sum, src[RIDX(i,j,dim)]);
                sum.red += (int) src[RIDX(i,j,dim)].red;
                sum.green += (int) src[RIDX(i,j,dim)].green;
                sum.blue += (int) src[RIDX(i,j,dim)].blue;
                sum.alpha += (int) src[RIDX(i,j,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i,j+1,dim)]);
                sum.red += (int) src[RIDX(i,j+1,dim)].red;
                sum.green += (int) src[RIDX(i,j+1,dim)].green;
                sum.blue += (int) src[RIDX(i,j+1,dim)].blue;
                sum.alpha += (int) src[RIDX(i,j+1,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i,j-1,dim)]);
                sum.red += (int) src[RIDX(i,j-1,dim)].red;
                sum.green += (int) src[RIDX(i,j-1,dim)].green;
                sum.blue += (int) src[RIDX(i,j-1,dim)].blue;
                sum.alpha += (int) src[RIDX(i,j-1,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i+1,j,dim)]);
                sum.red += (int) src[RIDX(i+1,j,dim)].red;
                sum.green += (int) src[RIDX(i+1,j,dim)].green;
                sum.blue += (int) src[RIDX(i+1,j,dim)].blue;
                sum.alpha += (int) src[RIDX(i+1,j,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i-1,j,dim)]);
                sum.red += (int) src[RIDX(i-1,j,dim)].red;
                sum.green += (int) src[RIDX(i-1,j,dim)].green;
                sum.blue += (int) src[RIDX(i-1,j,dim)].blue;
                sum.alpha += (int) src[RIDX(i-1,j,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i+1,j-1,dim)]);
                sum.red += (int) src[RIDX(i+1,j-1,dim)].red;
                sum.green += (int) src[RIDX(i+1,j-1,dim)].green;
                sum.blue += (int) src[RIDX(i+1,j-1,dim)].blue;
                sum.alpha += (int) src[RIDX(i+1,j-1,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i-1,j+1,dim)]);
                sum.red += (int) src[RIDX(i-1,j+1,dim)].red;
                sum.green += (int) src[RIDX(i-1,j+1,dim)].green;
                sum.blue += (int) src[RIDX(i-1,j+1,dim)].blue;
                sum.alpha += (int) src[RIDX(i-1,j+1,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i+1,j+1,dim)]);
                sum.red += (int) src[RIDX(i+1,j+1,dim)].red;
                sum.green += (int) src[RIDX(i+1,j+1,dim)].green;
                sum.blue += (int) src[RIDX(i+1,j+1,dim)].blue;
                sum.alpha += (int) src[RIDX(i+1,j+1,dim)].alpha;
                sum.num++;
                //accumulate_sum(&sum, src[RIDX(i-1,j-1,dim)]);
                sum.red += (int) src[RIDX(i-1,j-1,dim)].red;
                sum.green += (int) src[RIDX(i-1,j-1,dim)].green;
                sum.blue += (int) src[RIDX(i-1,j-1,dim)].blue;
                sum.alpha += (int) src[RIDX(i-1,j-1,dim)].alpha;
                sum.num++;

               
                current_pixel.red = (unsigned short) (sum.red/9);
                current_pixel.green = (unsigned short) (sum.green/9);
                current_pixel.blue = (unsigned short) (sum.blue/9);
                current_pixel.alpha = (unsigned short) (sum.alpha/9);
                dst[RIDX(i, j, dim)] = current_pixel;
            }
            else {
                dst[RIDX(i,j, dim)] = avg(dim, i, j, src);
            }
        }
    }
}

/* 
 * naive_smooth - The naive baseline version of smooth
    fewafjewa;fjewal;fjewa748923743892
 */
char naive_smooth_descr[] = "naive_smooth: Naive baseline implementation";
void naive_smooth(int dim, pixel *src, pixel *dst) 
{
    for (int i = 0; i < dim; i++)
	for (int j = 0; j < dim; j++)
            dst[RIDX(i,j, dim)] = avg(dim, i, j, src);
}
/* 
 * smooth - Your current working version of smooth
 *          Our supplied version simply calls naive_smooth
 */
char another_smooth_descr[] = "another_smooth: Another version of smooth";
void another_smooth(int dim, pixel *src, pixel *dst) 
{
    naive_smooth(dim, src, dst);
}

/*********************************************************************
 * register_smooth_functions - Register all of your different versions
 *     of the smooth function by calling the add_smooth_function() for
 *     each test function. When you run the benchmark program, it will
 *     test and report the performance of each registered test
 *     function.  
 *********************************************************************/

void register_smooth_functions() {
    add_smooth_function(&naive_smooth, naive_smooth_descr);
    add_smooth_function(&another_smooth, another_smooth_descr);
    add_smooth_function(&better_smooth, better_smooth_descr);
}