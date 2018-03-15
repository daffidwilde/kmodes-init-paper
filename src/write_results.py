""" Formatting and writing results to a LaTeX file. """

from pathlib import Path
import pandas as pd

from get_results import get_init_results

def format_results(results):
    """ Take a results dataframe, get the mean and std out for each
    initialisation process; return a concatenation of these that is rounded and
    transposed. """

    mean_df = results.groupby('Initialisation').mean().reset_index()
    mean_df[''] = 'mean'

    std_df = results.groupby('initialisation').std().reset_index()
    std_df[''] = 'std'

    result = pd.concat([mean_df, std_df])

    return result.groupby(['Initialisation', '']).sum().T.round(4)

def write_results(name, data, max_seed):
    """ Write result dataframes to file if they don't already exist.

    Parameters
    ----------
    name : str
        Name of dataset
    data : dataframe
        Dataset from which to get results
    max_seed : int
        Maximum number of runs to take results over
    """

    clustering_path = Path(f'../tex/{name}_clustering_results.tex')
    prediction_path = Path(f'../tex/{name}_predicting_results.tex')

    if not clustering_path.exists():

        clust_result_dfs = []
        for init in ['cao', 'huang', 'random', 'matching_best',
                     'matching_worst', 'matching_random']:

            clust_result = get_init_results(data, init,
                                            'clustering', max_seed)
            clust_result_dfs.append(clust_result)

        clustering_results = pd.concat(clust_result_dfs)
        format_results(clustering_results).to_latex(clustering_path)

    if not prediction_path.exists():

        pred_result_dfs = []
        for init in ['cao', 'huang', 'random', 'matching_best',
                     'matching_worst', 'matching_random']:

            pred_result = get_init_results(data, init,
                                           'prediction', max_seed)
            pred_result_dfs.append(pred_result)

        prediction_results = pd.concat(pred_result_dfs)
        format_results(prediction_results).to_latex(prediction_path)
