import lightgbm as lgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from matplotlib import pyplot as plt
import numpy as np

class LightGBMWrapper:
    """
    Apply an light GBM model on a dataset with hyperparameters tuning
    """
    params = {'boosting_type': 'gbdt',
              'max_depth' : 5,
              'objective': 'binary',
              'num_leaves': 64,
              'learning_rate': 0.05,
              'subsample': 1,
              'colsample_bytree': 0.8,
              'max_bin' : 10}

    # Create parameters to search
    default_parameters = {
        'n_estimators': [100, 200, 300],
        'num_leaves': [6,8,12],
        'boosting_type' : ['gbdt'],
        'objective' : ['binary'],
        'colsample_bytree': [i for i in list(np.arange(0.2, 1.2, 0.2))],
        'subsample': [0.6, 0.8, 1.0],
        'max_depth': [i for i in range(1, 13, 2)],
        'min_child_weight': [1, 5, 10]
        }

    
    def __init__(self, train_x, train_y, parameters=default_parameters, n_folds= 5, n_jobs=5, scoring_metrics='accuracy'):
        """
        Instantiate a light GBM object.
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


        self.lgbm_model = lgb.LGBMClassifier(boosting_type= 'gbdt',
                  objective = 'binary',
                  n_jobs = n_jobs
                  silent = True,
                  max_bin = self.params['max_bin'],
                  max_depth = self.params['max_depth'],
                  #subsample_for_bin = self.params['subsample_for_bin'],
                  subsample = self.params['subsample'])
                  #subsample_freq = self.params['subsample_freq'],
                  #min_split_gain = self.params['min_split_gain'])
                  #min_child_weight = self.params['min_child_weight']
                  #min_child_samples = self.params['min_child_samples'],
                  #scale_pos_weight = self.params['scale_pos_weight'])
        
        
        self.gridSearch = GridSearchCV(self.lgbm_model, parameters, n_jobs=n_jobs, 
                   cv=StratifiedKFold(n_splits=n_folds, shuffle=True), 
                   scoring=scoring_metrics,
                   refit=True, 
                   verbose=10)
      
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
        plt.bar(self.columns_names , self.gridSearch.best_estimator_.feature_importances_)
        plt.show()
        