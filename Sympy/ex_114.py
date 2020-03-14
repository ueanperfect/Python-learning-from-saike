from sympy import *
x = symbols("x")
m = simplify((x+2020)**2 - (x+2025)**2)
print(m)

from sympy import *
x = symbols("x")
m = radsimp(2/(sqrt(5)+1))
print(m)
# (-1 + sqrt(5))/2

from sympy import *
x , y= symbols("x, y")
m = ratsimp (x/(y+2021)-y/(x-2024))
print(m)

from sympy import *
x , y= symbols("x, y")
m = fraction( ratsimp (x/(x-2024)-y/(y-2026)))
print(m)

from sympy import *
x , y= symbols("x, y")
f = Function("f")
m = cancel((f(x,y)**3-1)/(f(x,y)-1))
print(m)
# f(x, y)**2 + f(x, y) + 1

from sympy import *
x , y= symbols("x, y")
f = Function("f")
m = trigsimp(f(sin(x)**2+cos(x)**2-cos(y)**2))
print(m)
# f(sin(y)**2)

from sympy import *
x , y= symbols("x, y")
m = expand((x-y)**5)
print(m)
# x**5 - 5*x**4*y + 10*x**3*y**2 - 10*x**2*y**3 + 5*x*y**4 - y**5

from sympy import *
x , y= symbols("x, y")
m = factor(2*x**2+2*y-2*x-2*x*y)
print(m)
# 2*(x - 1)*(x - y)

from sympy import *
x , y, a , b = symbols("x, y, a, b")
n =  expand((y-a*x)**2 - (x-b*y)**3)
m1 = collect(n, x)
m2 = collect(n, y)
print(m1)
print(m2)
# b**3*y**3 - x**3 + x**2*(a**2 + 3*b*y) + x*(-2*a*y - 3*b**2*y**2) + y**2
# a**2*x**2 + b**3*y**3 - x**3 + y**2*(-3*b**2*x + 1) + y*(-2*a*x + 3*b*x**2)