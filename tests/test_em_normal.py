"""End-to-end test: EM fitting of normal mixture based on demo_normal.py."""
import numpy as np
import pytest

import mixem
from mixem.distribution import NormalDistribution


def test_em_normal():
    np.random.seed(0)

    # True mixture: 30% N(μ=4, σ=1), 70% N(μ=1, σ=0.5)
    dist_params = [(4, 1), (1, 0.5)]
    true_weights = [0.3, 0.7]
    n_data = 5000
    data = np.concatenate([
        np.random.normal(loc=mu, scale=sigma, size=int(n_data * w))
        for (mu, sigma), w in zip(dist_params, true_weights)
    ])
    np.random.shuffle(data)

    weights, fitted, ll = mixem.em(
        data,
        [NormalDistribution(3.5, 1.0), NormalDistribution(1.5, 1.0)],
        progress_callback=None,
    )

    # Weights must sum to 1
    assert sum(weights) == pytest.approx(1.0, abs=1e-6)

    # Expected fitted parameters:
    # Component 0 (high-mean cluster): μ ≈ 4, σ ≈ 1, weight ≈ 0.3
    # Component 1 (low-mean cluster):  μ ≈ 1, σ ≈ 0.5, weight ≈ 0.7
    assert weights[0] == pytest.approx(0.3, abs=0.05)
    assert weights[1] == pytest.approx(0.7, abs=0.05)

    assert fitted[0].mu == pytest.approx(4.0, abs=0.2)
    assert fitted[0].sigma == pytest.approx(1.0, abs=0.1)

    assert fitted[1].mu == pytest.approx(1.0, abs=0.2)
    assert fitted[1].sigma == pytest.approx(0.5, abs=0.1)
