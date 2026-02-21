# mix'EM

mixem is a pure-python implementation of the Expectation-Maximization (EM) algorithm for fitting mixtures of probability distributions. It requires Python 3.12+ and uses few dependencies (only NumPy and SciPy).

![Old Faithful example](http://i.imgur.com/kJgsHMG.png)

## Features

* Easy-to-use and fully-documented API
* Built-in support for several probability distributions
* Easily define custom probability distributions by implementing their probability density function and weighted log-likelihood

## Documentation

Find the mix'EM documentation on [ReadTheDocs](https://mixem.readthedocs.org/en/latest/).

## Installation

Using uv (recommended):

```bash
uv add mixem
```

Using pip:

```bash
pip install mixem
```

Install directly from GitHub (latest development version):

```bash
uv add git+https://github.com/SamBryce-Smith/mixem

pip install git+https://github.com/SamBryce-Smith/mixem
```

## Development

Clone the repository and install with development dependencies using uv:

```bash
git clone https://github.com/SamBryce-Smith/mixem
cd mixem
uv sync --dev
```

Run the tests:

```bash
uv run pytest
```

Check and fix linting with ruff:

```bash
uv run ruff check mixem/
uv run ruff check --fix mixem/
```
