""" Write results to file for each dataset in ../../data/ directory. """

from glob import iglob
from pathlib import Path

import pandas as pd

from write_results import write_results


def get_name(path):
    """ Get name of dataset from its path. """

    return Path(path).parts[-1].replace(".csv", "")


def get_dataset(path):
    """ Read in dataset from path, dropping missing values. """

    return pd.read_csv(path, na_values="?").dropna(axis=0, inplace=True)


max_seed = 10

inputs = [
    (get_name(path), get_dataset(path)) for path in iglob("../../data/*.csv")
]

for name, dataset in inputs:
    write_results(name, dataset, max_seed)
