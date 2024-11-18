import sys

input = sys.stdin.readline


def solution(n: int):
    DP = [0 for _ in range(n + 1)]
    DP[1] = 1

    for i in range(2, n + 1):
        DP[i] = DP[i - 1] + DP[i - 2]

    return DP[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
