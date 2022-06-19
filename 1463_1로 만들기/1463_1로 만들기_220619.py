N = int(input())

dp_table = [0 for _ in range(10 ** 6 + 1)]
for i in range(2, N + 1):
    candidate = []
    if i % 3 == 0:
        candidate.append(dp_table[i // 3] + 1)
    if i % 2 == 0:
        candidate.append(dp_table[i // 2] + 1)
    candidate.append(dp_table[i - 1] + 1)
    dp_table[i] = min(candidate)
    
print(dp_table[N])
