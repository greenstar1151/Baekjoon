import sys


def solution(N: int, trigraph: list[tuple[int, ...]]):
    DP = [[0] * 3 for _ in range(N + 1)]
    DP[1][0] = trigraph[0][1] + trigraph[1][0]
    DP[1][1] = (
        min(
            [
                DP[1][0],
                trigraph[0][1],
                trigraph[0][1] + trigraph[0][2],
            ]
        )
        + trigraph[1][1]
    )
    DP[1][2] = (
        min(
            [
                DP[1][1],
                trigraph[0][1],
                trigraph[0][1] + trigraph[0][2],
            ]
        )
        + trigraph[1][2]
    )

    for i in range(2, N):
        DP[i][0] = min(DP[i - 1][:2]) + trigraph[i][0]
        DP[i][1] = min([DP[i][0]] + DP[i - 1]) + trigraph[i][1]
        DP[i][2] = min([DP[i][1]] + DP[i - 1][1:]) + trigraph[i][2]

    return DP[N - 1][1]


if __name__ == "__main__":
    data_in = sys.stdin.read().rstrip().split("\n")
    handle = 0
    tc = 1
    while True:
        N = int(data_in[handle].strip())
        if N == 0:
            break

        trigraph = [
            tuple(map(int, row.split())) for row in data_in[handle + 1 : handle + N + 1]
        ]
        print(f"{tc}. {solution(N, trigraph)}")
        handle += N + 1
        tc += 1
