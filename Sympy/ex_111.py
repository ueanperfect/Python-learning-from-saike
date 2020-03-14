from sympy import *
x = Symbol("x", real=True)
tmp = series(exp(-I*x), x, 0, 10)
print(tmp)
print(im(tmp))     # 获得 tmp 的虚部
print(re(tmp))      # 获得 tmp 的实部
y1 = series(-sin(x), x, 0, 10)
print(y1)
y2 = series(cos(x), x, 0, 10)
print(y2)

# 1 - I*x - x**2/2 + I*x**3/6 + x**4/24 - I*x**5/120 - x**6/720 + I*x**7/5040 + x**8/40320 - I*x**9/362880 + O(x**10)
# -x**9/362880 + x**7/5040 - x**5/120 + x**3/6 - x + im(O(x**10))
# x**8/40320 - x**6/720 + x**4/24 - x**2/2 + re(O(x**10)) + 1
# -x + x**3/6 - x**5/120 + x**7/5040 - x**9/362880 + O(x**10)
# 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 + O(x**10)

from sympy import *
x = Symbol("x", real=True)
tmp = series((exp(I*x)+exp(-I*x))/2, x, 0, 10)
print(tmp)
print(im(tmp))     # 获得 tmp 的虚部
print(re(tmp))      # 获得 tmp 的实部
#y1 = series(-sin(x), x, 0, 10)
#print(y1)
y2 = series(cos(x), x, 0, 10)
print(y2)

# 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 + O(x**10)
# im(O(x**10))
# x**8/40320 - x**6/720 + x**4/24 - x**2/2 + re(O(x**10)) + 1
# 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 + O(x**10)

from sympy import *
x = Symbol("x", real=True)
tmp = series((exp(I*x)-exp(-I*x))/2/I, x, 0, 10)
print(tmp)
print(im(tmp))     # 获得 tmp 的虚部
print(re(tmp))      # 获得 tmp 的实部
y1 = series(sin(x), x, 0, 10)
print(y1)
#y2 = series(cos(x), x, 0, 10)
#print(y2)

# x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)
# im(O(x**10))
# x**9/362880 - x**7/5040 + x**5/120 - x**3/6 + x + re(O(x**10))
# x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)