# r : nb ligne
# c : nb col
# h : nb jambon minimal
# s : nb max case part

r = 0
c = 0
h = 0
s = 0
matcolision = []
matpiece = []


def construct_matcolision(r, c, pizza) :
    matpiece = []
    for i in range(r) :
        rowpiece = []
        for j in range(c):
            rowpiece.append(False)
        matpiece.append(rowpiece)

def check(h, s, piece) :
    cpth = 0
    nr = len(piece)
    if nr == 0 :
        return False
    nc = len(piece[0])
    #print("check nc * nr :", nc * nr, "s :", s)
    if nc * nr > s :
        return False
    #print("Lol")
    for i in range(nr) :
        for j in range(nc):
            cpth += 1 if piece[i][j] == 'H' else 0

    return cpth >= h

# verif part plus grand
def best_share(r, c, h, s, pizza):
    royal_pieces = [] # 1 * s

    for i in range(r):
        piece = []
        j = 0
        while j < (c - s + 1):
            npiece = 1
            
            print(pizza[i])
            piece = [pizza[i][j:j + s]]
            print(" " * j + piece[0])
            if check(h, s, piece) :
                npiece = s
                royal_pieces.append(((i, j), (i, j + npiece)))
            j += npiece
    return royal_pieces

def read_in(filename) :
    with open(filename, 'r') as lines:
        lc = lines.readline().strip()
        lc = lc.split(' ')
        r1, c1, h1, s1 = map(int, lc)
        for line in lines:
            line = line.strip()
            matpiece.append(line)
    return (r1, c1, h1, s1)


#3 lignes, 5 colonnes, 1 case de jambon par part au
#minimum, 6 cases par part au maximum.
def write_out(r, c, h, s, filename) :
    print(r, c, h, s)
    result = best_share(r, c, h, s, matpiece)
    with open(filename, 'w') as mfile:
        mfile.write(str(len(result)) + "\n")
        for ((x1,y1),(x2,y2)) in result:
            mfile.write(str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + "\n")


if __name__ == '__main__':
    r, c, h, s = read_in("in.txt")
    write_out(r, c, h, s -1, "out.txt")
