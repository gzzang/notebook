# @time: 2020/11/16 16:46
# @author: gzzang
# @file: apply.py
# @project: notebook

import pandas as pd
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.randint(low=0, high=10, size=[4, 6]))

df[0].apply(lambda x: 11 if x == 5 else 0)

print(df)
