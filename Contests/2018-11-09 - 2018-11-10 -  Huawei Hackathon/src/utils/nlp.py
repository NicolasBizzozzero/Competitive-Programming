from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
import re
from gensim.models import Word2Vec
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


# Pour le stemming
stemmer = LancasterStemmer()
# Pour les stopwords
english_stopwords = stopwords.words('english')
# Pour la ponctuation
translator = str.maketrans('', '', string.punctuation)


def clear_text(text, stemming=False, punctuation=True):
    """
    Clear text by removing special chars / lower case / delete stopwords / stemming
    Return tokenized text

    Parameters
    ------------
        text : string
        stemming : Apply stemming or not
        punctuation : Delete punctutation or not
    """

    pre_process = remove_special_chars(text)
    pre_process = pre_process.lower()

    new_words = []
    for word in pre_process.split(' '):
        if word not in english_stopwords:
            if stemming:
                new_words.append(stemmer.stem(word))
            else:
                new_words.append(word)

    return new_words


def remove_special_chars(text, punctuation=True):
    """
    Delete special chars from a text

    Parameters
    ------------
        text : string
        punctuation : Delete punctutation or not
    """
    brackets_deleted = re.sub('\[[^]]*\]', '', text)
    pre_process = brackets_deleted.replace("(", "")
    pre_process = pre_process.replace(")", "")
    pre_process = pre_process.replace("\n", "")
    pre_process = pre_process.replace("\r", "")

    if punctuation:
        pre_process = pre_process.translate(translator)

    return pre_process


def w2v(tokenized_text):
    pass


default_bow_parameters = {'strip_accents': 'unicode',
                          'lowercase': True,
                          'stop_words': english_stopwords,
                          'ngram_range': (1, 3),
                          'analyzer': 'char'}


def bow(texts, parameters=default_bow_parameters, tfidf=True):
    """
    Create a vectorizer to convert texts into bag of words

    Parameters
    ------------
        texts : List of string
        parameters : parameters for your new representation
        tfidf : If you want a tfidf representation
    """

    if tfidf:
        vectorizer = TfidfVectorizer(**parameters)
    else:
        vectorizer = CountVectorizer(**parameters)

    texts_representation = vectorizer.fit_transform(texts)

    return texts_representation, vectorizer


def remove_words_from_df(df, list_words, columns_name):
    """
    Remove words from texts in a dataframe
    """
    pass


def remove_chars(string, chars_to_remove):
    """ Return string without the chars contained in chars_to_remove.
        Example :
        >>> remove_chars("Hello World !", " o!e")
        HllWrld
    """
    new_string = string
    chars_removed = 0
    for index, char in enumerate(string):
        for char_to_remove in chars_to_remove:
            if char == char_to_remove:
                new_string = remove_char_at(new_string, index - chars_removed)
                chars_removed += 1
                break
    return new_string


def remove_char_at(string, index):
    """ Return string minus the char at the place index.
        Example :
        >>> remove_char_at("Hello World !", 5)
        HelloWorld !
    """
    return string[:index] + string[index + 1:]


def remove_accents(string):
    """ Remove all accents from a string.

    Examples :
    >>> remove_accents("Málaga")
    Malaga
    """
    return unidecode.unidecode(string)


if __name__ == '__main__':
    pass
