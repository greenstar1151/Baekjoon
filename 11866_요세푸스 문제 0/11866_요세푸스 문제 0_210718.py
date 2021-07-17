from collections import deque
import sys


N, K = map(int, input().split())


output = []
circle = deque(range(1, N+1))

idx = K - 1
while len(circle) > 0:
    output.append(f'{circle[idx]}')
    del circle[idx]
    idx += K - 1
    idx %= max(len(circle), 1)

sys.stdout.write('<' + ', '.join(output) + '>')
