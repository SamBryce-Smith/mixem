# mix'EM

mixem is a pure-python implementation of the Expectation-Maximization (EM) algorithm for fitting mixtures of probability distributions. It requires Python 3.12+ and uses few dependencies (only NumPy and SciPy).

![Old Faithful example](http://i.imgur.com/kJgsHMG.png)

## Features

* Easy-to-use and fully-documented API
* Built-in support for several probability distributions
* Easily define custom probability distributions by implementing their probability density function and weighted log-likelihood

## Documentation

Find the original package mix'EM documentation on [ReadTheDocs](https://mixem.readthedocs.org/en/latest/). Documentation specific to this fork will be published to a separate link at a later date

Changes between releases are described in [CHANGELOG.md](CHANGELOG.md)

## Installation

Install this forked version of mixem directly from GitHub (latest development version):

```bash
# recommended
uv add git+https://github.com/SamBryce-Smith/mixem

pip install git+https://github.com/SamBryce-Smith/mixem

# installing a specific version based on git commit tag (e.g. v0.2.0):
uv add git+https://github.com/SamBryce-Smith/mixem@v0.2.0
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
