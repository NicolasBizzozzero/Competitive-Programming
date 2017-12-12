def pstdin() :
    n = int(input())
    args = []
    for i in range(n):
        s = input()
        s = s.strip()
        args.append(s.split(' '))
    return args

def algo(args):
    for ia, a in enumerate(args):
        src = a[0]
        base_src = a[1]
        base_dst = a[2]
        ns = len(base_src)
        nd = len(base_dst)
        # Transforme en base 10
        r_b10 = 0
        for i, s in enumerate(reversed(src)):
            r_b10 += base_src.find(s) * (ns ** i)

        # Transforme en base dst
        res = ""
        rest = 1
        quot = r_b10
        while quot != 0 :
            rest = quot % nd
            quot = quot // nd
            res = base_dst[rest] + res

        print('Case #' + str(ia + 1) + ': ' + str(res))


if __name__ == '__main__':
    algo(pstdin())
