# @Time    : 2020/4/19 0:49
# @Author  : gzzang
# @File    : filter
# @Project : notebook

import numpy as np
import pandas as pd

np.random.seed(0)

df = pd.DataFrame(np.random.randint(low=0, high=10, size=[4, 6]))

print(df)
print(df[df[1] > 5][[0, 1]])
