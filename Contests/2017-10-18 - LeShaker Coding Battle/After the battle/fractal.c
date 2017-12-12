/**
 * Shamelessly copy/pasted from :
 * https://codegolf.stackexchange.com/a/54508
 */

#include <stdio.h>

#define VICSEK_BITPATTERN 186
#define VICSEK_SCALE 3
#define VICSEK_GENERATIOn 3


int main(int argc, char** argv) {
    int bitpattern = atoi(argv[1]);
    int scale = atoi(argv[2]);
    int generation = atoi(argv[3]);

    int i;
    int width = 1;
    for (i=0; i < generation; ++i) {
        width *= scale;
    }

    char* out = malloc(width * width);

    for (i=0; i < width * width; ++i)
        out[i] = '#';


    int blocksize = width / scale;
    for (i=0; i < generation; ++i) {
        int x, y;
        for (y=0; y < width; ++y) {
            for (x=0; x < width; ++x) {
                int localX = x / blocksize;
                localX %= scale;
                int localY = y / blocksize;
                localY %= scale;
                int localPos = localY * scale + localX;
                if (!((bitpattern >> localPos) & 1))
                    out[y * width + x] = ' ';
            }
        }
        blocksize /= scale;
    }

    int x, y;
    for (y=0; y < width; ++y) {
        for (x=0; x < width; ++x)
            printf("%c ", out[y * width + x]);
        printf("\n");
    }
    return 0;
}