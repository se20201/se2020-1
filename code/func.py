from math import fabs
from math import pi

#弧度角度转换函数
def radian2angle(x):
    return 180*x/(pi)

def angle2radian(x):
    return x*(pi)/180

#三角函数计算函数
def sin(x):
    g = 0
    t = x
    n = 1
    while (fabs(t) >= 1e-10):
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n - 2)
    return g

def cos(x):
    x = 1.57079 - x
    return sin(x)

def tan(x):
    return sin(x)/cos(x)

def cot(x):
    return cos(x)/sin(x)










