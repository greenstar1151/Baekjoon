import math

dp_table = [0 for _ in range(50001)]
n = int(input())

dp_table[1:4] = [1, 2, 3]
for i in range(4, n+1):
    dp_table[i] = 1 + min([dp_table[i - m**2] for m in range(1, math.floor(math.sqrt(i))+1)])

print(dp_table[n])
