# @Time    : 2020/9/12 22:59
# @Author  : gzzang
# @File    : repeat
# @Project : notebook

import numpy as np

m = 3
n = 5

t = np.arange(m)

a = np.repeat(t, n)
b = np.tile(t, n)

print(a)
print(b)
