import sys
from itertools import accumulate

input = sys.stdin.readline


class CumulativeTable:
    def __init__(self, table: list[list[int]]):
        self.acc_table = [[0]] + [[0] + list(accumulate(row)) for row in table]

    def get_range_sum(self, x1: int, y1: int, x2: int, y2: int):
        return sum(row[y2] - row[y1 - 1] for row in self.acc_table[x1 : x2 + 1])


if __name__ == "__main__":
    N, M = map(int, input().split())
    table: list[list[int]] = []
    for _ in range(N):
        table.append(list(map(int, input().split())))
    acc_table = CumulativeTable(table)
    for _ in range(M):
        sys.stdout.write(f"{acc_table.get_range_sum(*map(int, input().split()))}\n")
