# @time: 2020/12/8 16:06
# @author: gzzang
# @file: mm.py
# @project: code_note

import torch

m = 2
n = 3
o = 4

u = torch.randn(size=(m, n))
print(u)
print(u.dtype)
print(u.shape)

v = torch.randn(size=(n, o))
print(v)
print(v.dtype)
print(v.shape)

w = torch.mm(u, v)
print(w)
print(w.dtype)
print(w.shape)
