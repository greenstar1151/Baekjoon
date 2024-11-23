import sys


def solution(n: int, k: int, coins: list[int]):
    # DP[i][j] -> i-1번째 동전을 포함하여 k원을 만드는 경우의 수
    # DP = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    # 메모리 제약으로 인해 직전 값 테이블만 유지
    MEMO = [[0 for _ in range(k + 1)] for _ in range(2)]

    MEMO[1] = [1] * (k + 1)  # base case, n == 1
    MEMO[0][0] = 1  # base case, k == 0

    for i in range(1, n + 1):
        for j in range(k + 1):
            MEMO[1][j] = (
                MEMO[0][j] + MEMO[1][j - coins[i - 1]]
                if j - coins[i - 1] >= 0
                else MEMO[0][j]
            )
        MEMO.pop(0)
        MEMO.append([0] * (k + 1))

    return MEMO[0][k]


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().rstrip().split())
    coins = list(map(int, sys.stdin.read().rstrip().split("\n")))
    coins.sort()
    print(solution(n, k, coins))
