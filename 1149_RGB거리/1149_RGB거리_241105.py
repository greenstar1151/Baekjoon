import sys


def solution(N: int, costs: list[list[int]]):
    # DP[i][0] -> i번째 집이 빨강일 때 i번째 집까지 칠하는 비용의 최솟값
    # DP[i][1] -> i번째 집이 초록일 때 i번째 집까지 칠하는 비용의 최솟값
    # DP[i][2] -> i번째 집이 파랑일 때 i번째 집까지 칠하는 비용의 최솟값
    DP = [[0 for _ in range(3)] for _ in range(N)]
    DP[0][0], DP[0][1], DP[0][2] = costs[0][0], costs[0][1], costs[0][2]

    for i in range(1, N):
        r, g, b = costs[i]
        DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + r
        DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + g
        DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + b

    return min(DP[N - 1])


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    costs = [
        list(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(N, costs))
