import sys
from itertools import combinations


def solution(N: int, stats: list[list[int]]):
    min_diff = float("inf")
    for pool in combinations(range(1, N + 1), N // 2):
        start_team = 0
        link_team = 0
        for i, j in combinations(pool, 2):
            start_team += stats[i - 1][j - 1]
            start_team += stats[j - 1][i - 1]
        for i, j in combinations(set(range(1, N + 1)) - set(pool), 2):
            link_team += stats[i - 1][j - 1]
            link_team += stats[j - 1][i - 1]
        min_diff = min(min_diff, abs(start_team - link_team))

    return min_diff


if __name__ == "__main__":
    stdin_read = sys.stdin.read().strip().split("\n")
    N, *stats = stdin_read
    stats = [list(map(int, row.split())) for row in stats]
    print(solution(int(N), stats))
