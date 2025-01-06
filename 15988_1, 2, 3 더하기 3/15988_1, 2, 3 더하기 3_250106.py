import sys


def solution(testcases: list[int]):
    DP = [0, 1, 2, 4] + [-1] * 1_000_000
    for i in range(4, 1_000_001):
        DP[i] = (DP[i - 3] + DP[i - 2] + DP[i - 1]) % 1_000_000_009

    for tc in testcases:
        yield DP[tc] % 1_000_000_009


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    testcases = list(map(int, sys.stdin.read().rstrip().split("\n")))
    for ans in solution(testcases):
        sys.stdout.write(f"{ans}\n")
