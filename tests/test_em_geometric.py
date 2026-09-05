"""End-to-end test: EM fitting of geometric mixture based on demo_geometric.py."""
import numpy as np
import pytest

import mixem
from mixem.distribution import GeometricDistribution


def test_em_geometric():
    np.random.seed(0)

    # True mixture: 40% Geom(p=0.1), 60% Geom(p=0.3)
    dist_params = [0.1, 0.3]
    true_weights = [0.4, 0.6]
    n_data = 10000
    data = np.concatenate([
        np.random.geometric(p=p, size=int(n_data * w))
        for p, w in zip(dist_params, true_weights)
    ])
    np.random.shuffle(data)

    weights, fitted, ll = mixem.em(
        data,
        [GeometricDistribution(0.8), GeometricDistribution(0.1)],
        progress_callback=None,
    )

    # Weights must sum to 1
    assert sum(weights) == pytest.approx(1.0, abs=1e-6)

    # Neither component should collapse to zero
    assert all(w > 0.1 for w in weights)

    # Sort components by p to handle potential ordering swap
    order = np.argsort([d.p for d in fitted])

    # Expected fitted parameters:
    # Lower-p component: p ≈ 0.1
    # Higher-p component: p ≈ 0.3
    # Note: Geom(0.1) and Geom(0.3) overlap substantially, so EM may settle
    # in a local optimum; verify components are in the right broad range.
    assert fitted[order[0]].p == pytest.approx(0.1, abs=0.05)
    assert 0.2 <= fitted[order[1]].p <= 0.6
