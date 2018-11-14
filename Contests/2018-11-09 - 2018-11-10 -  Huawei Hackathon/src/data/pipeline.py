import os
import pickle

import pandas as pd
import numpy as np

from glob import iglob
from multiprocessing import Pool


def iter_labels(path_dir, filename="true_labels_training.txt"):
    with open(path_dir + "/" + filename, 'r') as f:
        for y in str(f.readlines()[0]):
            yield y


def api_hist(df):
    return np.histogram(df.iloc[:, 2], bins=range(3561))[0]


def load_behavior(filename):
    df = pd.read_csv(filename, header=None)
    soft_id = int(df.iloc[0, 0].split("_")[1], 16)
    df.iloc[:, 0] = soft_id
    # df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: int(x, 16))s
    df.iloc[:, 2] = df.iloc[:, 2].apply(lambda x: info["api"]["index"][x])
    df.columns = ["id", "rip", "api"]
    return df


def transform(filename):
    df = load_behavior(filename)
    df.to_csv(filename[:-3] + "_transformed.txt")


def load_all_behaviors(directory, basename="transformed_training",
                       nb_thread=None):
    with Pool(nb_thread) as pool:
        df_list = pool.map(pd.read_csv, iglob(
            directory + "/" + basename + "_*_behavior*"))
    return df_list


def compute_all_hist(directory="training_dataset"):
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


def feature_sum_children(path, filename="nb_process_disctinct.txt"):
    with open(os.path.join(path, filename)) as file:
        truc = np.array(eval(file.read()))
    return pd.DataFrame(truc[:, 0], index=truc[:, 1])


def feature_max_api(df):
    return df.max(axis=1)


def feature_mean_api(df):
    return df.mean(axis=1)


def feature_std_api(df):
    return df.std(axis=1)


def feature_maxime(file_features="data_generated/features_generated.pickle"):
    with open(file_features, "rb") as f:
        return pd.DataFrame(np.array(pickle.load(f).todense()))


df = pd.read_csv("../hist_api.csv", index_col=0).astype(np.uint32)
df = pd.concat([df,
                feature_sum_api(df).astype(np.uint32),
                feature_notnull_api(df).astype(np.uint32),
                feature_max_api(df).astype(np.uint32),
                feature_mean_api(df).astype(np.float32),
                # feature_std_api(df).astype(np.float32),
                feature_sum_children(path="."),
                feature_maxime(file_features="data_generated/features_generated.pickle")],
               axis=1)
# df.columns.values[-5:] = ["sum_api", "notnull_api", "max_api",
#                          "mean_api", "std_api", "sum_children"]

datax_train = df.values
datay_train = np.array([y for y in iter_labels(path_dir=".")])

datax_test = pd.read_csv("validation_super_mega.csv", index_col=0).values
