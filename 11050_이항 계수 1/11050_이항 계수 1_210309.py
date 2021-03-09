def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


N, K = map(int, input().split())


print(factorial(N) // (factorial(K) * factorial(N - K)))
