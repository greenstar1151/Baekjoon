N, K = map(int, input().split())
inv99 = []

for i in range(1, K + 1):
    inv99.append(int(str(N * i)[::-1]))

inv99.sort(reverse=True)

print(inv99[0])
