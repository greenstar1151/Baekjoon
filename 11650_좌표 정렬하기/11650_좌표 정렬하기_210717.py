import sys


N = int(input())
stdin = sys.stdin.read().rstrip()
coords = stdin.split('\n')
coords = [tuple(map(int, coord.split())) for coord in coords]

coords = sorted(coords, key=lambda x: (x[0], x[1]))
print('\n'.join([f'{c[0]} {c[1]}' for c in coords]))
