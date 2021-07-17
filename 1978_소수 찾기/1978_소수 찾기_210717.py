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



N = input()
nums = map(int, input().split())


counter = 0
for n in nums:
    if is_prime(n):
        counter += 1

print(counter)
