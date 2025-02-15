import sys
from itertools import islice
from math import floor

CUT_RATIO = 0.15


def round(x: float):
    return floor(x + 0.5)


def solution(n: int, votes: list[int]):
    cutoff = round(n * CUT_RATIO)
    effective_votes = list(islice(sorted(votes), cutoff, n - cutoff))
    return round(sum(effective_votes) / len(effective_votes))


def main():
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        return
    votes = list(map(int, sys.stdin.read().rstrip().split("\n")))
    print(solution(n, votes))


if __name__ == "__main__":
    main()
