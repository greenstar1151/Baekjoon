import sys


N, M = map(int, input().split())
stdin = sys.stdin.read().rstrip()
board = stdin.split('\n')
board = [[0 if x == 'B' else 1 for x in list(l)] for l in board]

kernel_B = [[(x + 8*i + i)%2 for x in range(8)] for i in range(8)]
kernel_W = [[(x + 8*i + i + 1)%2 for x in range(8)] for i in range(8)]

cost_list = []
for x in range(N - 8 + 1):
    for y in range(M - 8 + 1):
        cost = 0
        for i, l in enumerate(kernel_B):
            for j, e in enumerate(l):
                if e != board[x + i][y + j]:
                    cost += 1
        cost_list.append(cost)
        cost = 0
        for i, l in enumerate(kernel_W):
            for j, e in enumerate(l):
                if e != board[x + i][y + j]:
                    cost += 1
        cost_list.append(cost)

cost_list.sort()
print(cost_list[0])
