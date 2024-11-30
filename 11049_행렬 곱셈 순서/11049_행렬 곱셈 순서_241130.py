import sys

sys.setrecursionlimit(500**2)


def solution(N: int, matrices: list[tuple[int, ...]]):
    # DP[i][j] -> i ~ j 번째 행렬을 곱할 때 곱셈 횟수의 최솟값
    DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for range_size in range(N):
        # DP[1][1], ... DP[N][N]
        # DP[1][2], ... DP[N-1][N]
        # ...
        # DP[1][N]
        for i in range(1, N - range_size + 1):
            j = i + range_size
            if i == j:
                DP[i][j] = 0
                continue
            DP[i][j] = min(
                DP[i][k]
                + DP[k + 1][j]
                + matrices[i - 1][0] * matrices[k - 1][1] * matrices[j - 1][1]
                for k in range(i, j)
            )

    return DP[1][N]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    matrices = [
        tuple(map(int, m.split())) for m in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(N, matrices))
