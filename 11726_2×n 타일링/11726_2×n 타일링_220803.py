# from functools import cache
# import sys

# sys.setrecursionlimit(10 ** 6)

# @cache
# def n2_tiles(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 3
#     else:
#         return (n2_tiles(n-1) + n2_tiles(n-2)) % 10007

# print(n2_tiles(int(input())) % 10007)

n = int(input())
dp_table = [0 for _ in range(n+1)]
dp_table[1:4] = [1, 2, 3]
for i in range(4, n+1):
    dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 10007

print(dp_table[n] % 10007)
