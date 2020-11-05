import math


X = int(input()) - 1
line = math.floor((-1 + math.sqrt(1 + 8 * X)) / 2)

if line % 2 == 0:
    pos = X - (line * (line + 1) / 2) + 1
    print(f'{int(line + 2 - pos)}/{int(pos)}')
else:
    pos = X - (line * (line + 1) / 2) + 1
    print(f'{int(pos)}/{int(line + 2 - pos)}')
