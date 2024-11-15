import sys

input = sys.stdin.readline


def solution(N: int) -> int:
    MAX_LENGTH = 100
    if N == 1:
        return 9

    # DP[i][j] -> i자리의 계단 수에서 가장 왼쪽에 있는 수가 j인 계단 수의 개수 (i > 1)
    DP = [[0 for _ in range(10)] for _ in range(MAX_LENGTH + 1)]
    DP[1] = [1] * 10
    for i in range(2, N + 1):
        digit_start = 1 if i == N else 0  # 0으로 시작하는 수 제외
        for j in range(digit_start, 10):
            if j == 9:
                DP[i][j] = DP[i - 1][j - 1]
            elif j == 0:
                DP[i][j] = DP[i - 1][j + 1]
            else:
                DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % 10**9

    return sum(DP[N]) % 10**9


if __name__ == "__main__":
    N = int(input().rstrip())
    print(solution(N))
