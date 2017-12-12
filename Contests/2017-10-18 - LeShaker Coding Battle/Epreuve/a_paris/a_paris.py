from statistics import median

TEXTE_JOCKEY_POURRI = "Jockey suivant !"
TEXTE_JOCKEY_PLUTOT_PAS_MAL = "Parie !"


def main():
    P, N = int(input()), int(input())
    positions = [int(s) for s in input().split()]

    if median(positions) >= P:
        print(TEXTE_JOCKEY_POURRI)
    else:
        print(TEXTE_JOCKEY_PLUTOT_PAS_MAL)


if __name__ == '__main__':
    main()
