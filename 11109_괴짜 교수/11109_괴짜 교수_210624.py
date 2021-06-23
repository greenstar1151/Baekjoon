import sys


T = int(input())
case_in = sys.stdin.read().rstrip()
cases = tuple(case_in.split('\n'))

for c in cases:
    d, n, s, p = map(int, c.split())
    if (d + n * p == n * s):
        print('does not matter')
    elif (d + n * p > n * s):
        print('do not parallelize')
    else:
        print('parallelize')
