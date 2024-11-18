import sys


def solution(n: int, wines: list[int]):
    # DP[i][j] -> i번째 잔까지의 최대 포도주 양, j번째 연속된 잔을 선택했을 때(j == 0 -> 선택 안 함)
    DP = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        DP[i][0] = max(DP[i - 1])
        DP[i][1] = DP[i - 1][0] + wines[i - 1]
        DP[i][2] = DP[i - 1][1] + wines[i - 1]

    return max(DP[n])


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    wines = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print(solution(n, wines))
