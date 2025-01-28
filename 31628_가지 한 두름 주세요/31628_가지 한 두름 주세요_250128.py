import sys


def transpose(mat: list[list[str]]):
    for i in range(len(mat[0])):
        yield [row[i] for row in mat]


def solution(grid: list[list[str]]):
    if 1 in set(map(lambda x: len(set(x)), grid)):
        return 1
    if 1 in set(map(lambda x: len(set(x)), transpose(grid))):
        return 1
    return 0


if __name__ == "__main__":
    grid = [list(row.split()) for row in sys.stdin.read().rstrip().split("\n")]
    print(solution(grid))
