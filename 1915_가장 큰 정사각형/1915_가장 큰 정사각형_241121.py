import sys


def solution(n: int, m: int, field: list[list[int]]):
    # padding
    for row in field:
        row.insert(0, 0)
    field.insert(0, [0] * (m + 1))

    DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if field[i][j] == 0:
                continue
            DP[i][j] = min(DP[i - 1][j - 1], DP[i][j - 1], DP[i - 1][j]) + 1

    return max(map(max, DP)) ** 2


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    field = [
        list(map(int, list(line))) for line in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(n, m, field))
