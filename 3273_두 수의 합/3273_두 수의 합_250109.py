import sys
from collections import Counter

input = sys.stdin.readline


def solution(seq: list[int], x: int):
    counter: Counter[int] = Counter()
    pairs_count = 0
    for a_i in seq:
        if a_i >= x:
            continue
        pairs_count += counter[a_i]
        counter[x - a_i] += 1
    return pairs_count


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    x = int(input())
    print(solution(seq, x))
