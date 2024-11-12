import sys
from functools import cache


def solution(N: int, schedules: list[list[int]]):
    # naive DP(memoization)
    @cache
    def pay(i: int, j: int) -> int:
        if i == j:
            return 0
        return max(
            pay(i, k) + schedules[k][1] + pay(k + schedules[k][0], j)
            if k + schedules[k][0] <= j
            else 0
            for k in range(i, j)
        )

    return pay(0, N)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    schedules = [
        list(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(N, schedules))
