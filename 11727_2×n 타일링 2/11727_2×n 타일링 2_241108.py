import sys


def solution(n: int):
    # DP[i] -> 2×i 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수
    # NOTE: 2×0 직사각형도 1개의 방법이 있다고 취급
    DP = [1 for _ in range(n + 1)]  # 1-based index

    for i in range(2, n + 1):
        DP[i] = (DP[i - 1] % 10007 + (2 * DP[i - 2]) % 10007) % 10007

    return DP[n]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(solution(n))
