""" Source code to produce datasets where the matching initialisation
outperforms Huang's method in terms of initial cost. """

import sys
from pathlib import Path

import numpy as np
from kmodes.kmodes import KModes
from edo_exp import run_trial

PATH = Path("../../../data/matching_over_huang_initial_cost/")

NUM_CORES = int(sys.argv[1])
SIZE = int(sys.argv[2])
SELECTION = float(sys.argv[3])
MUTATION = float(sys.argv[4])
SEED = int(sys.argv[5])


def difference_fitness(dataframe, n_clusters=3, seed=0):
    """ Cluster the data into `n_clusters` parts with each initialisation
    method. Return the difference between their initial costs so as to minimise
    that of the matching method. """

    km_matching = KModes(n_clusters=n_clusters, init="matching", max_iter=-1,
            n_init=25, random_state=seed).fit(dataframe)
    km_huang = KModes(n_clusters=n_clusters, init="huang", max_iter=-1,
            n_init=25, random_state=seed).fit(dataframe)

    return km_matching.cost_ - km_huang.cost_ # EDO minimises by default


def main(num_cores, size, selection, mutation, seed):
    """ Run a trial and write the datasets to file. """

    root = PATH / str(seed)
    root.mkdir(exist_ok=True, parents=True)

    data = root / "data"
    data.mkdir(exist_ok=True)

    row_limits = [50, 500]
    col_limits = [2, 50]

    run_trial(
        data, difference_fitness, num_cores, size, row_limits, col_limits,
        selection, mutation, seed, {"seed": seed}
    )


if __name__ == "__main__":
    main(NUM_CORES, SIZE, SELECTION, MUTATION, SEED)

