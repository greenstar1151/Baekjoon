import sys
from collections import deque


def get_next_moves(n: int, m: int, x: int, y: int):
    MOVES = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    return tuple(
        filter(
            lambda pos: 0 <= pos[0] < n and 0 <= pos[1] < m,
            [(x + dx, y + dy) for dx, dy in MOVES],
        )
    )


def solution(n: int, m: int, given_map: list[list[int]]):
    visited = [[-1] * m for _ in range(n)]
    start_x, start_y = -1, -1
    for i in range(n):
        for j in range(m):
            if given_map[i][j] == 2:
                start_x, start_y = i, j
                visited[i][j] = 0
            elif given_map[i][j] == 0:
                visited[i][j] = 0

    q: deque[tuple[int, tuple[int, int]]] = deque()
    q.append((0, (start_x, start_y)))
    visited[start_x][start_y] = 0
    while q:
        depth, pos = q.popleft()
        x, y = pos
        for next_pos in get_next_moves(n, m, x, y):
            nx, ny = next_pos
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = depth + 1
            q.append((depth + 1, (nx, ny)))

    return visited


def format_output(grid: list[list[int]]):
    for row in grid:
        yield " ".join(map(str, row))
        yield "\n"


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    given_map = [
        list(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]
    sys.stdout.writelines(format_output(solution(n, m, given_map)))
