""" Fitness function to produce datasets where Huang's method outperforms
the matching initialisation in terms of initial cost. """


def fitness(dataframe, n_clusters=3, seed=0):
    """ Cluster the data into `n_clusters` parts with each initialisation
    method. Return the difference between their initial costs so as to minimise
    that of Huang's method. """

    km_matching = KModes(
        n_clusters=n_clusters,
        init="matching",
        max_iter=-1,
        n_init=25,
        random_state=seed,
    ).fit(dataframe)
    km_huang = KModes(
        n_clusters=n_clusters,
        init="huang",
        max_iter=-1,
        n_init=25,
        random_state=seed,
    ).fit(dataframe)

    return km_huang.cost_ - km_matching.cost_  # EDO minimises by default
