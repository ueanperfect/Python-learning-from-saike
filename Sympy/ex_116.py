from sympy import *
x = symbols("x")
m = diff(3*sin(2*x)+2*cos(2*x), x, 10)
print(m)
# -1024*(3*sin(2*x) + 2*cos(2*x))

from sympy import *
x , y= symbols("x, y")
m1 = diff(y*sin(3*x) - exp(x)*y*cos(5*y), x, 10)
m2 = diff(y*sin(3*x) - exp(x)*y*cos(5*y), y, 8)
print(m1)
print(m2)