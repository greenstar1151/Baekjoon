import sys
import heapq

input = sys.stdin.readline

# (step, s, d, z)
Data = tuple[int, int, int, int]


def invert_direction(direction: int):
    match direction:
        case 1:
            return 2
        case 2:
            return 1
        case 3:
            return 4
        case 4:
            return 3
        case _:
            raise ValueError


def get_next_pos(period: int, offset: int, move_count: int, direction: int):
    flipped = False
    if direction in (1, 4):
        flipped = True
        offset = period - offset - 1

    pos_cycle = (offset + move_count) // (period - 1)
    direction_cycle = (offset + move_count - 1) // (period - 1)
    new_offset = (offset + move_count) % (period - 1)
    if pos_cycle % 2 == 1:
        new_offset = (period - 1) - new_offset
    if direction_cycle % 2 == 1 and direction_cycle > 0:
        direction = invert_direction(direction)

    if flipped:
        new_offset = period - new_offset - 1

    return new_offset, direction


def solution(R: int, C: int, sharks: list[tuple[int, ...]]):
    grid: list[list[list[Data]]] = [[[] for _ in range(C)] for _ in range(R)]

    for shark in sharks:
        r, c, s, d, z = shark
        grid[r - 1][c - 1].append((0, s, d, z))

    caught = 0
    for step, fisher_col in enumerate(range(C)):
        # 2. Catch uppermost shark
        for i in range(R):
            if grid[i][fisher_col]:
                *_, z = grid[i][fisher_col].pop()
                caught += z
                break

        # 3-1. Move
        for row in range(R):
            for col in range(C):
                current_cell = grid[row][col]
                if not current_cell:
                    continue

                while current_cell and current_cell[0][0] == step:
                    _, s, d, z = heapq.heappop(current_cell)
                    if d in (1, 2):
                        new_offset, new_d = get_next_pos(R, row, s, d)
                        next_cell = grid[new_offset][col]
                    else:  # 3, 4
                        new_offset, new_d = get_next_pos(C, col, s, d)
                        next_cell = grid[row][new_offset]
                    heapq.heappush(next_cell, (step + 1, s, new_d, z))

        # 3-2. Merge(naive)
        for row in range(R):
            for col in range(C):
                current_cell = grid[row][col]
                if len(current_cell) < 2:
                    continue

                grid[row][col] = sorted(current_cell, key=lambda x: -x[3])[:1]

    return caught


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    sharks: list[tuple[int, ...]] = []
    for _ in range(M):
        sharks.append(tuple(map(int, input().split())))

    print(solution(R, C, sharks))
