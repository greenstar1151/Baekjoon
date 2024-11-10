import sys


def solution(N: int):
    # DP[i][0] -> 0으로 끝나는 i+1자리 이친수의 개수
    # DP[i][1] -> 1로 끝나는 i+1자리 이친수의 개수
    DP = [[0, 0] for _ in range(N)]  # 0-based index

    DP[0][0], DP[0][1] = 0, 1
    for i in range(1, N):
        DP[i][0] = DP[i - 1][0] + DP[i - 1][1]
        DP[i][1] = DP[i - 1][0]

    return sum(DP[-1])


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))
