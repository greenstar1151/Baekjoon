import sys

from collections import deque
from itertools import combinations
from typing import Iterable
from copy import deepcopy


input = sys.stdin.readline

AIR = 0
WALL = 1
VIRUS = 2


def get_next_moves(x: int, y: int, x_max: int, y_max: int):
    return tuple(
        filter(
            lambda pos: 0 <= pos[0] < x_max and 0 <= pos[1] < y_max,
            [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)],
        )
    )


def spread_with_wall(new_walls: Iterable[tuple[int, int]], grid: list[list[int]]):
    new_grid = deepcopy(grid)
    for wall in new_walls:
        x, y = wall
        if grid[x][y] != AIR:
            raise ValueError
        new_grid[x][y] = WALL

    q: deque[tuple[int, int]] = deque()
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if new_grid[i][j] == VIRUS:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        new_grid[x][y] = VIRUS
        for pos in get_next_moves(x, y, len(new_grid), len(new_grid[0])):
            nx, ny = pos
            if new_grid[nx][ny] != AIR:
                continue
            q.append((nx, ny))

    return new_grid


def generate_valid_walls(
    grid: list[list[int]],
) -> Iterable[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    for comb in combinations(
        [(i, j) for j in range(len(grid[0])) for i in range(len(grid))], 3
    ):
        valid = True
        for pos in comb:
            x, y = pos
            if grid[x][y] != AIR:
                valid = False
                break
        if not valid:
            continue

        yield comb


def count_zeros(grid: list[list[int]]):
    return sum(len(list(filter(lambda x: x == AIR, row))) for row in grid)


def solution(grid: list[list[int]]):
    max_safe_area = 0
    for new_walls in generate_valid_walls(grid):
        new_grid = spread_with_wall(new_walls, grid)
        max_safe_area = max(max_safe_area, count_zeros(new_grid))

    return max_safe_area


if __name__ == "__main__":
    N, M = map(int, input().split())
    grid: list[list[int]] = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    print(solution(grid))
