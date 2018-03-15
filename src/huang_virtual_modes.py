""" Get virtual modes according to Huang's method and rank the elements of our
dataset by their dissimilarity with the first virtual mode; write to file. """

import pandas as pd
import numpy as np

from collections import defaultdict
from copy import deepcopy

def dissim(X, x):
    """ Return pointwise dissimilarity between x and all points in Y. """
    
    return np.sum(X != x, axis=1)

vehicle = pd.read_csv('../data/vehicle.csv', dtype='object')

vehicle.columns = [col.replace('_', '-').title() for col in vehicle.columns]
cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels', 'Eco-Friendly']
vehicle = vehicle[cols]

# Get virtual modes
data = vehicle.values
n_attrs = data.shape[1]
modes = np.empty((3, n_attrs), dtype='object')

for iattr in range(n_attrs):
    freq = defaultdict(int)
    for curattr in data[:, iattr]:
        freq[curattr] += 1

    choices = [chc for chc, wght in freq.items() for _ in range(wght)]

    choices = sorted(choices)
    modes[:, iattr] = np.random.choice(choices, 3)

tex = '\\begin{equation} \n\\begin{aligned} \n\t\\tilde{\\mu} = \\left\{ '
for mode in modes:
    tex += '& \\left['
    for val in mode:
        tex += '\\text{' + f'{val}' + '}, \ '
    tex = tex[:-4]
    tex += '\\right], \\\\ '
tex = tex[:-5]
tex += '\\right\} \\\\ \n\\end{aligned} \n\\end{equation}'

with open('../tex/huang_virtual_modes.tex', 'w') as out:
    out.write(tex)


# Get dissimilarity table
mode = modes[0, :]

dissim_df = deepcopy(vehicle)
dissim_df[r'Dissimilarity to $\tilde{\mu}_1$'] = dissim(data, mode)

dissim_df.sort_values(r'Dissimilarity to $\tilde{\mu}_1$',
                      ascending=True, inplace=True)

dissim_df.to_latex('../tex/huang_dissim.tex')
