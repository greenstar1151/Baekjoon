import sys


class TrominoBoard:
    def __init__(self, size: int):
        self.size = size
        self.board = [[-1 for _ in range(self.size)] for _ in range(self.size)]
        self.tromino_id = 1

    def get_new_tromino_id(self):
        current_id = self.tromino_id
        self.tromino_id += 1
        return current_id

    def _recursive_fill(
        self,
        hole: tuple[int, int],
        size: int,
        offset: tuple[int, int],
    ):
        """
        격자판(size)을 사분할하여 4개의 작은 격자판(size//2)으로 나누고, 구멍이 위치한 격자판(size//2)을 제외한 나머지의 경우
        격자판(size)의 중심 부근에 하나씩 새로운 구멍을 만들고 각각의 격자판(size//2)에 대해 같은 작업을 재귀적으로 반복합니다.
        새로 생긴 구멍 3개는 하나의 트리미노 조각을 채워둡니다.
        """
        tromino_id = self.get_new_tromino_id()
        if size == 2:  # base case
            for i in range(2):
                for j in range(2):
                    x, y = offset[0] + i, offset[1] + j
                    if x == hole[0] and y == hole[1]:
                        continue
                    self.board[x][y] = tromino_id
            return
        center = (offset[0] + size // 2 - 1, offset[1] + size // 2 - 1)
        relative_hole = (hole[0] - offset[0], hole[1] - offset[1])
        for i in range(2):
            for j in range(2):
                recursive_hole = center[0] + i, center[1] + j
                recursive_offset = (
                    offset[0] + i * (size // 2),
                    offset[1] + j * (size // 2),
                )
                # 사분면 중 구멍이 위치한 사분면은 재귀 시 그 구멍의 좌표를 그대로 전달
                if i == (relative_hole[0] // (size // 2)) and j == (
                    relative_hole[1] // (size // 2)
                ):
                    self._recursive_fill(hole, size // 2, recursive_offset)
                else:
                    self._recursive_fill(recursive_hole, size // 2, recursive_offset)
                    self.board[center[0] + i][center[1] + j] = tromino_id

    def fill_tiles(self, hole: tuple[int, int]):
        self._recursive_fill(hole, self.size, (0, 0))

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.board) + "\n"


def solution():
    K = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().rstrip().split())
    size = 2**K
    i, j = size - y, x - 1
    tromino_board = TrominoBoard(size)
    tromino_board.fill_tiles(hole=(i, j))
    sys.stdout.write(str(tromino_board))


if __name__ == "__main__":
    solution()
