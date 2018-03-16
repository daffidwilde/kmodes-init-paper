""" Get mode of toy dataset according to theorem. """

import pandas as pd

vehicle = pd.read_csv('../../data/vehicle.csv', dtype='object')

vehicle.columns = [col.replace('_', '-').title() for col in vehicle.columns]
cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels', 'Eco-Friendly']

vehicle = vehicle[cols]
mode = vehicle.describe().loc['top'].values

tex = '\\[ \n \t \mu = \\left['
for value in mode:
    tex += '\\text{' + f'{value}' '}, \ '
tex = tex[:-4]
tex += '\\right] \n\]'

with open('../../tex/top_mode.tex', 'w') as out:
    out.write(tex)
