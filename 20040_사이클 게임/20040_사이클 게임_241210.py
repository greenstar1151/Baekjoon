import sys

input = sys.stdin.readline


class UnionFind:
    def __init__(self, n: int):
        self.nodes = list(range(n))
        self.group_sizes = [1] * n

    def find(self, v: int) -> int:
        if self.nodes[v] == v:
            return v

        root = self.find(self.nodes[v])
        self.nodes[v] = root
        return root

    def union(self, v1: int, v2: int) -> bool:
        merge_target, to_merge = self.find(v1), self.find(v2)
        if merge_target == to_merge:
            return False

        if self.group_sizes[merge_target] < self.group_sizes[to_merge]:
            merge_target, to_merge = to_merge, merge_target

        self.nodes[to_merge] = merge_target
        self.group_sizes[merge_target] += self.group_sizes[to_merge]
        self.group_sizes[to_merge] = 0

        return True


def solution(n: int, edges: list[tuple[int, ...]]):
    uf = UnionFind(n)
    for i, e in enumerate(edges, 1):
        v1, v2 = e
        if not uf.union(v1, v2):
            break
    else:
        i = 0

    return i


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, e.split())) for e in sys.stdin.read().rstrip().split("\n")]
    print(solution(n, edges))
