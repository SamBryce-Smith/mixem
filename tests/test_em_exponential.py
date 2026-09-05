"""End-to-end test: EM fitting of exponential mixture based on demo_exponential.py."""
import numpy as np
import pytest

import mixem
from mixem.distribution import ExponentialDistribution


def test_em_exponential():
    np.random.seed(0)

    # True mixture: 40% Exp(λ=1), 60% Exp(λ=10)
    dist_params = [1, 10]
    true_weights = [0.4, 0.6]
    n_data = 10000
    data = np.concatenate([
        np.random.exponential(scale=1.0 / lmbda, size=int(n_data * w))
        for lmbda, w in zip(dist_params, true_weights)
    ])
    np.random.shuffle(data)

    weights, fitted, ll = mixem.em(
        data,
        [ExponentialDistribution(0.5), ExponentialDistribution(5.0)],
        progress_callback=None,
    )

    # Weights must sum to 1
    assert sum(weights) == pytest.approx(1.0, abs=1e-6)

    # Expected fitted parameters:
    # Component 0 (slow decay): λ ≈ 1, weight ≈ 0.4
    # Component 1 (fast decay): λ ≈ 10, weight ≈ 0.6
    assert weights[0] == pytest.approx(0.4, abs=0.05)
    assert weights[1] == pytest.approx(0.6, abs=0.05)

    assert fitted[0].lmbda == pytest.approx(1.0, abs=0.5)
    assert fitted[1].lmbda == pytest.approx(10.0, abs=1.0)
