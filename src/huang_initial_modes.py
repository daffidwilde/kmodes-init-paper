""" Find initial modes by Huang's method, and write to file. """

import pandas as pd
import numpy as np

from kmodes.kmodes import init_huang


def dissim(Y, x):
    """ Pointwise dissimilarity between x and all points in Y. """

    return np.sum(Y != x, axis=1)

vehicle = pd.read_csv('../data/vehicle.csv', dtype='object')

vehicle.columns = [col.replace('_', '-').title() for col in vehicle.columns]
cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels', 'Eco-Friendly']

np.random.seed(0)
vehicle = vehicle[cols]
data = vehicle.values
modes = init_huang(data, 3, dissim)

tex = '\\begin{equation} \n\\begin{aligned} \n\t\\bar{\\mu} = \\left\{ '
for mode in modes:
    tex += '& \\left['
    for val in mode:
        tex += '\\text{' + f'{val}' + '}, \ '
    tex = tex[:-4]
    tex += '\\right], \\\\ '
tex = tex[:-5]
tex += '\\right\} \\\\ \n\\end{aligned} \n\\end{equation}'

with open('../tex/huang_initial_modes.tex', 'w') as out:
    out.write(tex)
