""" A script for executing an entire experiment. """

import importlib
import os
import sys
from pathlib import Path

import numpy as np
import tqdm
from edo.pdfs import Distribution
from edo_exp import run_trial


class DiscreteUniform(Distribution):
    """ A discrete uniform distribution family.

    Attributes
    ----------
    name : str
        Name of the distribution, `"DiscreteUniform"`.
    dtype : str
        Preferred datatype, `"int"`.
    param_limits : dict
        A dictionary of limits on the bounds of the distribution.
    lower : float
        The lower bound of the distribution.
    upper : float
        The upper bound of the distribution.
    """

    name = "DiscreteUniform"
    dtype = "int"
    param_limits = {"bounds": [0, 10]}

    def __init__(self):

        lower, upper = sorted(self.param_limits["bounds"])
        lower = np.random.randint(lower, upper + 1)
        upper = np.random.randint(lower, upper + 1)
        self.bounds = [lower, upper]

    def sample(self, nrows):
        """ Take a sample of size `nrows` from the discrete uniform distribution
        with parameters given by `bounds`. """

        return np.random.randint(self.bounds[0], self.bounds[1] + 1, size=nrows)


EXPERIMENT = str(sys.argv[1])
PATH = Path(f"../../data/{EXPERIMENT}/")

NUM_CORES = int(sys.argv[2])
SIZE = int(sys.argv[3])
MAX_ITER = int(sys.argv[4])
SELECTION = float(sys.argv[5])
MUTATION = float(sys.argv[6])

MAX_SEED = int(sys.argv[7])

ROW_LIMITS = [50, 500]
COL_LIMITS = [2, 50]

PDFS = [DiscreteUniform]


def main():

    fitness = importlib.import_module(EXPERIMENT).fitness
    for seed in tqdm.tqdm(range(MAX_SEED)):

        seed_path = PATH / str(seed)
        data_path = seed_path / "data"
        data_path.mkdir(exist_ok=True, parents=True)

        run_trial(
            NUM_CORES,
            fitness,
            SIZE,
            ROW_LIMITS,
            COL_LIMITS,
            PDFS,
            MAX_ITER,
            SELECTION,
            MUTATION,
            data_path,
            seed,
            {"seed": seed},
        )


if __name__ == "__main__":
    main()
