""" Generate all Huang example images. """

import pandas as pd

from util import get_mode_string
from huang_modes import get_initial_modes, get_virtual_modes
from huang_relative_freq import get_rel_freq_table, get_probability_dist
from huang_dissim_table import get_dissim_table


seed = 0
n_clusters = 3
vehicle = pd.read_csv("../../data/vehicle.csv", dtype="object")

# Format data for presentation.
vehicle.columns = [col.replace("_", "-").title() for col in vehicle.columns]
cols = ["Price", "Maintenance", "Doors", "Passengers", "Wheels", "Eco-Friendly"]
vehicle = vehicle[cols]

data = vehicle.values

# Get relative frequency table and probability distribution; write to file.
idxs = ["0", "1", "2", "3", "4", "5", "7", "8", "L", "M", "H", "V"]
relative_freq_table = get_rel_freq_table(vehicle, idxs)[cols]
probability_dist = get_probability_dist(relative_freq_table)

relative_freq_table.to_latex("../../tex/huang_relative_freq_table.tex")
probability_dist.to_latex("../../tex/huang_probability_dist.tex")

# Get mode strings; write to file.
virtual_modes = get_virtual_modes(data, n_clusters, seed)
initial_modes = get_initial_modes(data, n_clusters, seed)

for name, modes in zip(["virtual", "initial"], [virtual_modes, initial_modes]):

    path = f"../../tex/huang_{name}_modes.tex"
    string = get_mode_string(modes, name)

    with open(path, "w") as outfile:
        outfile.write(string)

# Get dissimilarity table; write to file.
dissim_table = get_dissim_table(vehicle, virtual_modes)

dissim_table.to_latex("../../tex/huang_dissim.tex")
