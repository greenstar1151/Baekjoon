import sys

input = sys.stdin.readline

# [(variants, shape), ...]
# variants -> (rotate, flip(horizontal))
Variant = tuple[int, int]
Variants = tuple[Variant, ...]
Shape = list[list[int]]
TETROMINOS: dict[str, tuple[Variants, Shape]] = {
    "I": (
        ((0, 0), (1, 0)),
        [
            [1, 1, 1, 1],
        ],
    ),
    "O": (((0, 0),), [[1, 1], [1, 1]]),
    "L": (
        ((0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1)),
        [[1, 0], [1, 0], [1, 1]],
    ),
    "S": (((0, 0), (1, 0), (0, 1), (1, 1)), [[1, 0], [1, 1], [0, 1]]),
    "T": (((0, 0), (1, 0), (2, 0), (3, 0)), [[1, 1, 1], [0, 1, 0]]),
}


def rotate(tetromino: Shape):
    """
    rotate 90 deg counterclockwise
    """
    w, h = len(tetromino[0]), len(tetromino)
    rotated: list[list[int]] = []
    for i in range(w - 1, -1, -1):
        row: list[int] = []
        for j in range(h):
            row.append(tetromino[j][i])
        rotated.append(row)

    return rotated


def flip(tetromino: Shape):
    """
    flip horizontal
    """
    w, h = len(tetromino[0]), len(tetromino)
    flipped: list[list[int]] = []
    for i in range(h - 1, -1, -1):
        row: list[int] = []
        for j in range(w):
            row.append(tetromino[i][j])
        flipped.append(row)

    return flipped


def get_all_variants(tetrominos: dict[str, tuple[Variants, Shape]] = TETROMINOS):
    for _, (variants, base_shape) in tetrominos.items():
        for r, f in variants:
            shape = [row[:] for row in base_shape]
            for _ in range(r):
                shape = rotate(shape)
            for _ in range(f):
                shape = flip(shape)
            yield shape


def get_filtered_val(board: list[list[int]], kernel: list[list[int]]):
    board_w, board_h = len(board[0]), len(board)
    kernel_w, kernel_h = len(kernel[0]), len(kernel)
    for i in range(board_h - kernel_h + 1):
        for j in range(board_w - kernel_w + 1):
            conv = 0
            for ki, kernel_row in enumerate(kernel):
                for kj, e in enumerate(kernel_row):
                    conv += board[i + ki][j + kj] * e
            yield conv


def solution(board: list[list[int]]):
    max_val = 0
    for kernel in get_all_variants():
        max_val = max(max_val, max(get_filtered_val(board, kernel)))

    return max_val


if __name__ == "__main__":
    N, M = map(int, input().split())
    board: list[list[int]] = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    print(solution(board))
