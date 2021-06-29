from functools import cache
from math import sqrt, floor, log, sin
import sys

sys.setrecursionlimit(12800)

@cache
def x(i):
    if i <= 0:
        return 1
    return x(floor(i - sqrt(i))) + x(floor(log(i))) + x(floor(i * (sin(i) ** 2)))

x(100000)
x(500000)
x(1000000)
for line in open(0).readlines():
    line = line.rstrip() 
    if line == '-1':
        break
    print(x(int(line)) % 1000000)
