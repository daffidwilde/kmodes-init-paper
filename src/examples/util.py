""" A collection of useful functions for the examples. """

import numpy as np


def dissim(Y, x):
    """ Pointwise dissimilarity between x and all points in Y. """

    return np.sum(Y != x, axis=1)

def density(Y, x):
    """ Average density of a point, x, in a dataset Y. """

    N, m = Y.shape
    summed_dissim = np.sum(dissim(Y, x))

    return 1 - summed_dissim / (N * m)

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
