d1, d2, d3 = map(int, input().split())
a = (d1 + d2 - d3) / 2
b = (d1 - d2 + d3) / 2
c = (-d1 + d2 + d3) / 2

if a > 0 and b > 0 and c > 0:
    print(1)
    print(' '.join(map(str, [round(x, 2) for x in (a, b, c)])))
else:
    print(-1)
