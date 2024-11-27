import sys


class UF:
    """Naive implementation of union-find"""

    def __init__(self, N: int):
        self.set_array = list(range(N))
        self.v_count = [1] * N

    def find(self, i: int) -> int:
        if self.set_array[i] == i:
            return i
        return self.find(self.set_array[i])

    def union(self, i: int, j: int):
        i_root = self.find(i)
        j_root = self.find(j)

        if i_root != j_root:
            self.set_array[j_root] = i_root
            self.v_count[i_root] += self.v_count[j_root]
            self.v_count[j_root] = 0

    def subgraph_node_count(self, i: int):
        return self.v_count[self.find(i)]


def solution(V: int, edges: list[tuple[int, ...]]):
    uf = UF(V)
    for e in edges:
        v1, v2 = e
        uf.union(v1 - 1, v2 - 1)

    return uf.subgraph_node_count(0) - 1


if __name__ == "__main__":
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    if E == 0:
        print(0)
        sys.exit(0)
    edges = [
        tuple(map(int, edge.split())) for edge in sys.stdin.read().rstrip().split("\n")
    ]
    print(solution(V, edges))
