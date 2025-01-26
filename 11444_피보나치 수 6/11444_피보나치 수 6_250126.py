import sys
from typing import TypeAlias

Matrix2D: TypeAlias = list[list[int]]


def apply_mod(matrix: Matrix2D, mod: int):
    return [[col % mod for col in row] for row in matrix]


def matrix_mul(m_1: Matrix2D, m_2: Matrix2D):
    result: Matrix2D = []
    for i in range(len(m_1)):
        row: list[int] = []
        for j in range(len(m_2[0])):
            row.append(sum(m_2[k][j] * e for k, e in enumerate(m_1[i])))
        result.append(row)
    return result


def recursive_fibonacci(k: int, mod: int) -> Matrix2D:
    FIB_0 = [[0, 0], [0, 0]]
    FIB_1 = [[1, 1], [1, 0]]
    if k == 0:
        return FIB_0
    if k == 1:
        return FIB_1

    half = apply_mod(recursive_fibonacci(k // 2, mod), mod)
    half_squared = apply_mod(matrix_mul(half, half), mod)
    if k % 2 == 0:
        return half_squared
    else:
        return apply_mod(matrix_mul(FIB_1, half_squared), mod)


def fibonacci(n: int, mod: int):
    fib_matrix = recursive_fibonacci(n, mod)

    return fib_matrix[0][1]


def solution():
    n = int(sys.stdin.readline().rstrip())
    print(fibonacci(n, 1_000_000_007))


if __name__ == "__main__":
    solution()
