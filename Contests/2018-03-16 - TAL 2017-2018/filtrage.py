from typing import List
from pathlib import Path

from nltk.stem.snowball import FrenchStemmer


STOP_WORDS_FR = Path("stopwords/stopwords_fr.txt").read_text().split()

STEMMER_FR = FrenchStemmer()


def filtrage(document: List[str], min_size: int = 3,
             stemmatisation: bool = True, lemmatisation: bool = True,
             stop_words: bool = True, encoding: str = "utf-8") -> List[str]:
    """ Retire les mots inintéressant d'un document vectorisé. """
    # Suppression des mots de trop petite taille
    document = list(filter(lambda w: len(w) >= min_size, document))

    if stop_words:
        document = list(filter(lambda w: not stop_words_french(w), document))

    if stemmatisation:
        document = list(map(stemmatisation_french, document))

    return document


def stop_words_french(word: str) -> str:
    """ Filtre les mots selon si ce sont des stop words de la langue
    française ou non.
    """
    global STOP_WORDS_FR

    return word in STOP_WORDS_FR


def stemmatisation_french(word: str) -> str:
    """ Stemmatise un mot français. """
    global STEMMER_FR

    return STEMMER_FR.stem(word)


if __name__ == '__main__':
    pass
