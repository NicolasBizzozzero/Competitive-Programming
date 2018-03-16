from pprint import pprint
from collections import Counter

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

from parsing import *
from preprocessing import *
from filtrage import *
from common import *
from vectorization import *
from learning import *
from postprocessing import *


RE_CM_ID = r"<\d*:\d*:([CM])>"
RE_CM_TEST_ID = r"<\d*:\d*>"


def main_chirac_mitterrand():
    # Chargement des données
    data_train, data_test = parse_chirac_mitterrand()

    # Récupération des classes des documents
    classes_train, data_train = extract_labels(data_train, regex=RE_CM_ID)
    _, data_test = extract_labels(data_test, regex=RE_CM_TEST_ID)

    # Preprocessing des documents
    data_train, data_test = preprocessing(data_train, data_test, )

    # Apprentissage
    ppln_tf_mnnaivebayes = Pipeline([
        ("vectorization", CountVectorizer()),
        ("transformation", TfidfTransformer()),
        ("classification", MultinomialNB())
    ])
    ppln_tf_mnnaivebayes.fit(data_train, classes_train)

    # Prediction
    predictions = ppln_tf_mnnaivebayes.predict(data_test)
    pprint(predictions)


def preprocessing_cm():
    # Chargement des données
    data_train, data_test = parse_chirac_mitterrand()

    # Récupération des classes des documents
    classes_train, data_train = retrieve_classes_chirac_mitterrand(data_train)
    data_test = remove_labels_test_chirac_mitterrand(data_test)

    # Preprocessing des documents
    data_train = list(map(preprocessing, data_train))
    data_test = list(map(preprocessing, data_test))

    # Vectorisation des documents
    data_train = list(map(lambda d: d.split(), data_train))
    data_test = list(map(lambda d: d.split(), data_test))

    # Filtrage des mots inutiles du documents
    data_train = list(map(filtrage, data_train))

    # Extraction de tous les mots du corpus
    all_words = np.array(extract_all_words(data_train))

    # De-vectorization
    data_train = map(lambda d: " ".join(d), data_train)
    data_test = map(lambda d: " ".join(d), data_test)

    return data_train, classes_train, data_test


if __name__ == '__main__':
    main_chirac_mitterrand()
