import math
from decimal import *


precision = 100 # Global precision def
getcontext().prec = precision

# pi, cos, sin code from https://docs.python.org/3/library/decimal.html#recipes

def pi():
    getcontext().prec += 2
    three = Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

def cos(x):
    x = x % (2 * pi())
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def sin(x):
    x = x % (2 * pi())
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def newton(x, A, B, C):
    return (x - 
            (A*x + B*sin(x) - Decimal(str(C)))
            / 
            (Decimal(str(A)) + B*cos(x))  # 문제 조건에서 0이 나오지 않도록 보장
            )


A, B, C = map(int, input().split())


x_n = Decimal('0')
while True:
    x = newton(x_n, A, B, C)
    if math.isclose(x, x_n, rel_tol=1e-100, abs_tol=0.0):
        break
    else:
        x_n = x


print(round(x, 12))
