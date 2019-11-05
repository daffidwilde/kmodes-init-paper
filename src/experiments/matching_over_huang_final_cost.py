""" Fitness function to produce datasets where the matching initialisation
outperforms Huang's method in terms of final cost. """

from kmodes.kmodes import KModes


def fitness(dataframe, n_clusters=3, seed=0):
    """ Cluster the data into `n_clusters` parts with each initialisation
    method. Return the difference between their initial costs so as to minimise
    that of Huang's method. """

    km_matching = KModes(
        n_clusters=n_clusters, init="matching", n_init=25, random_state=seed
    ).fit(dataframe)
    km_huang = KModes(
        n_clusters=n_clusters, init="huang", n_init=25, random_state=seed
    ).fit(dataframe)

    return km_matching.cost_ - km_huang.cost_  # EDO minimises by default
