""" Get datasets from URLs (or make locally); save to data folder. """

import pathlib
import pandas as pd

# Create ../data/ directory, if it doesn't already exist.
pathlib.Path('../data/').mkdir(parents=True, exist_ok=True)


# Get datasets from URLs where possible, attach column names.
soybean = pd.read_csv('https://archive.ics.uci.edu/ml/'
                      'machine-learning-databases/soybean/soybean-large.data',
                      names=['class', 'date', 'plant_stand', 'precip', 'temp',
                             'hail', 'crop_hist', 'area_damaged', 'severity',
                             'seed_tmt', 'germination', 'plant_growth',
                             'leaves', 'leafspots_halo', 'leafspots_marg',
                             'leafspots_size', 'leaf_shread', 'leaf_malf',
                             'leaf_mild', 'stem', 'lodging', 'stem_cankers',
                             'canker_lesion', 'fruiting_bodies',
                             'external_decay', 'mycelium', 'int_discolor',
                             'sclerotia', 'fruit_pods', 'fruitspots', 'seed',
                             'mold_growth', 'seed_discolor', 'seed_size',
                             'shriveling', 'roots'])

mushroom = pd.read_csv('https://archive.ics.uci.edu/ml/'
                       'machine-learning-databases/mushroom/'
                       'agaricus-lepiota.data',
                       names=['class', 'cap_shape', 'cap_surface', 'cap_color',
                              'bruises', 'odor', 'gill_attachment',
                              'gill_spacing', 'gill_size', 'gill_color',
                              'stalk_shape', 'stalk_root',
                              'stalk_surface_above_ring',
                              'stalk_surface_below_ring',
                              'stalk_color_above_ring',
                              'stalk_color_below_ring', 'veil_type',
                              'veil_color', 'ring_number', 'ring_type',
                              'spore_print_color', 'population', 'habitat'])

zoo = pd.read_csv('http://archive.ics.uci.edu/ml/'
                  'machine-learning-databases/zoo/zoo.data',
                  names=['animal_name', 'hair', 'feathers', 'eggs', 'milk',
                         'airborne', 'aquatic', 'predator', 'toothed',
                         'backbone', 'breathes', 'venomous', 'fins', 'legs',
                         'tail', 'domestic', 'catsize', 'class'])

breast_cancer = pd.read_csv('https://archive.ics.uci.edu/ml/'
                            'machine-learning-databases/'
                            'breast-cancer-wisconsin/'
                            'breast-cancer-wisconsin.data',
                            names=['id_number', 'clump_thickness',
                                   'cell_size_uniformity',
                                   'cell_shape_uniformity',
                                   'marginal_adhesion',
                                   'single_epithelial_size', 'bare_nuclei',
                                   'bland_chromatin', 'normal_nucleoli',
                                   'mitoses', 'class'])

# Create the toy example by hand
vehicle = pd.DataFrame({
    'price': ['H', 'L', 'V', 'H', 'M', 'M', 'V', 'L', 'H', 'H'],
    'maintenance': ['M', 'M', 'H', 'L', 'M', 'L', 'H', 'V', 'M', 'M'],
    'doors': [2, 0, 2, 4, 2, 2, 4, 2, 0, 4],
    'passengers': [2, 1, 3, 5, 5, 4, 5, 4, 2, 7],
    'wheels': [4, 2, 8, 4, 4, 4, 4, 4, 2, 4],
    'eco_friendly': [0, 0, 0, 1, 1, 1, 0, 0, 1, 0]
})


# Write them all to file
for name, dataset in zip(['soybean', 'mushroom',
                          'zoo', 'breast_cancer', 'vehicle'],
                          [soybean, mushroom,
                           zoo, breast_cancer, vehicle]):
    dataset.to_csv(f'../data/{name}.csv', index=False)
