import numpy as np
import xgboost as xgb

from random import shuffle

def make_dataset(tree, min_nb_visits=5):
    global dataset
    for child in tree.childNodes:
        if child.visits > min_nb_visits:
            dataset.append((child.state.features, child.reward))
            make_dataset(child, min_nb_visits=min_nb_visits)

dataset = []
make_dataset(tree, 10)

shuffle(dataset)

x, y = zip(*dataset)

x_train = x[:int(len(x) * .8)]
y_train = y[:int(len(x) * .8)]
x_test  = x[int(len(x) * .8):]
y_test  = y[int(len(x) * .8):]

regressor = xgb.XGBRegressor(max_depth=3, n_estimators=100, n_jobs=1)
regressor.fit(x_train, y_train)
