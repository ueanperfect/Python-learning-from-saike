from sympy import *
r = symbols( 'r', positive=True)
x = symbols( 'x')
circle_area = 2 * integrate(sqrt(r**2-x**2), (x, -r, r))
print(circle_area)
circle_area = circle_area.subs(r, sqrt(r**2-x**2))
print(circle_area)
V0 = integrate(circle_area, (x, -r, r))
print(V0)
V1 = V0.subs(r, pow(r**3-x**3,1/3))
print(V1)

# pi*r**2
# pi*(r**2 - x**2)
# 4*pi*r**3/3
# 4*pi*(r**3 - x**3)**1.0/3