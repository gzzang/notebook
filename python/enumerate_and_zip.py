# @Time    : 2020/4/19 22:28
# @Author  : gzzang
# @File    : enumerate_and_zip
# @Project : notebook

import numpy as np

number = 5
ar_foo = np.random.rand(number)
ar_bar = np.random.rand(number)
ar_baz = np.random.rand(number)

for i, (v_foo, v_bar, v_baz) in enumerate(zip(ar_foo, ar_bar, ar_baz)):
    print(f'{i}:{v_foo + v_bar + v_baz}')
