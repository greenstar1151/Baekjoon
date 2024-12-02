import sys

input = sys.stdin.readline


def solution(N: int, K: int, goods: list[tuple[int, ...]]):
    DP = [0] * (K + 1)
    for w, v in goods:
        for i in range(K, w - 1, -1):
            DP[i] = max(DP[i], DP[i - w] + v)
    return DP[K]


if __name__ == "__main__":
    N, K = map(int, input().split())
    goods = [
        tuple(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]

    print(solution(N, K, goods))
