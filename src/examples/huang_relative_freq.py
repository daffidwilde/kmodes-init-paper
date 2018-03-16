""" Get relative frequency table for Huang example. """

import pandas as pd

def get_rel_freq_table(data, idxs):
    """ Return relative frequency table for a given dataset. """

    relative_freqs = {
        col: data[col].value_counts(normalize=True) for col in data.columns
    }

    relative_freq_table = pd.DataFrame(relative_freqs.reindex(idxs).fillna(0))

    return relative_freq_table

def get_probability_dist(relative_freq_table):
    """ Get probability distribution for first attribute of a relative frequency
    table for Huang example. """

    pass
