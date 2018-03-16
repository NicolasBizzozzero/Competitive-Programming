import re
import string
import unicodedata
from functools import partial

from filtrage import filtrage


RE_URL = r"www[a-z0-9\.\/:%_+.#?!@&=-]+"
RE_WHITESPACES = r" +"


def preprocessing(data_train, data_test,
                  strip_punctuation=True, strip_whitespaces=True,
                  strip_digits=True, remove_accents=True,
                  remove_urls=True, to_lower=True, min_word_size=3,
                  stemmatisation=True, lemmatisation=True,
                  remove_stop_words=True, encoding="utf-8"):
    # Preprocessing des documents
    preprocessing_func = partial(preprocessing_doc,
                                 strip_punctuation=strip_punctuation,
                                 strip_whitespaces=strip_whitespaces,
                                 strip_digits=strip_digits,
                                 remove_accents=remove_accents,
                                 remove_urls=remove_urls,
                                 to_lower=to_lower,
                                 encoding=encoding)
    data_train = list(map(preprocessing_func, data_train))
    data_test = list(map(preprocessing_func, data_test))

    # Vectorisation des documents
    data_train = list(map(lambda d: d.split(), data_train))
    data_test = list(map(lambda d: d.split(), data_test))

    # Filtrage des mots inutiles du documents
    filtrage_func = partial(filtrage,
                            min_size=min_word_size,
                            stemmatisation=stemmatisation,
                            lemmatisation=lemmatisation,
                            stop_words=remove_stop_words,
                            encoding=encoding)
    data_train = list(map(filtrage_func, data_train))

    # Extraction de tous les mots du corpus
    # all_words = np.array(extract_all_words(data_train))

    # De-vectorization
    data_train = list(map(lambda d: " ".join(d), data_train))
    data_test = list(map(lambda d: " ".join(d), data_test))

    return data_train, data_test


def preprocessing_doc(document: str, strip_punctuation=True,
                      strip_whitespaces=True, strip_digits=True,
                      remove_accents=True, remove_urls=True, to_lower=True,
                      encoding="utf-8") -> str:
    """ Effectue le nettoyage du contenu d'un document. """
    to_removes = ""

    # All Regular Expressions first
    if remove_urls:
        document = re.sub(RE_URL, "", document)
    if remove_accents:
        document = unicodedata.normalize('NFD', document).encode(
            "ascii", 'ignore').decode(encoding)
    if to_lower:
        document = document.lower()
    if strip_punctuation:
        to_removes += string.punctuation
    if strip_digits:
        to_removes += string.digits
    if strip_whitespaces:
        to_removes += string.whitespace

    document = document.translate(
        str.maketrans(to_removes, ' ' * len(to_removes)))

    if strip_whitespaces:
        document = re.sub(RE_WHITESPACES, " ", document)
    return document


if __name__ == '__main__':
    pass
