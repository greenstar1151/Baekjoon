import sys

input = sys.stdin.readline


MAX_CUSTOMER_PER_CITY = 100
INF = float("inf")


def solution(target: int, cities: list[tuple[int, ...]]):
    limit = target + MAX_CUSTOMER_PER_CITY
    dp = [INF] * (limit + 1)
    dp[0] = 0

    for cost, ret in cities:
        for i in range(ret, limit + 1):
            dp[i] = min(dp[i], dp[i - ret] + cost)

    return min(dp[target:])


if __name__ == "__main__":
    C, N = map(int, input().split())
    costs = [
        tuple(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]

    print(solution(C, costs))
