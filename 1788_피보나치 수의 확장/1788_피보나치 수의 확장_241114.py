import sys

input = sys.stdin.readline


def solution(n: int):
    # F(-1) == 1
    # F(-2) == -1
    # F(-3) == 2
    # F(-4) == -3
    # ...
    DP = [0 for _ in range(abs(n) + 2)]
    DP[1] = 1

    for i in range(2, abs(n) + 1):
        DP[i] = (DP[i - 2] % 10**9 + DP[i - 1] % 10**9) % 10**9

    sign = 1
    sign = -1 if n < 0 and n % 2 == 0 else sign
    sign = 0 if n == 0 else sign
    return sign, DP[abs(n)]


if __name__ == "__main__":
    n = int(input().rstrip())
    print("\n".join(map(str, solution(n))))
