""" Script for the collection and writing to LaTeX files of results for our
example datasets. """

import time

from glob import iglob
from pathlib import Path

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score, \
                            homogeneity_score, completeness_score
from kmodes.kmodes import KModes

###############
# DEFINITIONS #
###############

def get_prediction_results(X, y, init, n_clusters, seed):

    np.random.seed(seed)

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.3,
                                                        random_state=seed,
                                                        stratify=y)
    start = time.clock()
    kmodes = KModes(n_clusters, init=init, n_init=25)
    kmodes.fit(X_train)
    y_pred = kmodes.predict(X_test)
    time_taken = time.clock() - start

    adj_rand_idx = adjusted_rand_score(y_test, y_pred)
    adj_mutual_info = adjusted_mutual_info_score(y_test, y_pred)
    homogeneity = homogeneity_score(y_test, y_pred)
    completeness = completeness_score(y_test, y_pred)

    result = pd.DataFrame({'Initialisation': init.replace('_', ' ').title(),
                           'Adjusted Rand index': adj_rand_idx,
                           'Adjusted mutual information': adj_mutual_info,
                           'Homogeneity': homogeneity,
                           'Completeness': completeness,
                           'Time taken (s)': time_taken}, index=[''])
    return result

def get_clustering_results(data, init, n_clusters, seed):

    np.random.seed(seed)

    data = data.drop('class', axis=1)

    start = time.clock()
    kmodes = KModes(n_clusters, init=init, n_init=25)
    kmodes.fit_predict(data)
    time_taken = time.clock() - start

    result = pd.DataFrame({'Initialisation': init.replace('_', ' ').title(),
                           'Objective function': kmodes.cost_,
                           'No. of iterations': kmodes.n_iter_,
                           'Time taken (s)': time_taken}, index=[''])
    return result

def get_init_results(data, init, result_type, max_seed):

    y = data['class'].values
    n_clusters = len(np.unique(y))
    result_dfs = []

    if result_type == 'clustering':
        for seed in range(max_seed):
            result = get_clustering_results(data, init, n_clusters, seed)
            result_dfs.append(result)

        results = pd.concat(result_dfs)
        return results

    if result_type == 'prediction':    
        X = data.drop('class', axis=1).values
        for seed in range(max_seed):
            result = get_prediction_results(X, y, init, n_clusters, seed)
            result_dfs.append(result)

        results = pd.concat(result_dfs)
        return results

    raise ValueError('result_type must be one of "clustering" or "prediction"')

def latex_formatting(results):

    mean_df = results.groupby('Initialisation').mean().reset_index()
    mean_df[''] = 'mean'

    std_df = results.groupby('Initialisation').std().reset_index()
    std_df[''] = 'std'

    result = pd.concat([mean_df, std_df])

    return result.groupby(['Initialisation', '']).sum().round(4).T

def write_results(name, data, max_seed):

    clustering_path = Path('../tex/{name}_clustering_results.tex')
    prediction_path = Path('../tex/{name}_predicting_results.tex')

    if not clustering_path.exists():
        
        clust_result_dfs = []
        for init in ['cao', 'huang', 'random', 'matching_best',
                     'matching_worst', 'matching_random']:

            clust_result = get_init_results(dataset, init,
                                            'clustering', max_seed)
            clust_result_dfs.append(clust_result)
        
        clustering_results = pd.concat(clust_result_dfs)
        latex_formatting(clustering_results).to_latex(clustering_path)

    if not prediction_path.exists():
        
        pred_result_dfs = []
        for init in ['cao', 'huang', 'random', 'matching_best',
                     'matching_worst', 'matching_random']:

            pred_result = get_init_results(dataset, init,
                                           'prediction', max_seed)
            pred_result_dfs.append(pred_result)

        prediction_results = pd.concat(pred_result_dfs)
        latex_formatting(prediction_results).to_latex(prediction_path)

####################
# GET SOME RESULTS #
####################

max_seed = 10

inputs = [
    (Path(path).parts[-1].replace('.csv', ''), \
    pd.read_csv(path, na_values='?').dropna(axis=0, inplace=True)) \
    for path in iglob('../data/*.csv')
]

for name, dataset in inputs:
    write_results(name, dataset, max_seed)
