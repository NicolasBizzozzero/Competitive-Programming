import pandas as pd
import os.path as path
from glob import iglob, glob
from multiprocessing import Pool
from torch.utils.data import Dataset
import numpy as np
import os
import torch

from threading import Thread

info = {
    "basename": {"behavior": "_behavior_sequence.txt", "process": "_process_generation.txt",
                 "api": "api_"},
    "api": {"index": {"api_" + str(i).zfill(4): i for i in range(3561)}, "inverse": {i: "api_" + str(i) for i in range(3561)}},
}


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
    toto = Thread(target=df.to_csv(filename[:-3] + "_transformed.txt")).start()
    return df  # , training_id


def load_all_behaviors(directory, basename="transformed_training",
                       nb_thread=None):
    with Pool(nb_thread) as pool:
        df_list = pool.map(load_behavior, iglob(
            directory + "/" + basename + "_*_behavior*"))
    return df_list


def load_labels(filename):
    y = []
    with open(file_name, 'r') as f:
        line = str(f.readlines()[0])
        for i in line:
            y.append(int(i))
        print('true: ', true_label, 'false: ', false_label)


def load_process_tree(filename):
    process_tree = {}
    with open(filename, "r") as f:
        first = f.readline()
        process_id = int(first.split("->")[1].split("_")[1], 16)
        process_tree["root"] = process_id
        for line in f:
            father, son = line.split("->")
            father_id = int(father.split("_")[1], 16)
            son_id = int(son.split("_")[1], 16)
            if father_id not in process_tree:
                process_tree[father_id] = []
            process_tree[father_id].append(son_id)
    return process_tree


def iter_data_transformed(path_dir_data):
    for file in sorted(glob(path_dir_data + "/" + "*_transformed*")):
        yield pd.read_csv(file)  # ["api"].count()


def iter_labels(path_dir, filename="true_labels_training.txt"):
    with open(path_dir + "/" + filename, 'r') as f:
        for y in str(f.readlines()[0]):
            yield y


def iter_data(path_dir_data, path_target):
    for x, y in zip(iter_data_transformed(path_dir_data), iter_labels(path_target)):
        yield x, y


def api_hist(df):
    return np.histogram(df.iloc[:, 2], bins=range(3561))[0]


def compute_all_hist(list_df, directory):
    ret = {}
    for df, filename in zip(list_df, iglob(directory + "/*behavior*")):
        training_id = int(filename.split("_")[2])
        ret[training_id] = api_hist(df)
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


def load_process_tree(filename):
    process_tree = {}
    with open(filename, "r") as f:
        first = f.readline()
        process_id = first.split("->")[1].split("_")[1]
        process_tree["root"] = process_id
        for line in f:
            father, son = line.split("->")
            father_id = father.split("_")[1]
            son_id = son.split("_")[1]
            if father_id not in process_tree:
                process_tree[father_id] = []
            process_tree[father_id].append(son_id)
    exemple_id = int(filename.split('_')[2])
    return process_tree, exemple_id


def load_all_tree(directory, basename="validation", nb_thread=None):
    with Pool(nb_thread) as pool:
        df_list = pool.map(len_tree, iglob(
            directory + "/" + basename + "_*_process_generation.txt"))
    return df_list


def len_tree(filename):
    a = load_process_tree(filename)
    return len(a[0]), a[1]


def pipeline(dir_data="validation_dataset", basename="validation"):
    list_df = load_all_behaviors(dir_data, basename=basename,
                                 nb_thread=None)
    df = compute_all_hist(list_df, dir_data)
    truc = load_all_tree(dir_data, basename=basename)
    truc = np.array(truc)
    df_tree = pd.DataFrame(truc[:, 0], index=truc[:, 1])
    df = pd.concat([df,
                    df_tree,
                    feature_sum_api(df).astype(np.uint64),
                    feature_notnull_api(df).astype(np.uint64),
                    feature_max_api(df).astype(np.uint64),
                    feature_mean_api(df).astype(np.float64),
                    feature_std_api(df).astype(np.float64)
                    ],
                   axis=1)
    tenseur = torch.Tensor(df.values)
    torch.save(tenseur, "testdata.torchsave")
