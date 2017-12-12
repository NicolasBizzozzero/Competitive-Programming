#include <stdio.h>

int main()
{
    int C, Ci;
    int n, m, k;
    int stones, enclosed;
    int i;
    
    scanf("%d", &C);
    for (Ci = 1; Ci <= C; Ci++) {
        scanf("%d%d%d", &n, &m, &k);
        if (n > m) {
            i = n; n = m; m = i;
        }
        if (n <= 2)
            stones = k;
        else {
            stones = 1;
            enclosed = 1;
            if (enclosed >= k)
                goto done;
            
            while ((stones + 1) / 2 + 1 <= n) {
                stones++;
                enclosed += (stones + 1) / 4 + (stones + 1) % 2;
                if (enclosed >= k)
                    goto done;
            }
            while ((stones + 1) / 2 + 1 <= m) {
                stones++;
                enclosed += (n + (stones + 1) % 2) / 2;
                if (enclosed >= k)
                    goto done;
            }
            i = 4 * n / 2;
            while (1) {
                stones++;
                enclosed += i-- / 4;
                if (enclosed >= k)
                    goto done;
            }
done:
            ;
        }
        printf("Cas #%d: %d\n", Ci, stones);
    }
    return 0;
}
