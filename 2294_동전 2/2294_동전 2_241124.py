import sys


def solution(k: int, coins: list[int]):
    DP = [0 for _ in range(k + 1)]

    for i in range(1, k + 1):
        candidates = [DP[i - c] for c in coins if i - c >= 0 and DP[i - c] >= 0]
        DP[i] = min(candidates) + 1 if candidates else -1

    return DP[k]


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().rstrip().split())
    coins = list(set(map(int, sys.stdin.read().rstrip().split("\n"))))
    print(solution(k, coins))
