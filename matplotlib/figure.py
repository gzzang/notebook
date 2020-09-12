# @time: 2020/9/12 16:55
# @author: gzzang
# @file: figure.py
# @project: notebook

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
n = 8

fig, ax = plt.subplots()
plt.plot(np.random.rand(8), label='a')
plt.plot(np.random.rand(8), label='b')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0, n])
plt.ylim([0, 1])
plt.xticks([0, n])
plt.yticks([0, 1])
plt.show()
