
SORTIE_PREFIXE = "God save"


def get_enfants(parent, liens_parente, morts):
    return [f for p, f in liens_parente if (p == parent) and (f not in morts)]


def get_parent(fils, liens_parente):
    for p, f in liens_parente:
        if f == fils:
            return p


def get_heritier(mec_mort, liens_parente, morts):
    enfants = get_enfants(mec_mort, liens_parente, morts)
    if len(enfants) > 0:
        if enfants[0] not in morts:
            return enfants[0]
        else:
            return get_heritier(enfants[0], liens_parente, morts)
    else:
        pere = get_parent(mec_mort, liens_parente)
        return get_heritier(pere, liens_parente, morts)


def main():
    mec_mort = input()
    N = int(input())
    liens_parente = [input().split() for _ in range(N - 1)]
    D = int(input())
    morts = [input() for _ in range(D)]

    print(SORTIE_PREFIXE, get_heritier(mec_mort, liens_parente, morts))


if __name__ == '__main__':
    main()
