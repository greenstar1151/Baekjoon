from functools import cache


@cache
def exp(n: int, r: int, mod: int = 1) -> int:
    if r == 1:
        return n % mod
    if r == 0:
        return 1 % mod
    half = exp(n, r // 2, mod) % mod

    if r % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * n) % mod


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(exp(A, B, C))
