MODULO = 10007


def solution(N: int):
    # DP[n][x]: x로 시작하는 n자리 오르막 수
    DP = [[0] * 10 for _ in range(N + 1)]
    # 1자리 오르막 수
    for i in range(10):
        DP[1][i] = 1

    for i in range(2, N + 1):
        for j in range(9, -1, -1):
            DP[i][j] = sum(DP[i - 1][j:]) % MODULO
    return sum(DP[N]) % MODULO


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
