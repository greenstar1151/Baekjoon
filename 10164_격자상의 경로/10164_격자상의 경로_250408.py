from math import factorial


def solution(rows: int, columns: int, mark_no: int):
    if mark_no == 0:
        return (
            factorial(rows - 1 + columns - 1)
            // factorial(rows - 1)
            // factorial(columns - 1)
        )
    row_idx, col_idx = divmod(mark_no - 1, columns)
    return (
        factorial(row_idx + col_idx) // factorial(row_idx) // factorial(col_idx)
    ) * (
        factorial((rows - row_idx - 1) + (columns - col_idx - 1))
        // factorial(rows - row_idx - 1)
        // factorial(columns - col_idx - 1)
    )


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    print(solution(N, M, K))
