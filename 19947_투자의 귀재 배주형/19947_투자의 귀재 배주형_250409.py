from math import floor


def solution(principal: int, years: int):
    DP = [0.0 for _ in range(years + 1)]
    DP[0] = principal
    for i in range(1, years + 1):
        candidates: list[float] = [DP[i - 1] * 1.05]
        if i - 3 >= 0:
            candidates.append(DP[i - 3] * 1.2)
        if i - 5 >= 0:
            candidates.append(DP[i - 5] * 1.35)
        DP[i] = max(map(floor, candidates))
    return DP[years]


if __name__ == "__main__":
    H, Y = map(int, input().split())
    print(solution(H, Y))
