import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol('x')

a1 = 1.5522
#   b = 3.0668
b1 = 0
c1 = 0
d1 = 0
#  c = -29.0177
#   d = 32.8239
e1 = -61.3827
#диапазон
n = 5
#точность
dl = 0.000005

f = a1*x ** 4 + b1*x ** 3 + c1*x ** 2 + d1*x + e1

a = -1.5
b = -1.0

eps = 0.00001
x0 = (a + b) / 2
x1 = x0 + 2 * eps

d = sp.diff(f)
while(np.abs((x1 - x0)) > eps):
    x0 = x1
    x1 = x0 - f.subs(x, x0)/d.subs(x, x0)
x1