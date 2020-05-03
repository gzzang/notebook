# @Time    : 2020/5/3 13:01
# @Author  : gzzang
# @File    : stats
# @Project : notebook

from scipy.stats import binom
import numpy as np

n = 10
x = np.arange(n+1)
p = 0.5

result = binom(n, p).pmf(x)

print(result)

