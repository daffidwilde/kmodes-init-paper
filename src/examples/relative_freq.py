""" Write relative frequency table to tex file for Huang example. """

import pandas as pd

vehicle = pd.read_csv('../../data/vehicle.csv', dtype='object')

vehicle.columns = [col.replace('_', '-').title() for col in vehicle.columns]
cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels', 'Eco-Friendly']

vehicle = vehicle[cols]

idxs = ['0', '1', '2', '3', '4', '5', '7', '8', 'L', 'M', 'H', 'V']

relative_freq = pd.DataFrame(
    {col: vehicle[col].value_counts(normalize=True) \
     for col in vehicle.columns}).reindex(idxs).fillna(0)

relative_freq.to_latex('../../tex/relative_freq.tex')
