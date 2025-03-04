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
            if grid[i][j] == -1:
                visited[i][j] = True
            elif grid[i][j] == 1:
                visited[i][j] = True
                q.append((0, (i, j)))
    max_depth = 0
    while q:
        depth, pos = q.popleft()
        x, y = pos
        for next_pos in get_next_moves(n, m, x, y):
            nx, ny = next_pos
            if visited[nx][ny]:
                continue
            max_depth = max(max_depth, depth + 1)
            visited[nx][ny] = True
            q.append((depth + 1, (nx, ny)))

    if not all(all(row) for row in visited):
        return -1
    return max_depth


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    tomato_box = [
        list(map(int, line.split())) for line in sys.stdin.read().rstrip().split("\n")
    ]
    sys.stdout.write(f"{solution(N, M, tomato_box)}\n")
