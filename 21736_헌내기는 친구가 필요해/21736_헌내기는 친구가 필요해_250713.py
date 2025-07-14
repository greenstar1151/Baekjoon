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


def solution(n: int, m: int, grid: list[list[str]]):
    visited = [[False] * m for _ in range(n)]
    q: deque[tuple[int, int]] = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "X":
                visited[i][j] = True
            elif grid[i][j] == "I":
                visited[i][j] = True
                q.append((i, j))
    meet_counter = 0
    while q:
        pos = q.popleft()
        x, y = pos
        for next_pos in get_next_moves(n, m, x, y):
            nx, ny = next_pos
            if visited[nx][ny]:
                continue
            if grid[nx][ny] == "P":
                meet_counter += 1
            visited[nx][ny] = True
            q.append((nx, ny))

    return meet_counter if meet_counter > 0 else "TT"


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    campus = [list(line) for line in sys.stdin.read().rstrip().split("\n")]
    sys.stdout.write(f"{solution(N, M, campus)}\n")
