""" Get ranked tables for Cao's method example. """

from copy import deepcopy
import numpy as np

from util import dissim, density


def get_density_table(data):
    """ Take a dataset, calculate the average density of each point; return the
    dataset with a density column added, ranking the elements of the dataset by
    their density. """

    density_table = deepcopy(data)
    values = data.values
    densities = [density(values, point) for point in values]

    density_table['Density'] = densities
    density_table.sort_values('Density', ascending=True, inplace=True)

    cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels',
            'Eco-Friendly', 'Density']

    return density_table[cols]

def get_density_dissim_table(data, mode):
    """ Take a dataset, add columns for density, dissimilarity to a mode, and
    their product; rank the elements of the dataset by this product. """

    values = data.values
    densities = np.array([density(values, point) for point in values])
    dissims = dissim(values, mode)

    density_dissim_table = deepcopy(data)

    density_dissim_table['Density'] = densities
    density_dissim_table[r'Dissimilarity to $\bar{\mu}_1$'] = dissims
    density_dissim_table['Density-dissimilarity'] = densities * dissims

    density_dissim_table.sort_values('Density-dissimilarity',
                                     ascending=True, inplace=True)

    cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels',
            'Eco-Friendly', 'Density', r'Dissimilarity to $\bar{\mu}_1$',
            'Density-dissimilarity']

    return density_dissim_table[cols]
