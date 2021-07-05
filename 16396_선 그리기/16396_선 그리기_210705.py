import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
cases = stdin.split('\n')

coords_line = [0 for _ in range(10000)]

for l in cases:
    x, y = map(int, l.split())
    for i in range(x-1, y-1):
        coords_line[i] = 1

print(sum(coords_line))
