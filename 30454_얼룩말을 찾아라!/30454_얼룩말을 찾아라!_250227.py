import sys

from itertools import groupby


def solution(strips: list[str]):
    stripe_counts = [
        sum(1 for key, _ in groupby(strip) if key == "1") for strip in strips
    ]
    max_stripes = max(stripe_counts) if stripe_counts else 0
    count_max_stripes = stripe_counts.count(max_stripes)

    return max_stripes, count_max_stripes


if __name__ == "__main__":
    N, L = map(int, input().split())
    print(" ".join(map(str, solution(sys.stdin.read().rstrip().split("\n")))))
