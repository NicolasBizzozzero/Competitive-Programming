import catboost as cb
from sklearn.model_selection import GridSearchCV
from matplotlib import pyplot as plt
import numpy as np

class CatboostWrapper(object):
    default_parameters = {'depth':[3,1,2,6,4,5,7,8],
                          'iterations':[250,100, 500],
                          'learning_rate':[0.03,0.001,0.01,0.1], 
                          'l2_leaf_reg':[3,1,4]}


    def __init__(self, train_x, train_y, parameters=default_parameters, cat_features_index=None, max_one_hot=None, n_folds=3, n_jobs=-1, scoring_metrics='accuracy'):
        #train_x is a dataframe
        #train_y is a dataframe
        
        self.train_x = train_x
        self.train_y = train_y
        self.cat = cat_features_index
        self.max_one_hot = max_one_hot
        
        self.cb_model = cb.CatBoostClassifier(logging_level='Silent', one_hot_max_size=self.max_one_hot)
        
        self.gridSearch = GridSearchCV(self.cb_model, parameters, scoring=scoring_metrics, cv = n_folds, refit=True, verbose=1)
        
    def find_best_model(self):
        self.gridSearch.fit(self.train_x.values, self.train_y.values, cat_features=self.cat)
        return self.gridSearch.best_params_, self.gridSearch.best_score_
        
        
    def get_most_important_features_plot(self):
        plt.figure()
        plt.bar(self.train_x.columns.tolist(), self.gridSearch.best_estimator_.feature_importances_)
        plt.show()
        
    def predict(self, X):
        return self.gridSearch.predict(X)
        
        
class RandomForestWrapper(object):
    default_parameters = {'n_estimators': [100, 200, 500],
                          'max_features': ['auto', 'log2'],
                          'max_depth' : [1,2,3,4,5,6,7,8],
                          'criterion' :['gini', 'entropy']
                          }
    
    def __init__(self, train_x, train_y, parameters=default_parameters, n_folds= 5, n_jobs=-1, scoring_metrics='accuracy'):
        #train_x is a dataframe
        #train_y is a dataframe
        
        self.train_x = train_x
        self.train_y = train_y
        
        self.model = RandomForestClassifier()
        
        self.gridSearch = GridSearchCV(self.model, parameters, scoring=scoring_metrics, cv = n_folds, refit=True)
      
    def find_best_model(self):
        self.gridSearch.fit(self.train_x.values, self.train_y.values)
        return self.gridSearch.best_params_, self.gridSearch.best_score_
        
        
    def get_most_important_features_plot(self):
        plt.figure()
        plt.bar(self.train_x.columns.tolist(), self.gridSearch.best_estimator_.feature_importances_)
        plt.show()
        
    def predict(self, X):
        return self.gridSearch.predict(X)
        
        
        
