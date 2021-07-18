import sys


N, M = map(int, input().split())
D = dict()
for i in range(N):
    stdin = sys.stdin.readline().rstrip()
    D[stdin] = str(i + 1)
    D[str(i + 1)] = stdin

for _ in range(M):
    stdin = sys.stdin.readline().rstrip()
    sys.stdout.write(D[stdin]+'\n')
