import sys

input = sys.stdin.readline


def solution(n: int, stickers: tuple[tuple[int, ...], ...]):
    # DP[i][j] -> 2*i의 스티커 판이 있을 때, j행 i열의 스티커를 뗀다고 했을 때의 최대 점수 합
    # NOTE: j == 0인 경우 스티커를 떼지 않음
    DP = [[0] * 3 for _ in range(n + 1)]

    DP[1] = [0, stickers[0][0], stickers[1][0]]

    for i in range(2, n + 1):
        DP[i][0] = max(DP[i - 1])
        DP[i][1] = max(DP[i - 1][2], DP[i - 1][0]) + stickers[0][i - 1]
        DP[i][2] = max(DP[i - 1][1], DP[i - 1][0]) + stickers[1][i - 1]

    return max(DP[n])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        sticker_0 = tuple(map(int, input().split()))
        sticker_1 = tuple(map(int, input().split()))
        print(solution(n, (sticker_0, sticker_1)))
