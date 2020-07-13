Quickstart
===============

ezbootstrap generates bootstrap replicates from arbitrary functions. Functions are passed as lambda functions.

One Sample Bootstrap Replicates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    from ezbootstrap import bs_1sample
    import numpy as np
    import scipy.stats

    data = scipy.stats.norm(loc=100, scale=10).rvs(50)
    reps = bs_1sample(
        x=data,
        func=lambda x: np.mean(x)
    )
    confint = np.percentile(reps, [0.025, 0.975])
    print(f"Confidence interval for the mean of x: {confint}")


Bootstrap Pairs Replicates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    from ezbootstrap import bs_pairs
    import scipy.stats


    x = scipy.stats.norm(loc=100, scale=20).rvs(100)
    y = scipy.stats.norm(loc=50, scale=10).rvs(100)
    observed = scipy.stats.pearsonr(s)

    reps = bs_pairs(
        x=x,
        y=y,
        func=lambda x, y: scipy.stats.pearsonr(x, y)
    )


Permutation Replicates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    from ezbootstrap import permutation_2sample

    x = scipy.stats.norm(loc=100, scale=10).rvs(100)
    y = scipy.stats.norm(loc=90, scale=10).rvs(100)

    reps = permutation_2sample(
        x=x,
        y=y,
        func=lambda x, y: np.mean(x) - np.mean(y)
    )


Function arguments
======================

Function arguments can be specified in the definition of the lambda function.

::

    import numpy as np 
    import scipy.stats
    from ezbootstrap import bs_1sample

    x = scipy.stats.norm(loc=100, scale=20).rvs(100)
    reps = bs_1sample(
        x=x,
        func=lambda x: np.var(x, ddof=1)
    )

