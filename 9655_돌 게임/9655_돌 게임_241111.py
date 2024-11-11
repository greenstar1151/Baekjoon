import sys


def solution(N: int):
    # DP[i][0] -> 돌이 i개 있을 때 상근이부터 시작해서 게임을 이기는지 여부(0: 짐, 1: 이김)
    # DP[i][1] -> 돌이 i개 있을 때 창영이부터 시작해서 게임을 이기는지 여부
    DP = [[-1, -1] for _ in range(N + 1)]

    if N == 1:
        return "SK"
    elif N == 2:
        return "CY"

    DP[1][0], DP[1][1] = 1, 1
    DP[2][0], DP[2][1] = 0, 0
    DP[3][0], DP[3][1] = 1, 1

    for i in range(4, N + 1):
        DP[i][0] = 1 if DP[i - 3][1] == 0 or DP[i - 1][1] == 0 else 0
        DP[i][1] = 1 if DP[i - 3][0] == 0 or DP[i - 1][0] == 0 else 0

    return "SK" if DP[N][0] == 1 else "CY"


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))
