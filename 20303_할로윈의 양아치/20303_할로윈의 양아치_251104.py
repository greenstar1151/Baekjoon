import sys

input = sys.stdin.readline


class UnionFind:
    def __init__(self, n: int, node_weights: list[int] | None = None):
        self.nodes = list(range(n + 1))
        self.group_sizes = [1] * n
        if node_weights is not None:
            if len(node_weights) != n:
                raise ValueError
            self.group_weights = node_weights
        else:
            self.group_weights = [1] * n

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
        self.group_weights[merge_target] += self.group_weights[to_merge]
        self.group_weights[to_merge] = 0

        return True


def solution(N: int, K: int, candies: list[int], friendships: list[tuple[int, int]]):
    uf = UnionFind(N, candies)
    for f in friendships:
        a, b = f
        uf.union(a - 1, b - 1)  # 0-based index

    groups: list[tuple[int, int]] = []
    for group_size, group_weight in zip(uf.group_sizes, uf.group_weights):
        if group_size == 0 or group_weight == 0:
            continue
        groups.append((group_size, group_weight))

    DP = [0] * (K + 1)
    for s, w in groups:
        for i in range(K, s - 1, -1):
            DP[i] = max(DP[i], DP[i - s] + w)

    return DP[K - 1]


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    candies = list(map(int, input().split()))
    friendships: list[tuple[int, int]] = []
    for _ in range(M):
        a, b = map(int, input().split())
        friendships.append((a, b))

    print(solution(N, K, candies, friendships))
