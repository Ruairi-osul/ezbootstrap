# Ez Bootstrap

Ez bootstrap is a python package for performing bootstrap statistics. Read more on the [docs.](https://ezbootstrap.readthedocs.io/en/latest/)

## Installation

It can be installed using `pip` in a terminal or command prompt. 
```
$ pip install ezbootstrap
```

## Usage

Functions in `ezbootstrap` generate bootstrap replicates from arbitrary input functions.

### Generate bootstrap condidence intervals

```
from ezbootstrap import bs_1sample
import numpy as np
import scipy.stats

data = scipy.stats.norm(loc=100, scale=10).rvs(50)
reps = bs_1sample(
    x=data,
    func=lambda x: np.mean(x),
    size=10000
)
confint = np.percentile(reps, [0.025, 0.975])
print(f"Confidence interval for the mean of x: {confint}")
```

### Perform permutation tests for difference of mean

```
from ezbootstrap import permutation_2sample

x = scipy.stats.norm(loc=100, scale=10).rvs(100)
y = scipy.stats.norm(loc=90, scale=10).rvs(100)

observed = np.mean(x) - np.mean(y)
reps = permutation_2sample(
    x=x,
    y=y,
    func=lambda x, y: np.mean(x) - np.mean(y),
    size=5000
)
p = np.mean(np.abs(reps) >= np.abs(observed)) * 2
```

### Perform Hypothesis tests between two samples with arbitrary functions 

```
from ezbootstrap import bs_2sample
from sklearn.metrics import jaccard_score

x = np.random.choice([0, 1], 1000)
y = np.random.choice([0, 1], 1000)

observed = jaccard_score(x, y)
reps = bs_2sample(
    x=x,
    y=y,
    func=lambda x, y: jaccard_score(x, y),
    size=5000
)
p = np.mean(reps >= observed)
```


## Performance

`ezbootstrap` uses [`numba's`](https://github.com/numba/numba) just-in-time compiler to speed up bootstrap replicate generation. If compilation fails, it will revert to python which will be slower.

To increase odds of numba compilation succeeding, pass functions written in pure python or only using `numpy` functions.

## Acknowledgement

Justin Bois's [`dc_stat_think`](https://github.com/justinbois/dc_stat_think) was the inspiration for this package. `ezbootstrap` extends `dc_stat_think` by permitting users to generate bootstrap replicates with arbitrary functions.
