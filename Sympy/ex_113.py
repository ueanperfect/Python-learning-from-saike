from sympy import *
x, y, z = symbols("x,y,z")
m = Add(Mul(x, y, z), atan(y)*Pow(x, y), x*cos(z))
print(m)
# x*y*z + x*cos(z) + x**y*atan(y)

from sympy import *
x, y, z= symbols("x,y,z")
m = Add(x, Mul(-1, y), sin(x)*Mul(z,1/y) )
print(m)
# x - y + z*sin(x)/y