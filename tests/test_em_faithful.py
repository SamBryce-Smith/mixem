"""End-to-end test: EM fitting of bivariate Gaussian mixture to Old Faithful data."""
from pathlib import Path

import numpy as np
import pytest

import mixem
from mixem.distribution import MultivariateNormalDistribution

FAITHFUL_CSV = Path(__file__).parent.parent / "examples" / "faithful.csv"


def test_em_multinormal_faithful():
    # Load data with numpy (skip header row — columns: eruptions, waiting)
    data = np.genfromtxt(FAITHFUL_CSV, delimiter=",", skip_header=1)

    init_params = [
        (np.array([2.0, 50.0]), np.identity(2)),
        (np.array([4.0, 80.0]), np.identity(2)),
    ]
    distributions = [
        MultivariateNormalDistribution(mu, sigma) for mu, sigma in init_params
    ]

    weights, fitted, ll = mixem.em(
        data,
        distributions,
        initial_weights=[0.3, 0.7],
        progress_callback=None,  # suppress output during tests
    )

    # Weights must sum to 1
    assert sum(weights) == pytest.approx(1.0, abs=1e-6)

    # Expected fitted parameters for the Old Faithful dataset:
    # Component 0 (short eruptions): μ ≈ [2.04, 54.5], weight ≈ 0.36
    # Component 1 (long eruptions):  μ ≈ [4.29, 79.9], weight ≈ 0.64
    assert weights[0] == pytest.approx(0.36, abs=0.05)
    assert weights[1] == pytest.approx(0.64, abs=0.05)

    assert list(fitted[0].mu) == pytest.approx([2.04, 54.5], abs=0.5)
    assert list(fitted[1].mu) == pytest.approx([4.29, 79.9], abs=0.5)
