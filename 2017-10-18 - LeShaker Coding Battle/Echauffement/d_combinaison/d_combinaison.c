#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0


/**
 * Count the number of digits contained inside n.
 */
int count_digits(long long n) {
    return (int) log10(n) + 1;
}


/**
 * Split the integer n into a and b at the index index.
 */
void split_digits(long long n, int index, long long* a, long long* b) {
    *a = (long long) n / pow(10, index);
    *b = n - ((*a) * pow(10, index));
}


/**
 * Construct the concatenation of a and b
 */
long long digits_concat(long long a, long long b) {
    long long pow = 10;
    while (b >= pow)
        pow *= 10;
    return a * pow + b;
}


int main(int arc, char** argv) {
    long long n, a, b, res;
    long long l;

    scanf("%lld %lld", &n, &l);

    int nb_digits = count_digits(n);

    char printed = FALSE;
    long long i;
    for (i=(long long) pow(10, l - 1); i < pow(10, l); i++) {
        int j;
        for (j=1; j <= nb_digits; j++) {
            split_digits(i, j, &a, &b);

            res = ((long long) pow(a, 2)) + ((long long) (2 * b));
            if ((res == n) && (count_digits(a) + count_digits(b) == l)) {
                printf("%lld\n", digits_concat(a, b));
                printed = TRUE;
            }
        }
    }

    if (printed == FALSE)
        printf("Zut !");
}
