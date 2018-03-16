""" Find initial modes by Huang's method, and write to file. """

from collections import defaultdict
import numpy as np

from kmodes.kmodes import init_huang


def dissim(Y, x):
    """ Pointwise dissimilarity between x and all points in Y. """

    return np.sum(Y != x, axis=1)

def get_virtual_modes(data, n_clusters, seed=0):
    """ Find virtual modes by sampling from the relative frequencies of the
    attribute values in data. """

    np.random.seed(seed)
    n_attrs = data.shape[1]
    modes = np.empty((n_clusters, n_attrs), dtype='object')

    for i_attr in range(n_attrs):
        freq = defaultdict(int)
        for curr_attr in data[:, i_attr]:
            freq[curr_attr] += 1

        choices = [
            choice for choice, weight in freq.items() for _ in range(weight)
        ]

        choices = sorted(choices)
        modes[:, i_attr] = np.random.choice(choices, n_clusters)

    return modes

def get_initial_modes(data, n_clusters, seed=0):
    """ Find initial modes by Huang's method; return them as a LaTeX string. """

    np.random.seed(seed)
    modes = init_huang(data, n_clusters, dissim)

    return modes

def get_mode_string(modes, mode_type):
    """ Take an array of modes; return LaTeX string. """

    if mode_type == 'virtual':
        notation = 'tilde'
    elif mode_type == 'initial':
        notation = 'bar'

    tex = '\\begin{equation} \n\\begin{aligned} \n\t\\' \
            + f'{notation}' + '{\\mu} = \\left\{ '

    for mode in modes:
        tex += '& \\left['
        for value in mode:
            tex += '\\text{' + f'{value}' + '}, \ '
        tex = tex[:-4]
        tex += '\\right], \\\\ '
    tex = tex[:-5]
    tex += '\\right\} \\\\ \n\\end{aligned} \n\\end{equation}'

    return tex
