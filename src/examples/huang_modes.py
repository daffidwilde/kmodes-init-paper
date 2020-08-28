""" Find initial modes by Huang's method, and write to file. """

from collections import defaultdict

import numpy as np
from kmodes.kmodes import init_huang
from util import dissim


def get_virtual_modes(data, n_clusters, seed=0):
    """ Find virtual modes by sampling from the relative frequencies of the
    attribute values in data. """

    np.random.seed(seed)
    n_attrs = data.shape[1]
    modes = np.empty((n_clusters, n_attrs), dtype="object")

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
    """ Find initial modes by Huang's method, seeded. """

    np.random.seed(seed)
    modes = init_huang(data, n_clusters, dissim)

    return modes
