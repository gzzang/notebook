# @time: 2020/12/8 14:13
# @author: gzzang
# @file: multiply.py
# @project: code_note

import torch

m = 2
n = 3

u = torch.randn(m)
print(u)
print(u.dtype)
print(u.shape)

v = torch.randn(n)
print(v)
print(v.dtype)
print(v.shape)

x = torch.randn(m, n)

print(x)
print(x.dtype)
print(x.shape)

print(x * v)
print(v * x)

# 报错
# 原因：向量矩阵乘法，向量长度要和矩阵第二维长度相等
# print(x*u)
# print(u*x)
