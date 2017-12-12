CHAR_FRACTAL = "X"
CHAR_EMPTY = " "


def strcnt(*strings):
    res = ""
    for string in strings:
        res = "{0}{1}".format(res, string)
    return res


def strmult(string, times):
    res = ""
    for _ in range(times):
        res = "{0}{1}".format(res, string)
    return res

def str_insert(string, to_insert, index):
    return strcnt(string[:index], to_insert, string[index:])


def _build_top_fractal(fractal, largeur, char_empty):
    return strcnt(fractal, strmult(char_empty, largeur), fractal, "\n")


def _build_center_fractal(fractal, largeur, char_empty):
    return strcnt(strmult(char_empty, largeur), fractal,
                  strmult(char_empty, largeur), "\n")


def fractal(size, char_fractal=CHAR_FRACTAL, char_empty=CHAR_EMPTY):
    if size == 0:
        return char_fractal
    else:
        taille = 3 ** size
        fractale = [[" " for _ in range(taille)] for _ in range(taille)]
        delta = taille // 3
        rec = fractal(size - 1, char_fractal, char_empty)

        coordonnees = [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)]
        for coordonnee in coordonnees:
            for y in range(delta):
                truc = coordonnee[1] * delta + y
                string_to_paste = rec[y][:delta + 1]

                for x, c in enumerate(string_to_paste, coordonnee[0] * delta):
                    fractale[truc][x] = c
        return "\n".join("".join(ligne) for ligne in fractale)



        
        # for (int[] coord : coords)
        #     for (int y = 0; y < delta; y++) {
        #         rec[y].getChars(0, delta, c[coord[1]*delta + y], coord[0]*delta);
        #     }
        
        # String[] ret = new String[taille];
        # for (int i = 0; i < taille; i++) {
        #     ret[i] = new String(c[i]);
        # }
        # return ret;


def main():
    n = 2#int(input())
    print(fractal(n))


if __name__ == '__main__':
    main()
