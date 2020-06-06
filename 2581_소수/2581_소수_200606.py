def prime_table_until(n):
    prime_table = [False, False] + [True] * (n-1)
    for i, num in enumerate(prime_table):
        if num is True:
            c = i + i
            while c <= n:
                prime_table[c] = False
                c += i         
    return prime_table



M = int(input())
N = int(input())


prime_table = prime_table_until(10000)
primes = []

for n in range(M, N+1):
    if prime_table[n] == True:
        primes.append(n)
    else:
        continue
else:
    if len(primes) == 0:
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))
