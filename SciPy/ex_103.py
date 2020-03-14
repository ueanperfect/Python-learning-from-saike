"""
使用fmin()计算函数最小值。
"""
import scipy.optimize as opt
import numpy as np
import sys

points = []
def f(p):
	x, y = p
	z = (1-x)**2 + 100*(y-x**2)**2
	points.append((x,y,z))
	return z

def fprime(p):
    x, y = p
    dx = -2 + 2 * x - 400 * x * (y - x ** 2)
    dy = 200 * y - 200 * x ** 2
    return np.array([dx, dy])

init_point = (-2, -2)
try:
        method = sys.argv[1]
except:
        method ="fmin_bfgs"

fmin_func = opt.__dict__[method]
if method in ["fmin", "fmin_powell"]:
	result = fmin_func(f, init_point) #参数为目标函数和初始值
elif method in ["fmin_cg", "fmin_bfgs", "fmin_l_bfgs_b", "fmin_tnc"]:
	result = fmin_func(f, init_point, fprime) #参数为目标函数、初始值和导函数
elif method in ["fmin_cobyla"]:
	result = fmin_func(f, init_point, [])
else:
	print('fmin function not found')
	sys.exit(0)