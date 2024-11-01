import sys


def solution(stairs: list[int], N: int):
    if N == 1:
        return stairs[0]
    stairs = [0] + stairs
    DP = [[0 for _ in range(3)] for _ in range(N + 1)]  # 1-based index
    # DP[i][j] -> j개의 계단을 연속해서 밟은 상태에서 i번째 계단을 밟았을 때 지금까지의 최댓값
    # DP[k][1] = max([DP[k-2][1], DP[k-2][2]]) + stairs[k] # k-1번째 계단은 건너뜀
    # DP[k][2] = DP[k-1][1] + stairs[k]
    DP[1][1], DP[1][2] = stairs[1], 0
    DP[2][1], DP[2][2] = stairs[2], stairs[1] + stairs[2]
    for i in range(3, N + 1):
        DP[i][1] = max(DP[i - 2][1], DP[i - 2][2]) + stairs[i]
        DP[i][2] = DP[i - 1][1] + stairs[i]
    return max(DP[N])


def solution2(stairs: list[int], N: int):
    if N == 1:
        return stairs[0]
    stairs = [0] + stairs
    DP = [0 for _ in range(N + 1)]  # 1-based index
    # DP[i] -> i번째 계단까지, 밟지 않았던 계단들의 합의 최솟값
    DP[1] = stairs[1]
    DP[2] = stairs[2]
    for i in range(3, N + 1):
        DP[i] = min(DP[i - 3], DP[i - 2]) + stairs[i]
    return sum(stairs) - min(DP[N - 1], DP[N - 2])


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    stairs = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print(solution(stairs, N))
    # print(solution2(stairs, N))
