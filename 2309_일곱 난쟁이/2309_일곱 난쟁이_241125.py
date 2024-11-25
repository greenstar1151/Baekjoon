import sys

from itertools import permutations

data = list(map(int, sys.stdin.read().rstrip().split("\n")))
data.sort()

for c in permutations(data, 7):
    if sum(c) == 100:
        print("\n".join(map(str, c)))
        break
