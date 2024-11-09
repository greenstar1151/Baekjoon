import sys


def solution(n: int, int_triangle: list[list[int]]):
    # DP[i] -> 정수 삼각형의 i번째 행까지, 해당 원소까지 도달하는 경로 중 합의 최댓값들의 행
    DP: list[list[int]] = [[] for _ in range(n)]
    for i, row in enumerate(int_triangle):
        if i < 1:
            DP[i] = row
            continue
        for j, e in enumerate(row):
            if j == 0:
                DP[i].append(DP[i - 1][0] + e)
            elif j == i:
                DP[i].append(DP[i - 1][j - 1] + e)
            else:
                DP[i].append(max(DP[i - 1][j - 1], DP[i - 1][j]) + e)

    return max(DP[n - 1])


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    data_in = sys.stdin.read().rstrip().split("\n")
    int_triangle: list[list[int]] = []
    for row in data_in:
        int_triangle.append(list(map(int, row.split())))
    print(solution(n, int_triangle))
