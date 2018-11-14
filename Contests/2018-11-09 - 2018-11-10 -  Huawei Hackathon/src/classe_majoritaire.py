from collections import Counter

import numpy as np

import zipfile

PATH_OUTPUT = "bagging6.zip"


def generate_submit(tab):
    """ tab->list  :    prediction
        create the file and write the prediction
        have to be in the good order
       """
    with open("answer.txt", 'w') as f:
        for i in tab:
            f.write(str(i) + '\n')


def zipped(file_name='answer.zip', file_to_zip='answer.txt'):
    """ file_name -> str the name of the zipped file
        file_to_zip -> str the name of the file to zip
        zip the file file_to_zip"""
    zip = zipfile.ZipFile(file_name, 'w')
    zip.write(file_to_zip)
    zip.close()


with open("adrien2.txt") as f:
    y_adrien2 = np.array(list(map(float, f.read().strip().split("\n"))))


with open("mega_rf100.txt") as f:
    y_mega_rf100 = np.array(list(map(float, f.read().strip().split("\n"))))


with open("mlp_pred.txt") as f:
    y_mlp_pred = np.array(list(map(float, f.read().strip().split("\n"))))

with open("rf_500_entrop.txt") as f:
    y_rf_500_entrop = np.array(list(map(float, f.read().strip().split("\n"))))


with open("rf50.txt") as f:
    y_rf50 = np.array(list(map(float, f.read().strip().split("\n"))))


with open("xgboost100.txt") as f:
    y_xgboost100 = np.array(list(map(float, f.read().strip().split("\n"))))


y_bagged = np.vstack(
    (y_adrien2, y_mega_rf100, y_mlp_pred, y_rf_500_entrop, y_rf50,
        y_xgboost100)).T
y_bagged = y_bagged.mean(axis=1)


with open("answer.txt", "w") as f:
    for y in y_bagged:
        f.write(str(y) + "\n")

zipped(file_name=PATH_OUTPUT, file_to_zip="answer.txt")
