import sys


def solution(S1: str, S2: str):
    S1_l, S2_l = len(S1), len(S2)
    DP = [[0 for _ in range(S2_l + 1)] for _ in range(S1_l + 1)]

    for i in range(1, S1_l + 1):
        for j in range(1, S2_l + 1):
            if S1[i - 1] == S2[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
                continue
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

    return DP[S1_l][S2_l]


if __name__ == "__main__":
    S1, S2 = sys.stdin.read().rstrip().split("\n")
    print(solution(S1, S2))
