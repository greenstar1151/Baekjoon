import sys


stdin = sys.stdin.read().rstrip()
cases = stdin.split('\n')

cases.pop()
for ca in cases:
    a, b, c = sorted(map(int, ca.split()))
    if (a**2 + b**2 == c**2):
        print('right')
    else:
        print('wrong')
