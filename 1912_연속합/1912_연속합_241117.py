import sys

input = sys.stdin.readline


def solution(sequence: list[int]):
    max_subsequence_sum = float("-inf")
    current_max_sum = 0
    for e in sequence:
        current_max_sum = max(e, current_max_sum + e)
        max_subsequence_sum = max(max_subsequence_sum, current_max_sum)

    return max_subsequence_sum


if __name__ == "__main__":
    n = int(input().rstrip())
    sequence = list(map(int, input().rstrip().split()))
    print(solution(sequence))
