import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from matplotlib import pyplot as plt
import numpy as np


class XGboostWrapper:
    """
    Apply an XGboost model on a dataset with hyperparameters tuning
    """

    default_parameters = {
        'min_child_weight': [1, 5, 10],
        'gamma': [0.5, 1, 1.5, 2, 5],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [i for i in list(np.arange(0.2, 1.2, 0.2))],
        'max_depth': [i for i in range(1, 13)],
        'silent': [1],
        'n_estimators': [100, 200, 300]
    }

    def __init__(self, train_x, train_y, parameters=default_parameters, n_folds=5, n_jobs=5, scoring_metrics='accuracy'):
        """
        Instantiate a XGboost object.
        Parameters
        ------------
            train_x : A pandas dataframe with all the features
            train_y : A pandas dataframe with the ground truth
            parameters : dictionary of paramters used for grid search : https://xgboost.readthedocs.io/en/latest/parameter.html
            n_fold : Number of partitions for the cross validation
            n_jobs : Number of jobs for parallel execution 
            scoring_metrics : you can see both there : http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
        """

        self.columns_names = train_x.columns.tolist()
        self.train_x = train_x.values
        self.train_y = train_y.values

        self.xgb_model = xgb.XGBClassifier()

        self.gridSearch = GridSearchCV(self.xgb_model, parameters, n_jobs=n_jobs,
                                       cv=StratifiedKFold(
                                           n_splits=n_folds, shuffle=True),
                                       scoring=scoring_metrics,
                                       refit=True)

    def find_best_model(self):
        """
        Perform the grid search and return the best model and best model score on cross validation
        """

        self.gridSearch.fit(self.train_x, self.train_y)

        return self.gridSearch.best_estimator_, self.gridSearch.best_score_

    def get_most_important_features_plot(self):
        """
        Plot the most important features for XGboost decision
        """
        plt.bar(self.columns_names,
                self.gridSearch.best_estimator_.feature_importances_)
        plt.show()
