N = int(input())
P = list(map(int, input().split()))

P.sort()
accumulative_sum = 0
for i, p_i in enumerate(P):
    accumulative_sum += (N - i) * p_i

print(accumulative_sum)
