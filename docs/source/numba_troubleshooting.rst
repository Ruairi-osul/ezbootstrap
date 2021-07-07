Numba Troubleshooting
==========================

ezbootstrap will attempt to speed up bootstrap replicate generation using numba's just in time compiler. If compilation fails, it will revert to pure python. This will be slower.

These steps can help increase the odds of numba compilation succeeding.

- Pass functions which contain onlt pure python or numpy functions.
- Pass functions which take only one or two input arguments. You can use lambda expressions or functools.partial for this.

