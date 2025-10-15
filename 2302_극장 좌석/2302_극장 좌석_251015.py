import sys
from fractions import Fraction  # type: ignore # noqa: F401
from functools import cache, reduce  # type: ignore # noqa: F401
from math import factorial  # type: ignore # noqa: F401
from operator import mul

input = sys.stdin.readline


# @cache
# def compute_cases(n: int):
#     s = 0
#     for two_block_count in range(n // 2 + 1):
#         total_arrangements = Fraction(factorial(n - two_block_count), 1)
#         one_block_arrangements = Fraction(factorial(n - 2 * two_block_count), 1)
#         two_block_arrangements = Fraction(factorial(two_block_count), 1)
#         s += int(total_arrangements / one_block_arrangements / two_block_arrangements)

#     return s


# def solution(n: int, fixed: set[int]):
#     counter = 0
#     segments: list[int] = []
#     for i in range(1, n + 1):
#         if i in fixed:
#             if counter > 0:
#                 segments.append(counter)
#             counter = 0
#         else:
#             counter += 1
#     else:
#         if counter > 0:
#             segments.append(counter)

#     return reduce(mul, (compute_cases(seg) for seg in segments + [1]))


def solution(n: int, fixed: set[int]):
    DP = [0] * (n + 1)
    DP[0], DP[1] = 1, 1
    for i in range(2, n + 1):
        DP[i] = DP[i - 1] + DP[i - 2]

    counter = 0
    segments: list[int] = []
    for i in range(1, n + 1):
        if i in fixed:
            if counter > 0:
                segments.append(counter)
            counter = 0
        else:
            counter += 1
    else:
        if counter > 0:
            segments.append(counter)
    return reduce(mul, (DP[seg] for seg in segments + [1]))


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    fixed_seat: set[int] = set()
    for _ in range(M):
        fixed_seat.add(int(input()))
    print(solution(N, fixed_seat))
