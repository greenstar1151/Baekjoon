import sys
import math


def solution(N: int):
    upper_square_num = math.ceil(math.sqrt(N))
    DP = [0 for _ in range(N + 1)]

    for i in range(1, N + 1):
        candidates = [
            DP[i - j**2] + 1 for j in range(1, upper_square_num + 1) if i - j**2 >= 0
        ]
        DP[i] = min(candidates) if candidates else 1

    return DP[N]


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    print(solution(N))
