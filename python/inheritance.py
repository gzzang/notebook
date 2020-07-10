# @Time    : 2020/7/10 17:58
# @Author  : gzzang
# @File    : inheritance
# @Project : notebook


class A:
    def __init__(self):
        self.a = 1
        print(self.a)


class B(A):
    def __init__(self):
        super().__init__()
        self.a = 2
        print(self.a)


class C(B):
    def __init__(self):
        super().__init__()
        self.a = 3
        print(self.a)


foo = A()
print('-')
bar = B()
print('-')
baz = C()
print('-')
