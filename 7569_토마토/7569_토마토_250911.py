import sys
from collections import deque


def get_next_moves(m: int, n: int, h: int, x: int, y: int, z: int):
    MOVES = [(1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

    return tuple(
        filter(
            lambda pos: 0 <= pos[0] < m and 0 <= pos[1] < n and 0 <= pos[2] < h,
            [(x + dx, y + dy, z + dz) for dx, dy, dz in MOVES],
        )
    )


def solution(M: int, N: int, H: int, warehouse: list[list[list[int]]]):
    visited: list[list[list[bool]]] = [
        [[False] * M for _ in range(N)] for _ in range(H)
    ]
    q: deque[tuple[int, tuple[int, int, int]]] = deque()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if warehouse[i][j][k] in (1, -1):
                    visited[i][j][k] = True
                    if warehouse[i][j][k] == 1:
                        q.append((0, (i, j, k)))
    max_depth = 0
    while q:
        depth, pos = q.popleft()
        z, y, x = pos
        for next_pos in get_next_moves(M, N, H, x, y, z):
            nz, ny, nx = next_pos
            next_depth = depth + 1
            if visited[nx][ny][nz]:
                continue
            max_depth = max(max_depth, next_depth)
            visited[nx][ny][nz] = True
            q.append((next_depth, (nx, ny, nz)))

    for level in visited:
        for row in level:
            if not all(row):
                return -1

    return max_depth


if __name__ == "__main__":
    stdin_data = sys.stdin.read().strip().split("\n")
    M, N, H = map(int, stdin_data[0].split())
    warehouse: list[list[list[int]]] = []
    for i in range(0, H * N, N):
        warehouse.append(
            [list(map(int, row.split())) for row in stdin_data[1 + i : 1 + i + N]]
        )

    print(solution(M, N, H, warehouse))
