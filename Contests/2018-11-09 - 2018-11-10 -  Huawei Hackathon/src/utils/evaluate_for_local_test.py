#!/usr/bin/env python
import sys
import os
import os.path
import numpy as np
from sklearn.metrics import roc_auc_score


def answer_to_arr(path):
    return np.asarray(list(map(float, open(path, 'r').read().splitlines())))


def truth_to_arr(path):
    return np.asarray(list(map(float, open(path, 'r').read())))


# put your own truth file path here
truth_file = "true_labels_validation.txt"

# put your own answer file path here
submission_answer_file = "_code/test_random_validation.txt"
submission_answer_file = "_code/test_naive_validation.txt"
submission_answer_file = "_code/test_unigram_validation.txt"

truth = truth_to_arr(truth_file)
answer = answer_to_arr(submission_answer_file)
score = roc_auc_score(truth, answer)
print("score:{}".format(score))
