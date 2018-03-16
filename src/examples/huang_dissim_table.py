""" Get ranked dissimilarity table for virtual modes by Huang's method. """

from copy import deepcopy

from huang_modes import dissim

def get_dissim_table(data, modes):
    """ Take a dataset and some modes; return the dataset ranked by the
    dissimilarity of its points to the first element of modes. """

    mode = modes[0, :]
    dissim_table = deepcopy(data)
    dissim_col = r'Dissimilarity to $\tilde{\mu}_1$'

    dissim_table[dissim_col] = dissim(data, mode)
    dissim_table.sort_values(dissim_col, ascending=True, inplace=True)

    return dissim_table
