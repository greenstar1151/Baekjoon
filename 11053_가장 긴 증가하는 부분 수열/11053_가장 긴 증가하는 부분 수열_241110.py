import sys


def solution(sequence: list[int]):
    # DP[i] -> 수열 i번째를 마지막으로 가지는 가장 긴 증가하는 부분 수열의 길이
    DP = [0 for _ in range(len(sequence) + 1)]  # 1-based index
    DP[1] = 1

    for i in range(2, len(sequence) + 1):
        prev_max_lis = 0  # 수열 i-1번째까지 수들 가운데 i번째 수보다 작은 수로 끝나는 가장 긴 LIS의 길이
        for j in range(i):
            if sequence[j - 1] < sequence[i - 1]:
                if prev_max_lis < DP[j]:
                    prev_max_lis = DP[j]
        DP[i] = prev_max_lis + 1

    return max(DP)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    print(solution(A))
