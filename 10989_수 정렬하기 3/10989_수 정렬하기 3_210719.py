import sys


N = int(sys.stdin.readline())
counter = [0] * 10000
for _ in range(N):
    counter[int(sys.stdin.readline()) - 1] += 1

for i in range(10000):
    if counter[i] != 0:
        for _ in range(counter[i]):
            sys.stdout.write(f'{i+1}\n')
