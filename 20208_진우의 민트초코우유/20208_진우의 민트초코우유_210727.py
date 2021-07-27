from itertools import permutations
import sys


def dist_L1(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


N, M, H = map(int, input().split())
village = []
home_pos = None
milk_pos = []
for i in range(N):
    stdin_str = sys.stdin.readline()
    for j, m in enumerate(stdin_str.split()):
        if m == '0':
            continue
        elif m == '1':
            home_pos = (i, j)
        elif m == '2':
            milk_pos.append((i, j))

counter = set()
for path in permutations(milk_pos, len(milk_pos)):
    hp = M
    step_prev = home_pos
    for i, step in enumerate(path):
        d = dist_L1(step_prev, step)
        if d > hp:
            break
        else:
            hp += H - d
            if dist_L1(step, home_pos) <= hp:
                counter.add(i+1)
        step_prev = step

counter = list(counter)
counter.sort(reverse=True)
if len(counter) == 0:
    print(0)
else:
    print(counter[0])
