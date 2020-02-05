Source code, notebooks, and data
================================

This directory contains all of the source code, notebooks and data needed to
reproduce the results and plots in the paper "A novel initialisation based on
hospital-resident assignment for the $k$-modes algorithm" by Henry Wilde et al.

At the top level of this directory is an ``environment.yml`` file used to create
a virtual ``conda`` environment. This environment will ensure that the code
herein will reproduce the data and plots used in the paper exactly. Instructions
on how to create, use and otherwise manage ``conda`` environments can be found
[here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

The remainder of the directory is made up of three ZIP archives that should be
decompressed: ``data.zip``, ``nbs.zip``, and ``src.zip``.


The data
--------

The ``data`` subdirectory contains the data associated with each subsection
in the results of the paper. The ``data/knee`` and ``data/nclasses``
subdirectories contain the results for the benchmark datasets stored at the top
of ``data`` where the number of clusters has been chosen via knee point
detection and number of classes respectively. The ``data/artificial`` contains
two subdirectories -- one for each experiment in the final analysis. Each
experiment directory contains three trial subdirectories that are structured as
follows:

- ``data.tar.gz``: a tarball of all the data associated with that experiment.
- ``summary``: a directory containing a summary of the data in ``data.tar.gz``,
  i.e.:
    - ``main.csv``: a CSV detailing the index, dimensions, memory consumption,
      generation and fitness of every individual in the trial.
    - ``max``: a directory containing the dataset and metadata of the individual
      with the highest fitness score in the trial.
    - ``median``: a directory containing the dataset and metadata of the
      individual with the closest-to-median fitness score in the trial.
    - ``min``: a directory containing the dataset and metadata of the individual
      with the lowest fitness score in the trial.

In addition to this, each experiment directory contains a ``top`` directory
which describes the top-performing percentile of datasets across all trials.
Specifically, ``top/main.csv`` contains a subset of all the ``summary/main.csv``
files corresponding to the top percentile, and the remainder of the directory is
a copy of the datasets in the top percentile in their original
``<seed>/<generation>/<index>/main.csv`` structure.


The notebooks
-------------

The ``nbs`` subdirectory contains the Jupyter Notebooks used to produce the
data, tables and plots in the results section of the paper. Each notebook has
some brief documentation within.

It may be helpful to add the ``conda`` environment as a kernel to Jupyter. To do
this, run the following command once it is installed:
``python - ipykernel install --user --name kmodes-init --display-name "k-modes (Wilde)"``.


The source code
---------------

The ``src`` subdirectory contains the source code used to produce the data in
``data/artificial``. The only object in ``src`` is the ``artificial`` directory.
Within that, there are three files: two experiment files that define a
``fitness`` function, and ``main.py``. To reproduce the associated data, use the
following command: ``python main.py <experiment> <cores> 500 100 0.2 0.01 3``
where ``<experiment>`` is the experiment file's name (without the ``.py``
extension) and ``cores`` is the number of cores to use.

Note that the generation of this data is costly and will likely require a
machine that is capable of running undisturbed for a number of days or even
weeks.

Once the data has been generated, it can be easily summarised using the
``edo_exp`` library that can be found at
[github.com/daffidwilde/edo_exp](https://github.com/daffidwilde/edo_exp). To
summarise an experiment whose data is stored at ``<path/to/experiment/data>``,
do the following:

1. Clone the repository: ``git clone https://github.com/daffidwilde/edo_exp``
2. Move to its source code directory: ``cd edo_exp/src/edo_exp``
3. Run the command: ``python summarise.py <path/to/experiment/data>``.

Again, this may some time to complete.
