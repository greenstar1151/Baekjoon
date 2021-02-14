import math
import sys

T = int(input())
case_in = sys.stdin.read().rstrip()
cases = tuple(case_in.split('\n'))

for case in cases:
    H, W, N = map(int, case.split())
    floor = H if N % H == 0 else N % H
    print(f'{floor}{(math.ceil(N / H)):0>2}')
