import sys


N = int(input())
S = set()
for _ in range(N):
    stdin = sys.stdin.readline().rstrip()
    query, *n = stdin.split()
    if query == 'add':
        S.add(int(n[0]))
    elif query == 'remove':
        S.discard(int(n[0]))
    elif query == 'check':
        sys.stdout.write(f'{int(S.issuperset({int(n[0])}))}\n')
    elif query == 'toggle':
        S.symmetric_difference_update({int(n[0])})
    elif query == 'all':
        S.clear()
        S.update(range(1, 21))
    elif query == 'empty':
        S.clear()
