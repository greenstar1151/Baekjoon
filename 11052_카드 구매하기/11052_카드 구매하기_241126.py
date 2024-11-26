import sys

input = sys.stdin.readline


def solution(N: int, cardpacks: list[int]):
    DP = [0 for _ in range(N + 1)]
    DP[1] = cardpacks[0]

    for i in range(2, N + 1):
        DP[i] = cardpacks[i - 1]
        max_price = 0
        for j in range(i // 2 + 1):
            price = DP[i - j] + DP[j]
            if price > max_price:
                max_price = price
        DP[i] = max_price
    return DP[N]


if __name__ == "__main__":
    N = int(input())
    cardpacks = list(map(int, input().rstrip().split()))
    print(solution(N, cardpacks))
