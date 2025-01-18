import sys
from collections import deque


class BFS:
    def __init__(self, n: int, m: int, map: list[list[int]]):
        self.n = n
        self.m = m
        self.map = map
        self.visited = [[False] * m for _ in range(n)]
        self.next_dir = ((-1, 0), (0, -1), (1, 0), (0, 1))
        self.cluster_sizes: list[int] = []

    def _search(self, start_x: int, start_y: int):
        if self.map[start_x][start_y] == 0:
            return
        if self.visited[start_x][start_y]:
            return

        q: deque[tuple[int, int]] = deque()
        q.append((start_x, start_y))
        counter = 0
        while q:
            x, y = q.popleft()
            if self.map[x][y] == 0:
                continue
            if self.visited[x][y]:
                continue
            self.visited[x][y] = True
            counter += 1
            for dx, dy in self.next_dir:
                if 0 <= (nx := x + dx) < n and 0 <= (ny := y + dy) < m:
                    q.append((nx, ny))

        return counter

    def search(self):
        for i in range(self.n):
            for j in range(self.m):
                cluster_size = self._search(i, j)
                if cluster_size is not None:
                    self.cluster_sizes.append(cluster_size)


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    canvas = [
        list(map(int, row.split())) for row in sys.stdin.read().rstrip().split("\n")
    ]
    bfs = BFS(n, m, canvas)
    bfs.search()
    print(f"{len(bfs.cluster_sizes)}\n{max(bfs.cluster_sizes + [0])}")
