def factorial(s, n):
    f = 1
    for i in range(s, n+1):
        f *= i
    return f


N = int(input())


counter = 0
if (N - 1) % 3 == 0:
    for i in range(1, N, 3):
        counter += factorial(i+1, N-1)//factorial(1, N-1 - i)
elif (N - 1) % 3 == 1:
    for i in range(0, N, 3):
        counter += factorial(i+1, N-1)//factorial(1, N-1 - i)
elif (N - 1) % 3 == 2:
    for i in range(2, N, 3):
        counter += factorial(i+1, N-1)//factorial(1, N-1 - i)

print(counter % 1000000007)
