import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
people = stdin.split('\n')
people = [p.split() for p in people]
people = map(lambda x: (int(x[0]), x[1]), people)


people = sorted(people, key=lambda x: x[0])
people = [f'{p[0]} {p[1]}' for p in people]
print('\n'.join(people))
