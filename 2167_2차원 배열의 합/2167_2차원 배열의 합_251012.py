import sys

input = sys.stdin.readline


def build_prefix_mat(mat: list[list[int]]):
    prefix_mat = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
    for i in range(1, len(mat) + 1):
        for j in range(1, len(mat[0]) + 1):
            prefix_mat[i][j] = (
                prefix_mat[i - 1][j]
                + prefix_mat[i][j - 1]
                - prefix_mat[i - 1][j - 1]
                + mat[i - 1][j - 1]
            )

    return prefix_mat


def solution(mat: list[list[int]], queries: list[tuple[int, ...]]):
    prefix_mat = build_prefix_mat(mat)
    for q in queries:
        i, j, x, y = q
        yield (
            prefix_mat[x][y]
            - prefix_mat[x][j - 1]
            - prefix_mat[i - 1][y]
            + prefix_mat[i - 1][j - 1]
        )


if __name__ == "__main__":
    N, M = map(int, input().split())
    mat: list[list[int]] = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    K = int(input())
    queries: list[tuple[int, ...]] = []
    for _ in range(K):
        queries.append(tuple(map(int, input().split())))

    for ans in solution(mat, queries):
        sys.stdout.write(f"{ans}\n")
