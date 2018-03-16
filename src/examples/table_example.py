""" Write toy example dataframe to LaTeX """

import pandas as pd

vehicle = pd.read_csv('../../data/vehicle.csv')

vehicle.columns = [col.replace('_', '-').title() for col in vehicle.columns]
cols = ['Price', 'Maintenance', 'Doors', 'Passengers', 'Wheels', 'Eco-Friendly']

vehicle = vehicle[cols]

vehicle.to_latex('../../tex/example_table.tex')
