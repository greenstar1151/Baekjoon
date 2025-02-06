import sys


def digitsum(n: int, base: int, exp: int = 4):
    value = 0
    for e in range(1, exp + 1):
        value += (n % (base ** (e))) // (base ** (e - 1))
    return value


for i in range(1000, 10000):
    base10, base12, base16 = digitsum(i, 10), digitsum(i, 12), digitsum(i, 16)
    if base10 == base12 == base16:
        sys.stdout.write(f"{i}\n")
