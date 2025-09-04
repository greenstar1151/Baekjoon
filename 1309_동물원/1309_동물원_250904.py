MODULO = 9901


def solution(N: int):
    # DP[n][x]: n칸인 동물원에서 마지막 칸의 배치 상태가
    # x=0: [0, 0] / x=1: [1, 0] / x=2: [0, 1] (0: 없음, 1: 있음)
    DP = [[0] * 3 for _ in range(N + 1)]
    DP[1] = [1, 1, 1]
    for i in range(2, N + 1):
        DP[i][0] = sum(DP[i - 1]) % MODULO
        DP[i][1] = (DP[i - 1][0] + DP[i - 1][2]) % MODULO
        DP[i][2] = (DP[i - 1][0] + DP[i - 1][1]) % MODULO

    return sum(DP[N]) % MODULO


if __name__ == "__main__":
    N = int(input())
    print(solution(N))
