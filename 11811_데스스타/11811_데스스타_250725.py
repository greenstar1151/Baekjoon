import sys
from functools import reduce
from operator import or_


def get_seq(mat: list[list[int]]):
    return [reduce(or_, row) for row in mat]


def solution(mat: list[list[int]]):
    return " ".join(map(str, get_seq(mat)))


if __name__ == "__main__":
    data_in = sys.stdin.read().strip().split("\n")
    _, *mat = data_in
    mat = [list(map(int, row.split())) for row in mat]

    print(solution(mat))
