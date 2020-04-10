def starline(n):
    print('*' * (2 * n - 1))

N = int(input())

for i in range(N, 0, -1):
    print(' ' * (N - i), end='')
    starline(i)

for i in range(2, N+1):
    print(' ' * (N - i), end='')
    starline(i)
