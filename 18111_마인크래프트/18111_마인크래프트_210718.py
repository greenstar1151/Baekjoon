from math import inf
import sys


N, M, B = map(int, input().split())
stdin = sys.stdin.read().rstrip()
lands = stdin.split('\n')
lands = [list(map(int, l.split())) for l in lands]

cost_all = []
for height in range(257):
    cost_level = 0
    block_count = 0
    for l in lands:
        for block in l:
            blocks_req = height - block
            cost = blocks_req
            if cost < 0:
                cost *= -2
            cost_level += cost
            block_count += blocks_req
    if block_count > B:
        cost_level = inf
    cost_all.append((cost_level, height))


cost_all.sort(key=lambda x: (x[0], -x[1]))
print(f'{cost_all[0][0]} {cost_all[0][1]}')
