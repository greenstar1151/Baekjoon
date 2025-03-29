import sys
from itertools import pairwise, product, starmap
from operator import mul

input = sys.stdin.readline


def solution(w: int, h: int, w_cut: list[int], h_cut: list[int]):
    w_sizes = [hi - lo for lo, hi in pairwise([0] + sorted(w_cut) + [w])]
    h_sizes = [hi - lo for lo, hi in pairwise([0] + sorted(h_cut) + [h])]
    return max(starmap(mul, product(w_sizes, h_sizes)))


if __name__ == "__main__":
    w, h = map(int, input().split())
    cut_count = int(input())
    w_cut: list[int] = []
    h_cut: list[int] = []
    for _ in range(cut_count):
        d, pos = map(int, input().split())
        if d == 0:
            h_cut.append(pos)
        elif d == 1:
            w_cut.append(pos)

    print(solution(w, h, w_cut, h_cut))
