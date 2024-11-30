import sys
from functools import cache

sys.setrecursionlimit(500**2)


def solution(N: int, matrices: list[tuple[int, ...]]):
    @cache
    def matmulcount(i: int, j: int) -> int:
        nonlocal N, matrices
        if i == j:
            return 0
        min_count = [
            matmulcount(i, k)
            + matmulcount(k + 1, j)
            + matrices[i - 1][0] * matrices[k - 1][1] * matrices[j - 1][1]
            for k in range(i, j)
        ]
        return min(min_count)

    return matmulcount(1, N)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    matrices = [
        tuple(map(int, m.split())) for m in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(N, matrices))
