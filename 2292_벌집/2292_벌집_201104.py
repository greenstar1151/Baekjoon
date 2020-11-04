import math


N = int(input())
if N == 1:
    print(1)
else:
    sum = math.floor((N - 2) / 6)
    print(math.floor((-1 + math.sqrt(1 + 8 * sum)) / 2) + 2)
