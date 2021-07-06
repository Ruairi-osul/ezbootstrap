import numba
import warnings
import numpy as np
from numba import TypingError
from typing import Callable, overload, Any


@overload
def _jitted_func_factory(
    func: Callable[[np.ndarray, np.ndarray], Any]
) -> Callable[[np.ndarray, np.ndarray], Any]:
    ...


@overload
def _jitted_func_factory(
    func: Callable[[np.ndarray], Any]
) -> Callable[[np.ndarray], Any]:
    ...


def _jitted_func_factory(func):
    return numba.njit()(func)


def _bs_draw_apply_1sample(
    x: np.ndarray, f: Callable[[np.ndarray], Any], size: int
) -> np.ndarray:
    reps = np.empty(size)
    for i in range(size):
        xs = np.random.choice(x, replace=True, size=size)
        reps[i] = f(xs)
    return reps


def _bs_draw_apply_2sample(
    x: np.ndarray, y: np.ndarray, f: Callable[[np.ndarray, np.ndarray], Any], size: int
) -> np.ndarray:
    reps = np.empty(size)
    for i in range(size):
        xs = np.random.choice(x, replace=True, size=size)
        ys = np.random.choice(y, replace=True, size=size)
        reps[i] = f(xs, ys)
    return reps


def _permutation_draw_apply_2sample(
    x: np.ndarray, y: np.ndarray, f: Callable[[np.ndarray, np.ndarray], Any], size: int
) -> np.ndarray:
    reps = np.empty(size)
    idx = len(x)
    con = np.concatenate((x, y))
    for i in range(size):
        perm = np.random.permutation(con)
        xs = perm[:idx]
        ys = perm[idx:]
        reps[i] = f(xs, ys)
    return reps


def _bs_pairs_draw_apply(
    x: np.ndarray, y: np.ndarray, f: Callable[[np.ndarray, np.ndarray], Any], size: int
) -> np.ndarray:

    reps = np.empty(size)
    idx = np.arange(len(x))
    for i in range(size):
        idxs = np.random.choice(idx, replace=True, size=len(x))
        xs = x[idxs]
        ys = y[idxs]
        reps[i] = f(xs, ys)
    return reps


def bs_1sample(
    x: np.ndarray, func: Callable[[np.ndarray], Any], size: int = 5000
) -> int:
    """
    One sample bootsrap replicates.

    Args:
        x (arraylike): The sample from which replicates will be drawn
        func (callable[[np.ndarray], float]): The function that returns the statistic to be calculated on x.
        size (int): The number of bootstrap replicates to generate
    Returns:
        A numpy array of bootstrap replicates
    """
    try:
        jfunc = _jitted_func_factory(func)
        reps = numba.njit()(_bs_draw_apply_1sample)(x, jfunc, size=size)
    except TypingError:
        warnings.warn("Numba compilation failed. Reverting to pure python")
        reps = _bs_draw_apply_1sample(x, func, size=size)
    return reps


def bs_2sample(
    x: np.ndarray,
    y: np.ndarray,
    func: Callable[[np.ndarray, np.ndarray], Any],
    size: int = 5000,
) -> np.ndarray:
    """
    Two sample bootsrap replicates.

    Args:
        x (arraylike): The first sample from which replicates will be drawn
        y (arraylike): The second sample from which replicates will be drawn
        func (callable[[np.ndarray, np.ndarray], float]): The function that returns the statistic to be calculated on x and y. 
        size (int): The number of bootstrap replicates to generate
    Returns:
        A numpy array of bootstrap replicates
    """
    try:
        jfunc = _jitted_func_factory(func)
        reps = numba.njit()(_bs_draw_apply_2sample)(x, y, jfunc, size=size)
    except TypingError:
        warnings.warn("Numba compilation failed. Reverting to pure python")
        reps = _bs_draw_apply_2sample(x, y, func, size=size)
    return reps


def bs_pairs(
    x: np.ndarray,
    y: np.ndarray,
    func: Callable[[np.ndarray, np.ndarray], Any],
    size: int = 5000,
) -> np.ndarray:
    """
    Generate bootstrap replicates from pairs of x and y.

    Args:
        x (arraylike): The first variable from which replicates will be drawn
        y (arraylike): The second variable from which replicates will be drawn
        func (callable[[np.ndarray, np.ndarray], float]): The function that returns the statistic to be calculated on x and y.
        size (int): The number of bootstrap replicates to generate
    Returns:
        A numpy array of bootstrap replicates
    """
    try:
        jfunc = _jitted_func_factory(func)
        reps = numba.njit()(_bs_pairs_draw_apply)(x, y, jfunc, size)
    except TypingError:
        warnings.warn("Numba compilation failed. Reverting to pure python")
        reps = _bs_draw_apply_2sample(x, y, func, size=size)
    return reps


def permutation_2sample(
    x: np.ndarray,
    y: np.ndarray,
    func: Callable[[np.ndarray, np.ndarray], Any],
    size: int = 5000,
) -> np.ndarray:
    """
    Generate permutation replicates from two samples.

    Args:
        x (arraylike): The first sample from which replicates will be drawn
        y (arraylike): The second sample from which replicates will be drawn
        func (callable[[np.ndarray, np.ndarray], float]): The function that returns the statistic to be calculated on x and y.
        size (int): The number of permutation replicates to generate
    Returns:
        A numpy array of bootstrap replicates
    """
    try:
        jfunc = _jitted_func_factory(func)
        reps = numba.njit()(_permutation_draw_apply_2sample)(x, y, jfunc, size)
    except TypingError:
        warnings.warn("Numba compilation failed. Reverting to pure python")
        reps = _permutation_draw_apply_2sample(x, y, func, size)
    return reps
