import numpy as np
import pandas as pd
from glob import iglob
import os


def api_hist(df):
    return np.histogram(df.iloc[:, 2], bins=range(3561))[0]


def compute_all_hist(directory):
    ret = {}
    for filename in iglob(directory + "/*transformed*"):
        training_id = int(filename.split("_")[2])
        ret[training_id] = api_hist(pd.read_csv(filename, index_col=0))
    df = pd.DataFrame(ret).T
    return df


def feature_sum_api(df):
    return df[df != 0].sum(axis=1)


def feature_notnull_api(df):
    return df.astype(bool).sum(axis=1)


def feature_sum_children(path, filename="nb_process_distinct_validation.txt"):
    with open(os.path.join(path, filename)) as file:
        truc = np.array(eval(file.read()))
    return pd.DataFrame(truc[:, 0], index=truc[:, 1])


df = pd.read_csv("../hist_api.csv", index_col=0).astype(np.uint32)
df = pd.concat([df,
                feature_sum_api(df).astype(np.uint32),
                feature_notnull_api(df).astype(np.uint32),
                feature_sum_children(path=".")],
               axis=1)
df.columns.values[-3:] = ["sum_api", "notnull_api", "sum_children"]
