import os.path
import re
from typing import List, Tuple

from nltk.corpus.reader import CategorizedPlaintextCorpusReader


# Informations de la base Chirac-Mitterrand
DIR_DATA_CM = "data/Chirac-Mitterrand"
PATH_DATA_TRAIN_CM = os.path.join(DIR_DATA_CM, "corpus.tache1.learn.utf8")
PATH_DATA_TEST_CM = os.path.join(DIR_DATA_CM, "corpus.tache1.test.utf8")

# Informations de la base Movie-Reviews
DIR_DATA_MR = "data/Movie-Reviews"
DIR_DATA_TRAIN_MR = os.path.join(DIR_DATA_MR, "train")
PATH_DATA_TEST_MR = os.path.join(DIR_DATA_MR, "test.txt")


def parse_chirac_mitterrand(path_data_train: str = PATH_DATA_TRAIN_CM,
                            path_data_test: str = PATH_DATA_TEST_CM,
                            encoding: str = "utf8"):
    """ Lit les données Chirac-Mitterrand et les retourne au format brut. """
    with open(path_data_train, encoding=encoding) as file:
        data_train = file.read()
    with open(path_data_test, encoding=encoding) as file:
        data_test = file.read()

    data_train = data_train.split("\n")[:-1]
    data_test = data_test.split("\n")[:-1]

    return data_train, data_test


def parse_movie_reviews(dir_data_train: str = DIR_DATA_TRAIN_MR,
                        path_data_test: str = PATH_DATA_TEST_MR,
                        encoding: str = "utf8"):
    """ Lit les données Movie-Reviews et les retourne au format brut. """
    # Chargement des données
    data_train = CategorizedPlaintextCorpusReader(dir_data_train,
                                                  r'.*\.txt',
                                                  cat_pattern=r'(\w+)/*',
                                                  encoding=encoding)
    with open(path_data_test, encoding=encoding) as file:
        data_test = file.read()

    # Mise en forme des données d'apprentissage
    data_train = data_train.paras()
    data_cleaned = []
    for idoc, document in enumerate(data_train):
        data_cleaned.append([])
        for sentence in document:
            sentence_clean = " ".join(sentence)
            data_cleaned[idoc].append(sentence_clean)
    data_train = list(map(lambda d: " ".join(d), data_cleaned))

    # Mise en forme des données de test
    data_test = data_test.split("\n")

    return data_train, data_test


def extract_labels(corpus: List[str], regex: str,
                   labels_on_the_left: bool = True) -> Tuple[List[str],
                                                             List[str]]:
    """ Iterate through a corpus and extract the labels matching a regex.
    Return all the labels matched and the cleaned documents.
    """
    labels, documents = list(), list()
    if labels_on_the_left:
        for document in corpus:
            result = re.split(regex, document, maxsplit=1)
            try:
                label, document = filter(None, result)  # Remove empty-strings
            except ValueError:
                label, document = None, result[-1]
            labels.append(label)
            documents.append(document)
    else:
        for document in corpus:
            result = re.split(regex, document, maxsplit=1)
            try:
                document, label = filter(None, result)  # Remove empty-strings
            except ValueError:
                document, label = None, result[-1]
            labels.append(label)
            documents.append(document)
    return labels, documents


if __name__ == '__main__':
    pass
