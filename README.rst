mix'EM 
======


mixem is a pure-python implementation of the Expectation-Maximization (EM) algorithm for fitting mixtures of probability distributions. It requires Python 3.12+ and uses few dependencies (only NumPy and SciPy).


.. image:: http://i.imgur.com/kJgsHMG.png
   :scale: 50 %
   :alt: Old Faithful example
   :align: left


Features
--------

* Easy-to-use and fully-documented API
* Built-in support for several probability distributions
* Easily define custom probability distributions by implementing their probability density function and weighted log-likelihood

Documentation
-------------
Find the mix'EM documentation on `ReadTheDocs <https://mixem.readthedocs.org/en/latest/>`_.


Installation
------------

Using uv (recommended)::

    uv add mixem

Using pip::

    pip install mixem

Install directly from GitHub (latest development version)::

    uv add git+https://github.com/SamBryce-Smith/mixem

    pip install git+https://github.com/SamBryce-Smith/mixem

Development setup::

    git clone https://github.com/SamBryce-Smith/mixem
    cd mixem
    uv sync --dev
