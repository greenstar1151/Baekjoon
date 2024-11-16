import sys

input = sys.stdin.readline


def solution(N: int, prices: list[int]):
    returns = 0
    latest_top = prices[-1]
    for i in range(N - 1, -1, -1):
        if prices[i] < latest_top:
            returns += latest_top - prices[i]
        elif prices[i] > latest_top:
            latest_top = prices[i]

    return returns


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        prices = list(map(int, input().split()))
        print(solution(N, prices))
