# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-02-21

Modernised development and installation infrastructure, dropping support for
Python < 3.12 and raising minimum dependency versions accordingly.

### Breaking Changes

- Dropped support for Python 2.7 and Python < 3.12 (`requires-python = ">=3.12"`)
- Raised minimum NumPy version from `1.7.0` to `1.26.0`
- Raised minimum SciPy version from `0.14.0` to `1.11.0`

### Added

- `pyproject.toml` replacing `setup.py` as the single source of packaging
  metadata and build configuration (PEP 517/518, hatchling build backend)
- `uv` as the recommended package manager for both end-users and developers
- `pytest>=8.0` and `ruff>=0.8` as development dependencies via
  `[dependency-groups]`
- End-to-end tests fitting mixture models to synthetic and real data using
  `pytest.approx`: a bivariate Gaussian mixture on the Old Faithful dataset
  (`tests/test_em_faithful.py`) and individual distribution tests for the
  exponential, geometric, and normal distributions
  (`tests/test_em_exponential.py`, `tests/test_em_geometric.py`,
  `tests/test_em_normal.py`)

### Changed

- `README.rst` converted to `README.md` (GitHub Flavoured Markdown) and
  expanded with a Development section documenting `uv`-based workflows

### Removed

- `setup.py`

---

## [0.1.3] - (previous release)

Last release supporting Python 2.7 and Python 3.5+.
