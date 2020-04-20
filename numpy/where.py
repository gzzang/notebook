# @Time    : 2020/4/20 22:59
# @Author  : gzzang
# @File    : where
# @Project : notebook

import numpy as np

x = np.arange(10)
a = np.where(np.logical_or(x < 1, x > 5))
print(a)
print(type(a))

print(a[0])
print(type(a[0]))
