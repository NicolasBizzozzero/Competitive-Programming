
# coding: utf-8

# In[13]:

import time

import pandas as pd
import os
import sys
from scipy.sparse import hstack
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from matplotlib import pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle


module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import src.utils.nlp as nlp
from src.data.loader import iter_data, iter_data_transformed
from src.models.other import xgboostWrapper

from src.data.submit import generate_submit, zipped
import glob

"""
path_save_api = '/home/cloud/hackathon/data_generated/'



path = '/home/cloud/hackathon/training_dataset/'#*_behavior_sequence._transformed.txt'
path_labels = '/home/cloud/hackathon/'
textlines = []
labels = []
for i, (x, y) in enumerate(iter_data(path, path_labels)):
    if i % 1000 == 0:
        print(i / 10000)

    if i < 10000:
        api = x['api'].apply(str).tolist()
        labels.append(y)
        textlines.append(' '.join(api))
    else:
        break

"""

"""
# Store data (serialize)
with open(path_save_api + 'api.pickle', 'wb') as handle:
    pickle.dump(textlines, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Store data (serialize)
with open(path_save_api + 'labels.pickle', 'wb') as handle:
    pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)
"""

"""
with open(path_save_api + 'api.pickle', 'wb') as handle:
    textlines = pickle.load(handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Store data (serialize)
with open(path_save_api + 'labels.pickle', 'wb') as handle:
    labels = pickle.load(handle, protocol=pickle.HIGHEST_PROTOCOL)


print("len textlines : ", len(textlines))
print("len labels : ", len(labels))

"""



"""
"""

# In[18]:



class XGboostWrapper:
    """
    Apply an XGboost model on a dataset with hyperparameters tuning
    """

    
    default_parameters = {
        'min_child_weight': [1, 5, 10],
        'gamma': [0.5, 1, 1.5, 2, 5],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [i for i in list(np.arange(0.2, 1.2, 0.2))],
        'max_depth': [i for i in range(1, 13, 3)], 
        'silent': [1],
        'n_estimators': [100, 200, 300]
        }
    

    def __init__(self, train_x, train_y, parameters=default_parameters, n_folds= 5, n_jobs=5, scoring_metrics='accuracy'):
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
        
        #self.columns_names = train_x.columns.tolist()
        #self.train_x = train_x.values
        #self.train_y = train_y.values
        
        self.train_x = train_x
        self.train_y = train_y
        
        self.xgb_model = xgb.XGBClassifier()
        
        self.gridSearch = GridSearchCV(self.xgb_model, parameters, n_jobs=n_jobs, 
                   cv=StratifiedKFold(n_splits=n_folds, shuffle=True), 
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
        plt.bar(self.columns_names , self.gridSearch.best_estimator_.feature_importances_)
        plt.show()



def train_model(path, path_labels, parameters):
    textlines = []
    labels = []
    for i, (x, y) in enumerate(iter_data(path, path_labels)):

        if i % 1000 == 0:
            print(i / 5000)

        if i < 5000:
            api = x['api'].apply(str).tolist()
            labels.append(y)
            textlines.append(' '.join(api))
        else:
            break


    default_bow_parameters_3_ngram = {'strip_accents': 'unicode',
                      'lowercase': True,
                      'ngram_range': (3, 3),
                      'analyzer': 'word', 
                      'max_features' : 100}
    texts_representation_3_ngram, vectorizer_3_ngram = nlp.bow(textlines, default_bow_parameters_3_ngram, tfidf=False)




    train_x = texts_representation_3_ngram



    #best_estimator, best_score = xgboost.find_best_model()

    #print("best score : ", best_score)

    return vectorizer_3_ngram


xgboost_parameters = {
    'min_child_weight': [1, 5, 10],
    'gamma': [1, 2, 5],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [i for i in list(np.arange(0.2, 1.2, 0.4))],
    'max_depth': [i for i in range(1, 13, 4)], 
    'silent': [1],
    'n_estimators': [100, 200]
    }
"""
path = '/home/cloud/hackathon/training_dataset/'#*_behavior_sequence._transformed.txt'
#path = '/home/cloud/hackathon/validation_dataset/'
path_labels = '/home/cloud/hackathon'
vectorizer_3_ngram = train_model(path, path_labels, xgboost_parameters)


filename = '/home/cloud/hackathon/data_generated/vectorizer_3_ngram.pickle'
pickle.dump(vectorizer_3_ngram, open(filename, 'wb'))
"""

vectorizer_3_ngram = pickle.load(open('/home/cloud/hackathon/data_generated/vectorizer_3_ngram.pickle', 'rb'))




def test_model(path_test, vectorizer_3_ngram):
    print("Debut du test ")
    validation_lines = []

    for i, x in enumerate(iter_data_transformed(path_test)):
        if i % 10000 == 0:
            print(i / 40000)


        api = x['api'].apply(str).tolist()
        validation_lines.append(' '.join(api))

    print(len(validation_lines))


    validation_representation_3_ngram = vectorizer_3_ngram.transform(validation_lines)
    #validation_representation_5_ngram = vectorizer_5_ngram.transform(validation_lines)

    print(validation_representation_3_ngram.shape)


    validation_x_reduced = validation_representation_3_ngram


    path_validation_tranformed = '/home/cloud/hackathon/data_generated/'
    with open(path_validation_tranformed + 'features_generated_validation.pickle', 'wb') as handle:
        pickle.dump(validation_x_reduced, handle, protocol=pickle.HIGHEST_PROTOCOL)


    #ypred = best_estimator.predict(validation_x_reduced)

    #ypred = [int(y) for y in ypred]
    #print(ypred)

    #generate_submit(ypred)
    #zipped('bow_prediction.zip', 'answer.txt')


start_time = time.time()
#path_validation = '/home/cloud/hackathon/training_dataset/'
path_validation = '/home/cloud/hackathon/validation_dataset/'
test_model(path_validation, vectorizer_3_ngram)
print("--- %s seconds ---" % (time.time() - start_time))





    


"""



        




default_bow_parameters_13_ngram = {'strip_accents': 'unicode',
                          'lowercase': True,
                          'ngram_range': (1, 3),
                          'analyzer': 'word', 
                          'max_features' : 3000}
texts_representation_13_ngram, vectorizer_13_ngram = nlp.bow(textlines, default_bow_parameters_13_ngram)


default_bow_parameters_5_ngram = {'strip_accents': 'unicode',
                          'lowercase': True,
                          'ngram_range': (5, 5),
                          'analyzer': 'word',
                          'max_features' : 3000}
texts_representation_5_ngram, vectorizer_5_ngram = nlp.bow(textlines, default_bow_parameters_5_ngram)


train_x = hstack((texts_representation_13_ngram, texts_representation_5_ngram))


clf_randomForest = RandomForestClassifier(n_estimators=100)
# In[7]:

clf_randomForest.fit(train_x, labels)
n = 3000
idx_most_important_features = clf_randomForest.feature_importances_.argsort()[-n:]


print("nb features : ", len(idx_most_important_features))

train_x = train_x.todense()

train_x_reduced = train_x[:, idx_most_important_features]

print("dataset reduced : ", train_x_reduced.shape)





xgboost = XGboostWrapper(train_x_reduced, labels)

best_estimator, best_score = xgboost.find_best_model()

print("best score : ", best_score)


path_validation = '/home/cloud/hackathon/validation_dataset/'#*_behavior_sequence._transformed.txt'
validation_lines = []

for i, x in enumerate(iter_data_transformed(path_validation)):
    if i % 1000 == 0:
        print(i / 40000)

    api = x['api'].apply(str).tolist()
    validation_lines.append(' '.join(api))


path_validation_tranformed = '/home/cloud/hackathon/data_generated'

    # Store data (serialize)
with open(path_validation_tranformed + 'validation_transformed.pickle', 'wb') as handle:
    pickle.dump(validation_lines, handle, protocol=pickle.HIGHEST_PROTOCOL)


print(len(validation_lines))


validation_representation_13_ngram = vectorizer_13_ngram.transform(validation_lines)
validation_representation_5_ngram = vectorizer_5_ngram.transform(validation_lines)

print(validation_representation_13_ngram.shape)
print(validation_representation_5_ngram.shape)

validation_x = hstack((validation_representation_13_ngram, validation_representation_5_ngram))

validation_x_reduced = validation_x.todense()[:, idx_most_important_features]


path_validation_tranformed = '/home/cloud/hackathon/data_generated'


ypred = best_estimator.predict(validation_x_reduced)

ypred = [int(y) for y in ypred]
print(ypred)

generate_submit(ypred)
zipped('xboost_10k.zip', 'answer.txt')

with open(path_validation_tranformed + 'validation_features.pickle', 'wb') as handle:
    pickle.dump(validation_x_reduced, handle, protocol=pickle.HIGHEST_PROTOCOL)


"""

