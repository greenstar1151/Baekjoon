n = int(input())
s = set()

for i in range(1, int(n**0.5)+1):
    for j in range(1, int((n // i) ** 0.5) + 1):
        for k in range(1, n // (i * j) + 1):
            if i * j * k == n:
                s.add(tuple(sorted([i,j,k])))

print(' '.join([str(x) for x in sorted(list(s), key=lambda x: x[0]*x[1] + x[1]*x[2] + x[2]*x[0])[0]]))
