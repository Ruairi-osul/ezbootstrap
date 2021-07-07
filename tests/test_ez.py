import numpy as np
import ezbootstrap as ez

np.random.seed(1)


def test_1sample():
    expected = 50
    x = np.random.randn(1000) + expected
    reps = ez.bs_1sample(x, func=lambda x: np.mean(x), size=1000)
    observed = np.mean(reps)
    res = abs(expected - observed) < 0.1
    assert res


def test_2sample():
    expected = 4
    x = np.random.randn(5000)
    y = np.random.randn(5000) + expected
    reps = ez.bs_2sample(x, y, size=1000, func=lambda x, y: np.mean(y) - np.mean(x),)
    observed = np.mean(reps)
    res = abs(expected - observed) < 0.1
    assert res


def test_pairs():
    x = np.random.randn(5000) + 40
    expected = 3
    y = (x + (np.random.randn(5000) * 2)) * expected
    reps = ez.bs_pairs(x, y, size=1000, func=lambda x, y: np.polyfit(x, y, deg=1)[1])
    observed = np.mean(reps)
    assert (expected - observed) < 0.1

