""" Collecting clustering and predictive results for our datasets. """

import time

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    adjusted_rand_score,
    adjusted_mutual_info_score,
    homogeneity_score,
    completeness_score,
)
from kmodes.kmodes import KModes


def get_prediction_results(X, y, init, n_clusters, seed):
    """ Get predictive model results: ARI, AMI, homogeneity, completeness;
    return them as a dataframe.

    Parameters
    ----------
    X : array
        Data array from which to get results
    y : array
        Target labels for points in X
    init : str
        Initialisation method for k-modes
    n_clusters : int
        Number of clusters to split X into
    seed : int
        Pseudo-random state

    Returns
    -------
    result : dataframe
        Result dataframe
    """

    np.random.seed(seed)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=seed, stratify=y
    )

    start = time.clock()
    kmodes = KModes(n_clusters, init=init, n_init=25)
    kmodes.fit(X_train)
    y_pred = kmodes.predict(X_test)
    time_taken = time.clock() - start

    adj_rand_idx = adjusted_rand_score(y_test, y_pred)
    adj_mutual_info = adjusted_mutual_info_score(y_test, y_pred)
    homogeneity = homogeneity_score(y_test, y_pred)
    completeness = completeness_score(y_test, y_pred)

    result = pd.DataFrame(
        {
            "Initialisation": init.replace("_", " ").title(),
            "Adjusted Rand index": adj_rand_idx,
            "Adjusted mutual information": adj_mutual_info,
            "Homogeneity": homogeneity,
            "Completeness": completeness,
            "Time taken (s)": time_taken,
        },
        index=[""],
    )
    return result


def get_clustering_results(data, init, n_clusters, seed):
    """ Get clustering results: objective function (summed within-cluster
    dissimilarity), number of iterations; return them as a dataframe.

    Parameters
    ----------
    data : dataframe
        Dataset from which to get results
    init : str
        Initialisation method for k-modes
    n_clusters : int
        Number of clusters to split X into
    seed : int
        Pseudo-random state

    Returns
    -------
    result : dataframe
        Results dataframe
    """

    np.random.seed(seed)

    data = data.drop("class", axis=1)

    start = time.clock()
    kmodes = KModes(n_clusters, init=init, n_init=25)
    kmodes.fit_predict(data)
    time_taken = time.clock() - start

    result = pd.DataFrame(
        {
            "Initialisation": init.replace("_", " ").title(),
            "Objective function": kmodes.cost_,
            "No. of iterations": kmodes.n_iter_,
            "Time taken (s)": time_taken,
        },
        index=[""],
    )
    return result


def get_init_results(data, init, result_type, max_seed):
    """ Get results from max_seed runs of k-modes. """

    X = data.drop("class", axis=1).values
    y = data["class"].values
    n_clusters = len(np.unique(y))
    result_dfs = []

    if result_type == "clustering":
        for seed in range(max_seed):
            result = get_clustering_results(data, init, n_clusters, seed)
            result_dfs.append(result)

        results = pd.concat(result_dfs)
        return results

    if result_type == "prediction":
        for seed in range(max_seed):
            result = get_prediction_results(X, y, init, n_clusters, seed)
            result_dfs.append(result)

        results = pd.concat(result_dfs)
        return results

    raise ValueError('result_type must be one of "clustering" or "prediction"')
