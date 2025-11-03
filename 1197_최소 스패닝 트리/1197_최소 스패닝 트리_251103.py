import sys
import heapq

sys.setrecursionlimit(10**6 + 1)

input = sys.stdin.readline


class UF:
    def __init__(self, n: int) -> None:
        self.disjoint_set = list(range(n + 1))

    def find(self, v: int) -> int:
        if self.disjoint_set[v] == v:
            return v

        root_v = self.find(self.disjoint_set[v])
        self.disjoint_set[v] = root_v

        return root_v

    def union(self, v1: int, v2: int) -> bool:
        v1_set_root, v2_set_root = self.find(v1), self.find(v2)
        if v1_set_root == v2_set_root:
            return False

        self.disjoint_set[v2_set_root] = v1_set_root

        return True


def solution(v_count: int, edges: list[tuple[int, int, int]]):
    heapq.heapify(edges)
    uf = UF(v_count)
    mst_weight_sum = 0
    mst_edge_count = 0
    while mst_edge_count < v_count and edges:
        w, v1, v2 = heapq.heappop(edges)
        if uf.union(v1, v2):
            mst_weight_sum += w
            mst_edge_count += 1

    return mst_weight_sum


if __name__ == "__main__":
    V, E = map(int, input().split())
    edges: list[tuple[int, int, int]] = []
    for _ in range(E):
        v1, v2, weight = map(int, input().split())
        edges.append((weight, v1, v2))

    print(solution(V, edges))
