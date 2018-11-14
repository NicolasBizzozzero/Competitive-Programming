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


input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if not os.path.isdir(submit_dir):
    print("%s doesn't exist" % submit_dir)

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')
    output_file = open(output_filename, 'w')

    truth_file = os.path.join(truth_dir, "truth.txt")
    truth = truth_to_arr(truth_file)
    # truth = np.asarray(eval(open(truth_file).read()))

    submission_answer_file = os.path.join(submit_dir, "answer.txt")
    answer = answer_to_arr(submission_answer_file)
    # submission_answer = np.asarray(eval(open(submission_answer_file).read()))

    score = roc_auc_score(truth, answer)
    output_file.write("score:{}".format(score))

    output_file.close()
