import sys


def solution(N: int, K: int):
    DP = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for n in range(N + 1):
        for k in range(min(K, n) + 1):
            if k == 0 or n == k:
                DP[n][k] = 1
                continue
            DP[n][k] = ((DP[n - 1][k] % 10007) + (DP[n - 1][k - 1] % 10007)) % 10007

    return DP[N][K]


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(solution(N, K))
