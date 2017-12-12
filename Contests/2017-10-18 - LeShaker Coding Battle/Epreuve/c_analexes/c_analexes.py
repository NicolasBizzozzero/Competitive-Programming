TEXTE_ANALEXES = "ANALEXES"
TEXTE_NON_ANALEXES = "NON"

LOWERCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"


def count_words(string):
    dictionary = dict()
    for word in string.split():
        try:
            dictionary[word] += 1
        except KeyError:
            dictionary[word] = 1
    return dictionary


def main():
    phrase1 = input().lower().replace(" - ", " ")
    phrase2 = input().lower().replace(" - ", " ")

    phrase1 = " ".join(c for c in phrase1 if c in LOWERCASE_CHARACTERS)
    phrase2 = " ".join(c for c in phrase2 if c in LOWERCASE_CHARACTERS)

    if count_words(phrase1) == count_words(phrase2):
        print(TEXTE_ANALEXES)
    else:
        print(TEXTE_NON_ANALEXES)


if __name__ == '__main__':
    main()
