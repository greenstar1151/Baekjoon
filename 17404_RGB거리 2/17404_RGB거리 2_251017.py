import sys


def solution(N: int, costs: list[list[int]]):
    # 0-based index
    # DP[0][:][:] -> 0번째 집이 빨강일 때
    # DP[1][:][:] -> 0번째 집이 초록일 때
    # DP[2][:][:] -> 0번째 집이 파랑일 때
    # DP[:][i][0] -> i번째 집이 빨강일 때 i번째 집까지 칠하는 비용의 최솟값
    # DP[:][i][1] -> i번째 집이 초록일 때 i번째 집까지 칠하는 비용의 최솟값
    # DP[:][i][2] -> i번째 집이 파랑일 때 i번째 집까지 칠하는 비용의 최솟값
    DP: list[list[list[int | float]]] = [
        [[float("inf") for _ in range(3)] for _ in range(N)] for _ in range(3)
    ]
    DP[0][0][0], DP[1][0][1], DP[2][0][2] = costs[0][0], costs[0][1], costs[0][2]
    for i in range(3):
        for j in range(1, N):
            r, g, b = costs[j]
            DP[i][j][0] = min(DP[i][j - 1][1], DP[i][j - 1][2]) + r
            DP[i][j][1] = min(DP[i][j - 1][0], DP[i][j - 1][2]) + g
            DP[i][j][2] = min(DP[i][j - 1][0], DP[i][j - 1][1]) + b

    candidates: list[int | float] = []
    for i in range(3):
        for j, v in enumerate(DP[i][N - 1]):
            if i == j:
                continue
            candidates.append(v)
    return min(candidates)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    costs = [
        list(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(N, costs))
