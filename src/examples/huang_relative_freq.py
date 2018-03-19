""" Get relative frequency table for Huang example. """

import pandas as pd

def get_rel_freq_table(data, idxs):
    """ Return relative frequency table for a given dataset. """

    relative_freqs = {
        col: data[col].value_counts(normalize=True) for col in data.columns
    }

    relative_freq_table = pd.DataFrame(relative_freqs).reindex(idxs).fillna(0)

    return relative_freq_table

def get_probability_dist(relative_freq_table):
    """ Get probability distribution for first attribute of a relative frequency
    table for Huang example. """

    first_attr = relative_freq_table.iloc[:, 0]
    values, relative_freqs = first_attr.index, first_attr.values

    prob_dist_dict = {
        val: freq for val, freq in zip(values, relative_freqs) if freq > 0
    }

    probability_dist = pd.DataFrame(prob_dist_dict, index=[''])
    probability_dist[r'$A_1$'] = r'$\mathbb{P}(A_1 = a^{(1)})$'

    return probability_dist.set_index(r'$A_1$')[['L', 'M', 'H', 'V']]
