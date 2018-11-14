import numpy as np
from sklearn.preprocessing import StandardScaler

import os

malimg_dataset_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../data/external/malimg-dataset/malimg.npz")
def load_malimg(path_file=malimg_dataset_path, standardize=True):
    """
    :param dataset:
    :param standardize:
    :return:
    """
    with np.load(path_file) as dataset:
        features = dataset['arr'][:, 0]
        features = np.array([feature for feature in features])
        features = np.reshape(features,
                              (features.shape[0],
                               features.shape[1] * features.shape[2]))

        if standardize:
            features = StandardScaler().fit_transform(features)

        labels = dataset['arr'][:, 1]
        labels = np.array([label for label in labels])

        return features, labels


if __name__ == '__main__':
    features, labels = load_malimg()
    print("Dataset MalImg has", len(labels), "data")
