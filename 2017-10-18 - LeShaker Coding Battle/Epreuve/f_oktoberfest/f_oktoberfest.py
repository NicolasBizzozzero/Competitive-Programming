from math import sqrt, floor


def trois_malto_deux_sacchaprolifératio(Va, Vb):
    return Va ** 3, Vb ** 2


def deux_malto_trois_sacchaprolifératio(Va, Vb):
    return Va ** 2, Vb ** 3


def matracination(Va, Vb):
    return int(floor(sqrt(Va))), int(floor(sqrt(Vb)))


def jepeuxencore(V, Va, Vb):
    res1 = trois_malto_deux_sacchaprolifératio(Va, Vb)
    res2 = deux_malto_trois_sacchaprolifératio(Va, Vb)
    res3 = matracination(Va, Vb)
    return (sum(res1) <= V) or (sum(res2) <= V) or (sum(res3) <= V)


def get_maxV(V, Va, Vb):
    if jepeuxencore(V, Va, Vb):
        tocompute = []
        res1 = trois_malto_deux_sacchaprolifératio(Va, Vb)
        if res1[0] + res1[1] <= V:
            tocompute.append(res1)
        res2 = deux_malto_trois_sacchaprolifératio(Va, Vb)
        if res2[0] + res2[1] <= V:
            tocompute.append(res2)
        res3 = matracination(Va, Vb)
        if res3[0] + res3[1] <= V:
            tocompute.append(res3)

        return max([get_maxV(V, *res) for res in tocompute])
    else:
        return Va + Vb


def main():
    V, Va, Vb = int(input()), int(input()), int(input())

    print(get_maxV(V, Va, Vb))


if __name__ == '__main__':
    main()
