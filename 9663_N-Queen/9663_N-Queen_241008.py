import sys


class NQueen:
    def __init__(self, N: int):
        self.N = N
        self.queen_layout = [0 for _ in range(N)]  # queen on ith row in nth col
        self.valid_arrangements_count = 0
        self.occupied_rows: set[int] = set()
        self.occupied_upper_diag: set[int] = set()  # /
        self.occupied_lower_diag: set[int] = set()  # \

    def is_safe_to_place(self, row: int, col: int):
        if (
            (row in self.occupied_rows)
            or (row + col in self.occupied_upper_diag)
            or (self.N - 1 - row + col in self.occupied_lower_diag)
        ):
            return False
        return True

    def _place_queen(self, col: int):
        if col == self.N:
            self.valid_arrangements_count += 1
            return

        for i in range(self.N):
            if self.is_safe_to_place(i, col):
                self.queen_layout[col] = i
                self.occupied_rows.add(i)
                self.occupied_upper_diag.add(col + i)
                self.occupied_lower_diag.add(col + (self.N - 1 - i))
            else:
                continue
            self._place_queen(col + 1)
            self.occupied_rows.discard(i)
            self.occupied_upper_diag.discard(col + i)
            self.occupied_lower_diag.discard(col + (self.N - 1 - i))

    def search_layout(self):
        self._place_queen(0)


def solution():
    N = int(sys.stdin.readline().rstrip())
    board = NQueen(N)
    board.search_layout()
    print(board.valid_arrangements_count)


if __name__ == "__main__":
    solution()
