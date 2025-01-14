import sys


def is_target_cable_count_possible(cables: list[int], target_count: int, length: int):
    count = 0
    for cable in cables:
        count += cable // length
    return count >= target_count


def solution(target_count: int, cables: list[int]):
    low = 1
    high = max(cables)

    result = 0
    while low <= high:
        mid = (low + high) // 2

        if is_target_cable_count_possible(cables, target_count, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


if __name__ == "__main__":
    K, N = map(int, input().split())
    cables = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print(solution(N, cables))
