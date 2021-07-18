from functools import cache
import sys


@cache
def fibcount(n):
    if n == 0:
        return 1, 0
    if n == 1:
        return 0, 1
    return fibcount(n-2)[0] + fibcount(n-1)[0], fibcount(n-2)[1] + fibcount(n-1)[1]

T = int(input())
for i in range(T):
    stdin = sys.stdin.readline().rstrip()
    zero, one = fibcount(int(stdin))
    sys.stdout.write(f'{zero} {one}\n')
