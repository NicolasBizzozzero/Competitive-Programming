from typing import List, Tuple


def extract_all_words(corpus: List[str]) -> Tuple[str]:
    """ Retourne tous les mots présents dans une liste de listes de
    strings
    """
    all_words = set()
    for document in corpus:
        for word in document:
            all_words.add(word)
    return sorted(tuple(all_words))


if __name__ == '__main__':
    pass
