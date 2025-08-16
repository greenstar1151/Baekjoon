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


def solution(n: int, m: int, grid: list[list[int]]):
    visited = [[False] * m for _ in range(n)]
    q: deque[tuple[int, tuple[int, int]]] = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                visited[i][j] = True

    q.append((0, (0, 0)))
    path_length = 0
    while q:
        depth, pos = q.popleft()
        x, y = pos
        if (x == n - 1) and (y == m - 1):
            path_length = depth
        for next_pos in get_next_moves(n, m, x, y):
            nx, ny = next_pos
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append((depth + 1, (nx, ny)))

    return path_length + 1


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    maze = [
        list(map(int, list(line))) for line in sys.stdin.read().rstrip().split("\n")
    ]
    sys.stdout.write(f"{solution(N, M, maze)}\n")
