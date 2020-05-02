# @Time    : 2020/5/2 20:58
# @Author  : gzzang
# @File    : kron
# @Project : notebook

import numpy as np

n = 3
m = 5

a = np.kron(np.eye(n), np.ones((1, m)))
b = np.tile(np.eye(n), (1, m))
c = a.flatten()

print(a)
print(b)
print(c)