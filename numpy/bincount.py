# @Time    : 2020/4/19 0:33
# @Author  : gzzang
# @File    : bincount
# @Project : notebook

import numpy as np

high = 10
size = 100
ar = np.random.randint(low=0, high=high, size=size)

ar_count = np.bincount(ar, minlength=high)
print(ar_count)
