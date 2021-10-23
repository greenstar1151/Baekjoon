import sys


T = int(input())
case_in = sys.stdin.read().rstrip()
cases = case_in.split('\n')

L = [1]
S = [1]
# n_1_L = 7
# n_1_S = 3
# n_2_L = n_1_L * 3 + n_1_S * 4
# n_2_S = n_1_S + n_1_L * 2


for _ in range(1000000):
    l, s = L[-1], S[-1]
    L.append((l*3 + s*4) % 1000000007)
    S.append((l + s*2) % 1000000007)

for N in cases:
    N = int(N)
    print((L[N]) % 1000000007)
