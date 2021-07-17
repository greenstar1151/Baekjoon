import sys


def is_prime(n: int) -> bool: 
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    k, l = 5, n**0.5
    while k <= l:
        if n % k == 0 or n % (k+2) == 0:
            return False
        k += 6
    return True



M, N = map(int, input().split())


prime_list = []
for k in range(M, N+1):
    if is_prime(k):
        prime_list.append(k)

sys.stdout.write('\n'.join([str(x) for x in prime_list]))
