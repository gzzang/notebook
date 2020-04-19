# @Time    : 2020/3/25 16:45
# @Author  : gzzang
# @File    : indefinite_integral
# @Project : notebook

import sympy as mp

x = mp.Symbol('x')

expression = mp.sqrt(1 + x * x)
integrate_expression = mp.integrate(expression, x)
another_integrate_expression = x * mp.sqrt(x*x + 1)/2 + mp.log(x + mp.sqrt(1 + x * x)) / 2

print('Expressions.')
print(expression)

print('Expressions after integrate are different.')
print(integrate_expression)
print(another_integrate_expression)

print('Values are same. (x==3)')
print(integrate_expression.evalf(subs={x: 3}))
print(another_integrate_expression.evalf(subs={x: 3}))
