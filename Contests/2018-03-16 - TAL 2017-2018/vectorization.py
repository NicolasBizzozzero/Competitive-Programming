from typing import List

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def vectorize_count(corpus: List[List[str]], labels: List[str] = None):
    """ Met un corpus sous une forme vectorisée. """
    corpus = map(lambda d: " ".join(d), corpus)
    vectorizer = CountVectorizer()
    if labels == []:
        return vectorizer.transform(corpus)
    else:
        return vectorizer.fit_transform(corpus, labels)


def vectorize_tf(corpus: List[List[str]], labels: List[str] = None):
    """ Met un corpus sous une forme vectorisée. """
    corpus = map(lambda d: " ".join(d), corpus)
    vectorizer = TfidfVectorizer(use_idf=False)
    if not labels:
        return vectorizer.transform(corpus)
    else:
        return vectorizer.fit_transform(corpus, labels)


def vectorize_tfidf(corpus: List[List[str]], labels: List[str] = None):
    """ Met un corpus sous une forme vectorisée. """
    corpus = map(lambda d: " ".join(d), corpus)
    vectorizer = TfidfVectorizer()
    if not labels:
        return vectorizer.transform(corpus)
    else:
        return vectorizer.fit_transform(corpus, labels)


if __name__ == '__main__':
    pass
