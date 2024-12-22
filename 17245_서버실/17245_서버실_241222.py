import sys
from collections import Counter
from itertools import chain, starmap
from operator import mul


def solution(server_sizes: dict[int, int]) -> int:
    all_servers = sum(starmap(mul, server_sizes.items()))
    majority_minimum = (all_servers + 1) // 2
    low, high = 0, max(server_sizes.keys())
    mid = (low + high) // 2
    while low < mid:
        if (
            sum(min(lv, mid) * amount for lv, amount in server_sizes.items())
            < majority_minimum
        ):
            low = mid
        else:
            high = mid
        mid = (low + high) // 2

    return high


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    server_room = (
        tuple(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    )
    server_sizes = Counter(chain.from_iterable(server_room))
    print(solution(server_sizes))
