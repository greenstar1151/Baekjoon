import sys
from math import ceil

input = sys.stdin.readline


def solution(N: int, T: int, P: int, sizes: list[int]):
    return sum(ceil(s / T) for s in sizes), divmod(N, P)


if __name__ == "__main__":
    N = int(input())
    sizes = list(map(int, input().split()))
    T, P = map(int, input().split())
    shirts, pens = solution(N, T, P, sizes)
    print(f"{shirts}\n{pens[0]} {pens[1]}")
