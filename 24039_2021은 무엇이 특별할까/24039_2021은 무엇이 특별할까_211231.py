prime_table = [1] * 1000
for i in range(2, 1000): # sieve of Eratosthenes
    if prime_table[i] == 1:
        for j in range(i*i, 1000, i):
            prime_table[j] = 0
prime_table[1] = 0

N = int(input())
primes = []
for i in range(1, 1000):
    if prime_table[i] == 1:
        primes.append(i)

special_number = 0
idx = 0
while special_number <= N and idx < len(primes) - 2:
    special_number = primes[idx] * primes[idx+1]
    idx += 1

print(special_number)