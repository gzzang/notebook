# @Time    : 2020/7/13 18:17
# @Author  : gzzang
# @File    : lru_cache
# @Project : notebook

from functools import lru_cache


@lru_cache()
def func(x):
    print(f'calculate {x}.')
    return 2 * x


print(func(1))
print(func(1))
print(func(2))
print(func(3))
print(func(2))
